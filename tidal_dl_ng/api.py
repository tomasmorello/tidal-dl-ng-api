#!/usr/bin/env python
from typing import List, Union, Optional, Dict, Any
import uuid

from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks, Body
from pydantic import BaseModel

from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

from tidal_dl_ng import __version__
from tidal_dl_ng.config import Settings, Tidal
from tidal_dl_ng.constants import MediaType
from tidal_dl_ng.download import Download
from tidal_dl_ng.helper.path import get_format_template
from tidal_dl_ng.helper.tidal import (
    all_artist_album_ids,
    get_tidal_media_id,
    get_tidal_media_type,
    instantiate_media,
)
from tidal_dl_ng.helper.wrapper import LoggerWrapped
from tidal_dl_ng.model.cfg import HelpSettings

app = FastAPI()

class TidalContext:
    def __init__(self):
        self.settings = Settings()
        self.tidal = Tidal(self.settings)

def get_tidal_context():
    return TidalContext()

class DownloadRequest(BaseModel):
    urls: Union[List[str], str]

class DownloadManager:
    def __init__(self):
        self.active_downloads: Dict[str, Any] = {}

    def add_download(self, download_id: str, urls: List[str]):
        self.active_downloads[download_id] = {
            "urls": urls,
            "status": "in_progress",
            "progress": 0
        }

    def update_progress(self, download_id: str, progress: int):
        if download_id in self.active_downloads:
            self.active_downloads[download_id]["progress"] = progress

    def set_status(self, download_id: str, status: str):
        if download_id in self.active_downloads:
            self.active_downloads[download_id]["status"] = status

    def get_status(self, download_id: str):
        return self.active_downloads.get(download_id, None)

    def is_available(self):
        return all(download["status"] != "in_progress" for download in self.active_downloads.values())

download_manager = DownloadManager()

@app.get("/version")
async def version():
    return {"version": __version__}

@app.post("/settings")
async def settings_management(names: Optional[List[str]] = Body(None)):
    settings = Settings()
    d_settings = settings.data.to_dict()

    if names:
        if names[0] not in d_settings:
            raise HTTPException(status_code=400, detail=f'Option "{names[0]}" is not valid!')
        else:
            if len(names) == 1:
                return {names[0]: d_settings[names[0]]}
            elif len(names) > 1:
                settings.set_option(names[0], names[1])
                settings.save()
    else:
        return {"settings": d_settings}

@app.post("/login")
async def login(tidal_context: TidalContext = Depends(get_tidal_context)):
    result = tidal_context.tidal.login(fn_print=print)
    return {"login_successful": result}

@app.post("/logout")
async def logout(tidal_context: TidalContext = Depends(get_tidal_context)):
    result = tidal_context.tidal.logout()
    if result:
        return {"message": "You have been successfully logged out."}
    else:
        return {"message": "Logout failed."}

@app.post("/download")
async def download(request: DownloadRequest, background_tasks: BackgroundTasks, tidal_context: TidalContext = Depends(get_tidal_context)):
    urls = request.urls
    if isinstance(urls, str):
        urls = [urls]

    if not urls:
        raise HTTPException(status_code=400, detail="Provide at least one URL")

    settings = tidal_context.settings

    # Genera un ID único para la descarga
    download_id = str(uuid.uuid4())
    download_manager.add_download(download_id, urls)

    background_tasks.add_task(process_download, download_id, urls, settings, tidal_context)

    return {"status": "Download started", "download_id": download_id}

def process_download(download_id: str, urls: List[str], settings: Settings, tidal_context: TidalContext):
    progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    fn_logger = LoggerWrapped(print)
    dl = Download(
        session=tidal_context.tidal.session,
        skip_existing=settings.data.skip_existing,
        path_base=settings.data.download_base_path,
        fn_logger=fn_logger,
        progress=progress,
    )

    urls_pos_last = len(urls) - 1

    for item in urls:
        media_type = False

        if "http" in item:
            media_type = get_tidal_media_type(item)
            item_id = get_tidal_media_id(item)
            file_template = get_format_template(media_type, settings)

        if not media_type:
            print(f"It seems like that you have supplied an invalid URL: {item}")
            continue

        if media_type in [MediaType.TRACK, MediaType.VIDEO]:
            download_delay = bool(settings.data.download_delay and urls.index(item) < urls_pos_last)
            dl.item(media_id=item_id, media_type=media_type, file_template=file_template, download_delay=download_delay)
        elif media_type in [MediaType.ALBUM, MediaType.PLAYLIST, MediaType.MIX, MediaType.ARTIST]:
            item_ids = []

            if media_type == MediaType.ARTIST:
                media = instantiate_media(tidal_context.tidal.session, media_type, item_id)
                media_type = MediaType.ALBUM
                item_ids += all_artist_album_ids(media)
            else:
                item_ids.append(item_id)

            for item_id in item_ids:
                dl.items(
                    media_id=item_id,
                    media_type=media_type,
                    file_template=file_template,
                    video_download=settings.data.video_download,
                    download_delay=settings.data.download_delay,
                )

    download_manager.set_status(download_id, "completed")

@app.get("/download/status/{download_id}")
async def get_download_status(download_id: str):
    status = download_manager.get_status(download_id)
    if status is None:
        raise HTTPException(status_code=404, detail="Download not found")
    return status

@app.get("/download/availability")
async def check_availability():
    available = download_manager.is_available()
    return {"available": available}
