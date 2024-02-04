################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QLocale, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QAbstractItemView,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QMenu,
    QMenuBar,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.a_preferences = QAction(MainWindow)
        self.a_preferences.setObjectName("a_preferences")
        self.a_preferences.setEnabled(True)
        self.a_preferences.setText("Preferences...")
        self.a_preferences.setIconText("Preferences...")
        # if QT_CONFIG(tooltip)
        self.a_preferences.setToolTip("Preferences...")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.a_preferences.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.a_preferences.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.a_version = QAction(MainWindow)
        self.a_version.setObjectName("a_version")
        self.a_exit = QAction(MainWindow)
        self.a_exit.setObjectName("a_exit")
        self.w_central = QWidget(MainWindow)
        self.w_central.setObjectName("w_central")
        self.w_central.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.w_central.sizePolicy().hasHeightForWidth())
        self.w_central.setSizePolicy(sizePolicy)
        # if QT_CONFIG(tooltip)
        self.w_central.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.w_central.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.w_central.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.w_central.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.w_central.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.horizontalLayout = QHBoxLayout(self.w_central)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lh_main = QHBoxLayout()
        self.lh_main.setObjectName("lh_main")
        self.lh_main.setSizeConstraint(QLayout.SetNoConstraint)
        self.tr_lists_user = QTreeWidget(self.w_central)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, "Info")
        __qtreewidgetitem.setText(0, "Playlist")
        self.tr_lists_user.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.tr_lists_user)
        __qtreewidgetitem1.setFlags(Qt.ItemIsEnabled)
        __qtreewidgetitem2 = QTreeWidgetItem(self.tr_lists_user)
        __qtreewidgetitem2.setFlags(Qt.ItemIsEnabled)
        __qtreewidgetitem3 = QTreeWidgetItem(self.tr_lists_user)
        __qtreewidgetitem3.setFlags(Qt.ItemIsEnabled)
        self.tr_lists_user.setObjectName("tr_lists_user")
        # if QT_CONFIG(tooltip)
        self.tr_lists_user.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.tr_lists_user.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.tr_lists_user.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.tr_lists_user.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.tr_lists_user.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.tr_lists_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tr_lists_user.setProperty("showDropIndicator", False)
        self.tr_lists_user.setIndentation(10)
        self.tr_lists_user.setUniformRowHeights(True)
        self.tr_lists_user.setSortingEnabled(True)
        self.tr_lists_user.header().setCascadingSectionResizes(True)
        self.tr_lists_user.header().setHighlightSections(True)
        self.tr_lists_user.header().setProperty("showSortIndicator", True)

        self.lh_main.addWidget(self.tr_lists_user)

        self.lv_search_result = QVBoxLayout()
        # ifndef Q_OS_MAC
        self.lv_search_result.setSpacing(-1)
        # endif
        self.lv_search_result.setObjectName("lv_search_result")
        self.lh_search = QHBoxLayout()
        self.lh_search.setObjectName("lh_search")
        self.l_search = QLineEdit(self.w_central)
        self.l_search.setObjectName("l_search")
        self.l_search.setAcceptDrops(False)
        # if QT_CONFIG(tooltip)
        self.l_search.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.l_search.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.l_search.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.l_search.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.l_search.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.l_search.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.l_search.setText("")
        self.l_search.setPlaceholderText("Type and press ENTER to search...")
        self.l_search.setClearButtonEnabled(True)

        self.lh_search.addWidget(self.l_search)

        self.cb_search_type = QComboBox(self.w_central)
        self.cb_search_type.setObjectName("cb_search_type")
        # if QT_CONFIG(tooltip)
        self.cb_search_type.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cb_search_type.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.cb_search_type.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.cb_search_type.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.cb_search_type.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.cb_search_type.setCurrentText("")
        self.cb_search_type.setPlaceholderText("")

        self.lh_search.addWidget(self.cb_search_type)

        self.b_search = QPushButton(self.w_central)
        self.b_search.setObjectName("b_search")
        # if QT_CONFIG(statustip)
        self.b_search.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.b_search.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.b_search.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.b_search.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.b_search.setText("Search")
        # if QT_CONFIG(shortcut)
        self.b_search.setShortcut("")
        # endif // QT_CONFIG(shortcut)

        self.lh_search.addWidget(self.b_search)

        self.lv_search_result.addLayout(self.lh_search)

        self.tr_results = QTreeWidget(self.w_central)
        self.tr_results.setObjectName("tr_results")
        self.tr_results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tr_results.setProperty("showDropIndicator", False)
        self.tr_results.setDragDropOverwriteMode(False)
        self.tr_results.setAlternatingRowColors(False)
        self.tr_results.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tr_results.setIndentation(10)
        self.tr_results.setSortingEnabled(True)
        self.tr_results.header().setProperty("showSortIndicator", True)
        self.tr_results.header().setStretchLastSection(False)

        self.lv_search_result.addWidget(self.tr_results)

        self.lh_download = QHBoxLayout()
        self.lh_download.setObjectName("lh_download")
        self.l_quality_audio = QLabel(self.w_central)
        self.l_quality_audio.setObjectName("l_quality_audio")
        # if QT_CONFIG(tooltip)
        self.l_quality_audio.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.l_quality_audio.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.l_quality_audio.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.l_quality_audio.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.l_quality_audio.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.l_quality_audio.setText("Audio")
        self.l_quality_audio.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.lh_download.addWidget(self.l_quality_audio)

        self.cb_quality_audio = QComboBox(self.w_central)
        self.cb_quality_audio.setObjectName("cb_quality_audio")
        # if QT_CONFIG(tooltip)
        self.cb_quality_audio.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cb_quality_audio.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.cb_quality_audio.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.cb_quality_audio.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.cb_quality_audio.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.cb_quality_audio.setCurrentText("")
        self.cb_quality_audio.setPlaceholderText("")
        self.cb_quality_audio.setFrame(True)

        self.lh_download.addWidget(self.cb_quality_audio)

        self.l_quality_video = QLabel(self.w_central)
        self.l_quality_video.setObjectName("l_quality_video")
        # if QT_CONFIG(tooltip)
        self.l_quality_video.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.l_quality_video.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.l_quality_video.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.l_quality_video.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.l_quality_video.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.l_quality_video.setText("Video")
        self.l_quality_video.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.lh_download.addWidget(self.l_quality_video)

        self.cb_quality_video = QComboBox(self.w_central)
        self.cb_quality_video.setObjectName("cb_quality_video")
        # if QT_CONFIG(tooltip)
        self.cb_quality_video.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.cb_quality_video.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.cb_quality_video.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.cb_quality_video.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.cb_quality_video.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.cb_quality_video.setCurrentText("")
        self.cb_quality_video.setPlaceholderText("")

        self.lh_download.addWidget(self.cb_quality_video)

        self.b_download = QPushButton(self.w_central)
        self.b_download.setObjectName("b_download")
        # if QT_CONFIG(tooltip)
        self.b_download.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.b_download.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.b_download.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.b_download.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.b_download.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.b_download.setText("Download")
        # if QT_CONFIG(shortcut)
        self.b_download.setShortcut("")
        # endif // QT_CONFIG(shortcut)

        self.lh_download.addWidget(self.b_download)

        self.lh_download.setStretch(0, 5)
        self.lh_download.setStretch(2, 5)
        self.lh_download.setStretch(4, 15)

        self.lv_search_result.addLayout(self.lh_download)

        self.te_debug = QPlainTextEdit(self.w_central)
        self.te_debug.setObjectName("te_debug")
        self.te_debug.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.te_debug.sizePolicy().hasHeightForWidth())
        self.te_debug.setSizePolicy(sizePolicy1)
        self.te_debug.setMaximumSize(QSize(16777215, 16777215))
        self.te_debug.setAcceptDrops(False)
        # if QT_CONFIG(tooltip)
        self.te_debug.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.te_debug.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.te_debug.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.te_debug.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.te_debug.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.te_debug.setUndoRedoEnabled(False)
        self.te_debug.setReadOnly(True)

        self.lv_search_result.addWidget(self.te_debug)

        self.lh_main.addLayout(self.lv_search_result)

        self.lh_main.setStretch(0, 40)
        self.lh_main.setStretch(1, 60)

        self.horizontalLayout.addLayout(self.lh_main)

        MainWindow.setCentralWidget(self.w_central)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 24))
        # if QT_CONFIG(tooltip)
        self.menubar.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.menubar.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.menubar.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.menubar.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.menubar.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.m_file = QMenu(self.menubar)
        self.m_file.setObjectName("m_file")
        # if QT_CONFIG(tooltip)
        self.m_file.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.m_file.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.m_file.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.m_file.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.m_file.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # if QT_CONFIG(tooltip)
        self.statusbar.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.statusbar.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(accessibility)
        self.statusbar.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(accessibility)
        self.statusbar.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.statusbar.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.m_file.menuAction())
        self.m_file.addAction(self.a_preferences)
        self.m_file.addAction(self.a_version)
        self.m_file.addAction(self.a_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.a_version.setText(QCoreApplication.translate("MainWindow", "Version", None))
        self.a_exit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        ___qtreewidgetitem = self.tr_lists_user.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", "obj", None))

        __sortingEnabled = self.tr_lists_user.isSortingEnabled()
        self.tr_lists_user.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tr_lists_user.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", "Playlists", None))
        ___qtreewidgetitem2 = self.tr_lists_user.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", "Mixes", None))
        ___qtreewidgetitem3 = self.tr_lists_user.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", "Favorites", None))
        self.tr_lists_user.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem4 = self.tr_results.headerItem()
        ___qtreewidgetitem4.setText(5, QCoreApplication.translate("MainWindow", "obj", None))
        ___qtreewidgetitem4.setText(4, QCoreApplication.translate("MainWindow", "Duration", None))
        ___qtreewidgetitem4.setText(3, QCoreApplication.translate("MainWindow", "Album", None))
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", "Title", None))
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", "Artist", None))
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", "#", None))
        self.te_debug.setPlaceholderText(QCoreApplication.translate("MainWindow", "Logs...", None))
        self.m_file.setTitle(QCoreApplication.translate("MainWindow", "File", None))

    # retranslateUi
