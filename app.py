from PySide2.QtCore import (QCoreApplication, QMetaObject, QTimer, QRect, QSize, Qt, QEasingCurve, QPropertyAnimation)
from PySide2.QtGui import (QFont, QIcon, QPixmap)
from PySide2.QtWidgets import *
import mysql.connector as mys
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 625)
        MainWindow.setMinimumSize(QSize(1000, 625))
        MainWindow.setMaximumSize(QSize(1000, 625))
        MainWindow.setStyleSheet(u"background-color: #FFFFFF")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 600))
        self.centralwidget.setMaximumSize(QSize(1000, 600))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 55))
        self.Top_Bar.setStyleSheet(u"background-color: white;")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 50))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""border:none;")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"QPushButton {\n""	background-color: rgb(255, 255, 255);\n""	border:0px solid;\n""}\n""QPushButton:hover {\n""	background-color: grey;\n""}\n""")
        icon = QIcon()
        icon.addFile(u"project/lightning-fill 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"background-color: white;")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.app_name = QLabel(self.frame_top)
        self.app_name.setObjectName(u"app_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.app_name.sizePolicy().hasHeightForWidth())
        self.app_name.setSizePolicy(sizePolicy1)
        self.app_name.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"SF Pro Display")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.app_name.setFont(font)
        self.app_name.setStyleSheet(u"color: #000;\n""background-color: rgb(255, 255, 255);\n""border:none;")
        self.app_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.app_name)
        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_pages)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_pages)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_top_menus.sizePolicy().hasHeightForWidth())
        self.frame_top_menus.setSizePolicy(sizePolicy2)
        self.frame_top_menus.setMinimumSize(QSize(0, 0))
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.frame_top_menus)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"SF Pro Display")
        self.home_btn.setFont(font1)
        self.home_btn.setStyleSheet(u"QPushButton {\n""	color: #000000;\n""	background-color: #FFFFFF;\n""	border: 0px solid;\n""}\n""QPushButton:hover {\n""	background-color: grey;\n""}\n""")
        icon1 = QIcon()
        icon1.addFile(u"project/25694.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.home_btn)

        self.project_btn = QPushButton(self.frame_top_menus)
        self.project_btn.setObjectName(u"project_btn")
        self.project_btn.setMinimumSize(QSize(0, 40))
        self.project_btn.setFont(font1)
        self.project_btn.setStyleSheet(u"QPushButton {\n""	color: #000000;\n""	background-color: #FFFFFF;\n""	border: 0px solid;\n""}\n""QPushButton:hover {\n""	background-color: grey;\n""}\n""")
        icon2 = QIcon()
        icon2.addFile(u"project/target-front-color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.project_btn.setIcon(icon2)
        self.project_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.project_btn)

        self.tasks_btn = QPushButton(self.frame_top_menus)
        self.tasks_btn.setObjectName(u"tasks_btn")
        self.tasks_btn.setMinimumSize(QSize(0, 40))
        self.tasks_btn.setFont(font1)
        self.tasks_btn.setStyleSheet(u"QPushButton {\n"
"	color: #000000;\n"
"	background-color: #FFFFFF;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"project/tick-front-color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tasks_btn.setIcon(icon3)
        self.tasks_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.tasks_btn)

        self.analytics_btn = QPushButton(self.frame_top_menus)
        self.analytics_btn.setObjectName(u"analytics_btn")
        self.analytics_btn.setMinimumSize(QSize(0, 40))
        self.analytics_btn.setFont(font1)
        self.analytics_btn.setStyleSheet(u"QPushButton {\n"
"	color: #000000;\n"
"	background-color: #FFFFFF;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"project/Calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.analytics_btn.setIcon(icon4)
        self.analytics_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.analytics_btn)

        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.horizontalLayout_12.addWidget(self.frame_left_menu)

        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.horizontalLayout_15 = QHBoxLayout(self.home_page)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.home_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_14)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.home_content = QListWidget(self.frame_7)
        self.home_content.setObjectName(u"home_content")
        self.home_content.setGeometry(QRect(80, 160, 331, 301))
        font2 = QFont()
        font2.setPointSize(13)
        self.home_content.setFont(font2)
        self.home_content.setStyleSheet(u"color: #000000;\n""border:none;")
        self.home_content.setSpacing(10)
        self.home_content.setViewMode(QListView.ListMode)
        self.home_content.setSortingEnabled(True)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 0, 321, 81))
        self.label_2.setFont(font1)
        self.label_2.setPixmap(QPixmap(u"project/Welcome back..png"))
        self.tasks_heading_8 = QLabel(self.frame_7)
        self.tasks_heading_8.setObjectName(u"tasks_heading_8")
        self.tasks_heading_8.setGeometry(QRect(80, 60, 221, 81))
        self.tasks_heading_8.setMinimumSize(QSize(0, 70))
        font3 = QFont()
        font3.setFamily(u"SF Pro Display")
        font3.setPointSize(33)
        font3.setBold(False)
        font3.setWeight(50)
        self.tasks_heading_8.setFont(font3)
        self.tasks_heading_8.setStyleSheet(u"color:black;")
        self.tasks_heading_8.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(280, 90, 31, 41))
        self.pushButton_4.setStyleSheet(u"border:none;\n""")
        icon5 = QIcon()
        icon5.addFile(u"project/caret-circle-down-fill 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 130, 171, 16))
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setPixmap(QPixmap(u"project/Line 1.png"))

        self.horizontalLayout_16.addWidget(self.frame_7)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 500))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_15)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 100, 0, 150)
        self.tasks_heading_9 = QLabel(self.frame_15)
        self.tasks_heading_9.setObjectName(u"tasks_heading_9")
        self.tasks_heading_9.setMinimumSize(QSize(0, 70))
        font4 = QFont()
        font4.setPointSize(22)
        self.tasks_heading_9.setFont(font4)
        self.tasks_heading_9.setStyleSheet(u"color: black;")
        self.tasks_heading_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.tasks_heading_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.timer1 = QLabel(self.frame_15)
        self.timer1.setObjectName(u"timer1")
        font5 = QFont()
        font5.setFamily(u"SF Pro Display")
        font5.setPointSize(70)
        font5.setBold(True)
        font5.setWeight(75)
        self.timer1.setFont(font5)
        self.timer1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.timer1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.start_button_4 = QPushButton(self.frame_15)
        self.start_button_4.setObjectName(u"start_button_4")
        self.start_button_4.setMinimumSize(QSize(0, 50))
        font6 = QFont()
        font6.setFamily(u"SF Pro Display")
        font6.setPointSize(15)
        font6.setBold(False)
        font6.setWeight(50)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.start_button_4.setFont(font6)
        self.start_button_4.setStyleSheet(u"QPushButton {\n"
"	background-color:#F2F2F7;\n"
"	color:grey;\n"
"	border:2px solid #F2F2F7;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"project/Icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_button_4.setIcon(icon6)

        self.verticalLayout_8.addWidget(self.start_button_4, 0, Qt.AlignHCenter)
        self.horizontalLayout_16.addWidget(self.frame_15)

        self.horizontalLayout_15.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.home_page)
        self.projects_page = QWidget()
        self.projects_page.setObjectName(u"projects_page")
        self.projects_page.setStyleSheet(u"")
        self.horizontalLayout_13 = QHBoxLayout(self.projects_page)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.projects_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(500, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.addnew_project_btn = QPushButton(self.frame_11)
        self.addnew_project_btn.setObjectName(u"addnew_project_btn")
        self.addnew_project_btn.setGeometry(QRect(160, 400, 171, 50))
        self.addnew_project_btn.setMinimumSize(QSize(0, 50))
        self.addnew_project_btn.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"SF Pro Display")
        font7.setPointSize(15)
        self.addnew_project_btn.setFont(font7)
        self.addnew_project_btn.setMouseTracking(False)
        self.addnew_project_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"	color:grey;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"project/plus-bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addnew_project_btn.setIcon(icon7)
        self.addnew_project_btn.setIconSize(QSize(20, 20))
        self.tasks_heading_5 = QLabel(self.frame_11)
        self.tasks_heading_5.setObjectName(u"tasks_heading_5")
        self.tasks_heading_5.setGeometry(QRect(30, 30, 341, 81))
        self.tasks_heading_5.setMinimumSize(QSize(0, 70))
        font8 = QFont()
        font8.setFamily(u"SF Pro Display")
        font8.setPointSize(40)
        font8.setBold(False)
        font8.setWeight(50)
        self.tasks_heading_5.setFont(font8)
        self.tasks_heading_5.setStyleSheet(u"color:black;")
        self.tasks_heading_5.setAlignment(Qt.AlignCenter)
        self.pushButton_3 = QPushButton(self.frame_11)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(370, 60, 51, 41))
        self.pushButton_3.setStyleSheet(u"border:none;\n"
"")
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.projects_list = QListWidget(self.frame_11)
        self.projects_list.setObjectName(u"projects_list")
        self.projects_list.setGeometry(QRect(60, 130, 371, 271))
        font9 = QFont()
        font9.setPointSize(15)
        self.projects_list.setFont(font9)
        self.projects_list.setStyleSheet(u"color:black;\n"
"border:none;")
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 110, 251, 16))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setPixmap(QPixmap(u"project/Line2.png"))

        self.horizontalLayout_13.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.projects_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 500))
        self.frame_12.setMaximumSize(QSize(500, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 100, 0, 150)
        self.tasks_heading_6 = QLabel(self.frame_12)
        self.tasks_heading_6.setObjectName(u"tasks_heading_6")
        self.tasks_heading_6.setMinimumSize(QSize(0, 50))
        self.tasks_heading_6.setFont(font4)
        self.tasks_heading_6.setStyleSheet(u"color: black;")
        self.tasks_heading_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.tasks_heading_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.timer2 = QLabel(self.frame_12)
        self.timer2.setObjectName(u"timer2")
        self.timer2.setFont(font5)
        self.timer2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.timer2, 0, Qt.AlignVCenter)

        self.start_button_3 = QPushButton(self.frame_12)
        self.start_button_3.setObjectName(u"start_button_3")
        self.start_button_3.setMinimumSize(QSize(0, 50))
        self.start_button_3.setFont(font6)
        self.start_button_3.setStyleSheet(u"QPushButton {\n"
"	background-color:#F2F2F7;\n"
"	color:grey;\n"
"	border:2px solid #F2F2F7;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.start_button_3.setIcon(icon6)

        self.verticalLayout_6.addWidget(self.start_button_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.projects_page)
        self.tasks_page = QWidget()
        self.tasks_page.setObjectName(u"tasks_page")
        self.tasks_page.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.tasks_page)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.tasks_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.tasks_heading = QLabel(self.frame_17)
        self.tasks_heading.setObjectName(u"tasks_heading")
        self.tasks_heading.setGeometry(QRect(70, 30, 291, 81))
        self.tasks_heading.setMinimumSize(QSize(0, 70))
        self.tasks_heading.setFont(font8)
        self.tasks_heading.setStyleSheet(u"color:black;")
        self.tasks_heading.setAlignment(Qt.AlignCenter)
        self.tasks_list = QListWidget(self.frame_17)
        self.tasks_list.setObjectName(u"tasks_list")
        self.tasks_list.setGeometry(QRect(70, 130, 371, 251))
        self.tasks_list.setFont(font9)
        self.tasks_list.setStyleSheet(u"color:black;\n"
"border:none;")
        self.pushButton = QPushButton(self.frame_17)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 60, 51, 41))
        self.pushButton.setStyleSheet(u"border:none;\n"
"")
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(30, 30))
        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(80, 100, 181, 16))
        self.label_21.setLayoutDirection(Qt.LeftToRight)
        self.label_21.setPixmap(QPixmap(u"project/Line2.png"))

        self.horizontalLayout_18.addWidget(self.frame_17)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 500))
        self.frame_10.setMaximumSize(QSize(500, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 100, 0, 150)
        self.tasks_heading_2 = QLabel(self.frame_10)
        self.tasks_heading_2.setObjectName(u"tasks_heading_2")
        self.tasks_heading_2.setMinimumSize(QSize(0, 70))
        self.tasks_heading_2.setFont(font4)
        self.tasks_heading_2.setStyleSheet(u"color: black;")
        self.tasks_heading_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.tasks_heading_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.timer3 = QLabel(self.frame_10)
        self.timer3.setObjectName(u"timer3")
        self.timer3.setFont(font5)
        self.timer3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.timer3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.start_button = QPushButton(self.frame_10)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 50))
        self.start_button.setFont(font6)
        self.start_button.setStyleSheet(u"QPushButton {\n"
"	background-color:#F2F2F7;\n"
"	color:grey;\n"
"	border:2px solid #F2F2F7;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.start_button.setIcon(icon6)

        self.verticalLayout_9.addWidget(self.start_button, 0, Qt.AlignHCenter)
        self.horizontalLayout_18.addWidget(self.frame_10)
        self.horizontalLayout_7.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.tasks_page)
        self.analytics_page = QWidget()
        self.analytics_page.setObjectName(u"analytics_page")
        self.analytics_page.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.analytics_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.analytics_heading = QLabel(self.analytics_page)
        self.analytics_heading.setObjectName(u"analytics_heading")
        self.analytics_heading.setMaximumSize(QSize(16777215, 80))
        self.analytics_heading.setFont(font8)
        self.analytics_heading.setStyleSheet(u"color: black;")
        self.analytics_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.analytics_heading)

        self.frame_13 = QFrame(self.analytics_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color:white;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(30, -1, 30, -1)
        self.analytics_calendar = QCalendarWidget(self.frame_13)
        self.analytics_calendar.setObjectName(u"analytics_calendar")
        self.analytics_calendar.setMaximumSize(QSize(350, 300))
        self.analytics_calendar.setStyleSheet(u"background-color: rgb(141, 219, 129);")

        self.horizontalLayout_14.addWidget(self.analytics_calendar)

        self.arrow = QLabel(self.frame_13)
        self.arrow.setObjectName(u"arrow")
        self.arrow.setMaximumSize(QSize(130, 80))
        self.arrow.setPixmap(QPixmap(u"project/Arrow 3.png"))
        self.arrow.setScaledContents(False)

        self.horizontalLayout_14.addWidget(self.arrow)

        self.analytics_tasks = QListWidget(self.frame_13)
        self.analytics_tasks.setObjectName(u"analytics_tasks")
        self.analytics_tasks.setMaximumSize(QSize(300, 300))
        self.analytics_tasks.setStyleSheet(u"border:none;\n"
"color:black;")

        self.horizontalLayout_14.addWidget(self.analytics_tasks)
        self.verticalLayout_7.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.analytics_page)
        self.addnew_task = QWidget()
        self.addnew_task.setObjectName(u"addnew_task")
        self.verticalLayout_5 = QVBoxLayout(self.addnew_task)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.new_task_heading = QLabel(self.addnew_task)
        self.new_task_heading.setObjectName(u"new_task_heading")
        self.new_task_heading.setMinimumSize(QSize(0, 70))
        font10 = QFont()
        font10.setFamily(u"SF Pro Display")
        font10.setPointSize(30)
        font10.setBold(True)
        font10.setWeight(75)
        self.new_task_heading.setFont(font10)
        self.new_task_heading.setStyleSheet(u"color: black;")
        self.new_task_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.new_task_heading)

        self.change_task_name = QLineEdit(self.addnew_task)
        self.change_task_name.setObjectName(u"change_task_name")
        self.change_task_name.setMinimumSize(QSize(0, 40))
        font11 = QFont()
        font11.setPointSize(20)
        font11.setUnderline(True)
        self.change_task_name.setFont(font11)
        self.change_task_name.setStyleSheet(u"color: #8DDB81;")
        self.change_task_name.setFrame(False)
        self.change_task_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.change_task_name)

        self.new_task_desc = QTextEdit(self.addnew_task)
        self.new_task_desc.setObjectName(u"new_task_desc")
        font12 = QFont()
        font12.setPointSize(11)
        self.new_task_desc.setFont(font12)
        self.new_task_desc.setStyleSheet(u"color: black;")

        self.verticalLayout_5.addWidget(self.new_task_desc)

        self.extra_task_options_frame = QFrame(self.addnew_task)
        self.extra_task_options_frame.setObjectName(u"extra_task_options_frame")
        self.extra_task_options_frame.setMinimumSize(QSize(0, 80))
        self.extra_task_options_frame.setFrameShape(QFrame.StyledPanel)
        self.extra_task_options_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extra_task_options_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.deadline_frame = QFrame(self.extra_task_options_frame)
        self.deadline_frame.setObjectName(u"deadline_frame")
        self.deadline_frame.setMinimumSize(QSize(0, 50))
        self.deadline_frame.setFrameShape(QFrame.StyledPanel)
        self.deadline_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.deadline_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.dframe_label = QLabel(self.deadline_frame)
        self.dframe_label.setObjectName(u"dframe_label")
        font13 = QFont()
        font13.setPointSize(12)
        self.dframe_label.setFont(font13)
        self.dframe_label.setStyleSheet(u"color: #000000;")
        self.dframe_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.dframe_label)

        self.task_datetime = QDateTimeEdit(self.deadline_frame)
        self.task_datetime.setObjectName(u"task_datetime")
        self.task_datetime.setMinimumSize(QSize(0, 40))
        self.task_datetime.setFont(font13)
        self.task_datetime.setStyleSheet(u"color: #000000;")
        self.task_datetime.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.task_datetime)
        self.verticalLayout_11.addWidget(self.deadline_frame)

        self.priority_frame = QFrame(self.extra_task_options_frame)
        self.priority_frame.setObjectName(u"priority_frame")
        self.priority_frame.setMinimumSize(QSize(0, 50))
        self.priority_frame.setFrameShape(QFrame.StyledPanel)
        self.priority_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.priority_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pframe_label = QLabel(self.priority_frame)
        self.pframe_label.setObjectName(u"pframe_label")
        self.pframe_label.setFont(font13)
        self.pframe_label.setStyleSheet(u"color: black;\n"
"")
        self.pframe_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.pframe_label)

        self.priority_task_combo = QComboBox(self.priority_frame)
        self.priority_task_combo.setObjectName(u"priority_task_combo")
        self.priority_task_combo.setFont(font13)
        self.priority_task_combo.setStyleSheet(u"color: black;")

        self.horizontalLayout_6.addWidget(self.priority_task_combo)
        self.verticalLayout_11.addWidget(self.priority_frame)
        self.verticalLayout_5.addWidget(self.extra_task_options_frame)

        self.save_task_change = QPushButton(self.addnew_task)
        self.save_task_change.setObjectName(u"save_task_change")
        self.save_task_change.setMinimumSize(QSize(0, 50))
        self.save_task_change.setFont(font13)
        self.save_task_change.setStyleSheet(u"QPushButton {\n"
"	color: #8DDB81;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"project/check-bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_task_change.setIcon(icon8)
        self.save_task_change.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.save_task_change)

        self.cancel_task_change = QPushButton(self.addnew_task)
        self.cancel_task_change.setObjectName(u"cancel_task_change")
        self.cancel_task_change.setMinimumSize(QSize(0, 50))
        self.cancel_task_change.setFont(font13)
        self.cancel_task_change.setStyleSheet(u"QPushButton {\n"
"	color: red;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"project/x-bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_task_change.setIcon(icon9)
        self.cancel_task_change.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.cancel_task_change)

        self.stackedWidget.addWidget(self.addnew_task)
        self.addnew_project = QWidget()
        self.addnew_project.setObjectName(u"addnew_project")
        self.verticalLayout_12 = QVBoxLayout(self.addnew_project)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.new_project_heading = QLabel(self.addnew_project)
        self.new_project_heading.setObjectName(u"new_project_heading")
        self.new_project_heading.setMinimumSize(QSize(0, 70))
        self.new_project_heading.setFont(font10)
        self.new_project_heading.setStyleSheet(u"")
        self.new_project_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.new_project_heading)

        self.change_project_name = QLineEdit(self.addnew_project)
        self.change_project_name.setObjectName(u"change_project_name")
        self.change_project_name.setMinimumSize(QSize(0, 40))
        font14 = QFont()
        font14.setFamily(u"SF Pro Display")
        font14.setPointSize(20)
        font14.setUnderline(True)
        self.change_project_name.setFont(font14)
        self.change_project_name.setStyleSheet(u"color: #8DDB81;\n"
"border:none;")
        self.change_project_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.change_project_name)

        self.new_project_desc = QTextEdit(self.addnew_project)
        self.new_project_desc.setObjectName(u"new_project_desc")
        self.new_project_desc.setFont(font12)
        self.new_project_desc.setStyleSheet(u"color: black;\n"
"border-color:black;")

        self.verticalLayout_12.addWidget(self.new_project_desc)

        self.save_project_change = QPushButton(self.addnew_project)
        self.save_project_change.setObjectName(u"save_project_change")
        self.save_project_change.setMinimumSize(QSize(0, 50))
        self.save_project_change.setFont(font13)
        self.save_project_change.setStyleSheet(u"QPushButton {\n"
"	color: #8DDB81;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        self.save_project_change.setIcon(icon8)
        self.save_project_change.setIconSize(QSize(20, 20))

        self.verticalLayout_12.addWidget(self.save_project_change)

        self.cancel_project_change = QPushButton(self.addnew_project)
        self.cancel_project_change.setObjectName(u"cancel_project_change")
        self.cancel_project_change.setMinimumSize(QSize(0, 50))
        self.cancel_project_change.setFont(font13)
        self.cancel_project_change.setStyleSheet(u"QPushButton {\n"
"	color: red;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        self.cancel_project_change.setIcon(icon9)
        self.cancel_project_change.setIconSize(QSize(20, 20))

        self.verticalLayout_12.addWidget(self.cancel_project_change)

        self.stackedWidget.addWidget(self.addnew_project)
        self.edit_project = QWidget()
        self.edit_project.setObjectName(u"edit_project")
        self.verticalLayout_17 = QVBoxLayout(self.edit_project)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.edit_project_heading = QLabel(self.edit_project)
        self.edit_project_heading.setObjectName(u"edit_project_heading")
        self.edit_project_heading.setMinimumSize(QSize(0, 70))
        self.edit_project_heading.setFont(font10)
        self.edit_project_heading.setStyleSheet(u"")
        self.edit_project_heading.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.edit_project_heading)

        self.edit_project_name = QLineEdit(self.edit_project)
        self.edit_project_name.setObjectName(u"edit_project_name")
        self.edit_project_name.setMinimumSize(QSize(0, 40))
        self.edit_project_name.setFont(font14)
        self.edit_project_name.setStyleSheet(u"color: #8DDB81; ")
        self.edit_project_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.edit_project_name)

        self.edit_project_desc = QTextEdit(self.edit_project)
        self.edit_project_desc.setObjectName(u"edit_project_desc")
        self.edit_project_desc.setFont(font12)
        self.edit_project_desc.setStyleSheet(u"color: black;")

        self.verticalLayout_17.addWidget(self.edit_project_desc)

        self.save_project_edit = QPushButton(self.edit_project)
        self.save_project_edit.setObjectName(u"save_project_edit")
        self.save_project_edit.setMinimumSize(QSize(0, 50))
        self.save_project_edit.setFont(font13)
        self.save_project_edit.setStyleSheet(u"QPushButton {\n"
"	color: #8DDB81;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        self.save_project_edit.setIcon(icon8)
        self.save_project_edit.setIconSize(QSize(20, 20))

        self.verticalLayout_17.addWidget(self.save_project_edit)

        self.cancel_project_edit = QPushButton(self.edit_project)
        self.cancel_project_edit.setObjectName(u"cancel_project_edit")
        self.cancel_project_edit.setMinimumSize(QSize(0, 50))
        self.cancel_project_edit.setFont(font13)
        self.cancel_project_edit.setStyleSheet(u"QPushButton {\n"
"	color: red;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        self.cancel_project_edit.setIcon(icon9)
        self.cancel_project_edit.setIconSize(QSize(20, 20))

        self.verticalLayout_17.addWidget(self.cancel_project_edit)

        self.stackedWidget.addWidget(self.edit_project)
        self.current_project = QWidget()
        self.current_project.setObjectName(u"current_project")
        self.current_project.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_4 = QHBoxLayout(self.current_project)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.current_project)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.project_name_main = QLabel(self.frame_16)
        self.project_name_main.setObjectName(u"project_name_main")
        self.project_name_main.setGeometry(QRect(30, 10, 451, 80))
        self.project_name_main.setMinimumSize(QSize(0, 70))
        font15 = QFont()
        font15.setFamily(u"SF Pro Display")
        font15.setPointSize(30)
        font15.setBold(False)
        font15.setWeight(50)
        self.project_name_main.setFont(font15)
        self.project_name_main.setStyleSheet(u"color:black;")
        self.project_name_main.setAlignment(Qt.AlignCenter)
        self.delete_project = QPushButton(self.frame_16)
        self.delete_project.setObjectName(u"delete_project")
        self.delete_project.setGeometry(QRect(210, 480, 121, 50))
        self.delete_project.setMinimumSize(QSize(0, 50))
        self.delete_project.setFont(font7)
        self.delete_project.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"	color:grey;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"project/x(1)-bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_project.setIcon(icon10)
        self.delete_project.setIconSize(QSize(20, 20))
        self.project_settings = QPushButton(self.frame_16)
        self.project_settings.setObjectName(u"project_settings")
        self.project_settings.setGeometry(QRect(210, 430, 71, 50))
        self.project_settings.setMinimumSize(QSize(0, 50))
        self.project_settings.setFont(font7)
        self.project_settings.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"	color:grey;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"project/minus-bold.png", QSize(), QIcon.Normal, QIcon.Off)
        self.project_settings.setIcon(icon11)
        self.project_settings.setIconSize(QSize(20, 20))
        self.projects_tasklist = QListWidget(self.frame_16)
        self.projects_tasklist.setObjectName(u"projects_tasklist")
        self.projects_tasklist.setGeometry(QRect(110, 120, 256, 192))
        self.projects_tasklist.setStyleSheet(u"border:none;\n"
"color:black;\n"
"background-color: white;\n"
"")
        self.addnew_task_btn = QPushButton(self.frame_16)
        self.addnew_task_btn.setObjectName(u"addnew_task_btn")
        self.addnew_task_btn.setGeometry(QRect(210, 380, 81, 50))
        self.addnew_task_btn.setMinimumSize(QSize(0, 50))
        self.addnew_task_btn.setFont(font7)
        self.addnew_task_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:0px solid;\n"
"	color:grey;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        self.addnew_task_btn.setIcon(icon7)
        self.addnew_task_btn.setIconSize(QSize(20, 20))
        self.addnew_task_btn.setFlat(False)

        self.horizontalLayout_17.addWidget(self.frame_16)

        self.frame = QFrame(self.frame_8)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 100, 0, 150)
        self.tasks_heading_4 = QLabel(self.frame)
        self.tasks_heading_4.setObjectName(u"tasks_heading_4")
        self.tasks_heading_4.setMinimumSize(QSize(0, 70))
        self.tasks_heading_4.setFont(font4)
        self.tasks_heading_4.setStyleSheet(u"color: black;")
        self.tasks_heading_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.tasks_heading_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.timer4 = QLabel(self.frame)
        self.timer4.setObjectName(u"timer4")
        self.timer4.setFont(font5)
        self.timer4.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_10.addWidget(self.timer4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.start_button_2 = QPushButton(self.frame)
        self.start_button_2.setObjectName(u"start_button_2")
        self.start_button_2.setMinimumSize(QSize(0, 50))
        self.start_button_2.setFont(font6)
        self.start_button_2.setStyleSheet(u"QPushButton {\n"
"	background-color:#F2F2F7;\n"
"	color:grey;\n"
"	border:2px solid #F2F2F7;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"	border-radius: 20px;\n"
"}\n"
"")
        self.start_button_2.setIcon(icon6)

        self.verticalLayout_10.addWidget(self.start_button_2, 0, Qt.AlignHCenter)
        self.horizontalLayout_17.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.current_project)
        self.current_task = QWidget()
        self.current_task.setObjectName(u"current_task")
        self.verticalLayout_14 = QVBoxLayout(self.current_task)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.current_task)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.task_name_solo = QLabel(self.frame_2)
        self.task_name_solo.setObjectName(u"task_name_solo")
        self.task_name_solo.setFont(font10)
        self.task_name_solo.setStyleSheet(u"")
        self.task_name_solo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.task_name_solo)
        self.verticalLayout_14.addWidget(self.frame_2)

        self.task_project_name = QLabel(self.current_task)
        self.task_project_name.setObjectName(u"task_project_name")
        self.task_project_name.setMaximumSize(QSize(16777215, 40))
        font16 = QFont()
        font16.setPointSize(15)
        font16.setUnderline(True)
        self.task_project_name.setFont(font16)
        self.task_project_name.setStyleSheet(u"color: #8DDB81; ")
        self.task_project_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.task_project_name)

        self.task_description_solo = QLabel(self.current_task)
        self.task_description_solo.setObjectName(u"task_description_solo")
        self.task_description_solo.setFont(font12)
        self.task_description_solo.setStyleSheet(u"color:black;")
        self.task_description_solo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.task_description_solo)

        self.frame_3 = QFrame(self.current_task)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 90))
        self.frame_3.setStyleSheet(u"color: white;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 30))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"color: black;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_5)

        self.task_status = QLabel(self.frame_4)
        self.task_status.setObjectName(u"task_status")
        self.task_status.setStyleSheet(u"color: black;")
        self.task_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.task_status)
        self.verticalLayout_15.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 30))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.task_deadline = QLabel(self.frame_6)
        self.task_deadline.setObjectName(u"task_deadline")
        self.task_deadline.setStyleSheet(u"color: black;")
        self.task_deadline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.task_deadline)
        self.verticalLayout_15.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: black;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.task_priority = QLabel(self.frame_5)
        self.task_priority.setObjectName(u"task_priority")
        self.task_priority.setStyleSheet(u"color: black;")
        self.task_priority.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.task_priority)
        self.verticalLayout_15.addWidget(self.frame_5)
        self.verticalLayout_14.addWidget(self.frame_3)

        self.mark_task_completed = QPushButton(self.current_task)
        self.mark_task_completed.setObjectName(u"mark_task_completed")
        self.mark_task_completed.setMinimumSize(QSize(0, 30))
        self.mark_task_completed.setMaximumSize(QSize(16777215, 50))
        self.mark_task_completed.setFont(font9)
        self.mark_task_completed.setStyleSheet(u"QPushButton {\n"
"	color: #8DDB81;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        self.mark_task_completed.setIcon(icon8)
        self.mark_task_completed.setIconSize(QSize(20, 20))

        self.verticalLayout_14.addWidget(self.mark_task_completed)

        self.delete_task = QPushButton(self.current_task)
        self.delete_task.setObjectName(u"delete_task")
        self.delete_task.setMinimumSize(QSize(0, 30))
        self.delete_task.setFont(font9)
        self.delete_task.setStyleSheet(u"QPushButton {\n"
"	color: red;  \n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: grey;\n"
"	color:black;\n"
"}\n"
"")
        self.delete_task.setIcon(icon9)
        self.delete_task.setIconSize(QSize(20, 20))

        self.verticalLayout_14.addWidget(self.delete_task)

        self.stackedWidget.addWidget(self.current_task)

        self.horizontalLayout_12.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lightning", None))
        self.Btn_Toggle.setText("")
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"Lightning.", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home     ", None))
        self.project_btn.setText(QCoreApplication.translate("MainWindow", u"Projects  ", None))
        self.tasks_btn.setText(QCoreApplication.translate("MainWindow", u"Tasks      ", None))
        self.analytics_btn.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.label_2.setText("")
        self.tasks_heading_8.setText(QCoreApplication.translate("MainWindow", u"Today.", None))
        self.pushButton_4.setText("")
        self.label_3.setText("")
        self.tasks_heading_9.setText(QCoreApplication.translate("MainWindow", u"Focus Sprint.", None))
        self.timer1.setText(QCoreApplication.translate("MainWindow", u"25:00", None))
        self.start_button_4.setText(QCoreApplication.translate("MainWindow", u"Start.", None))
        self.addnew_project_btn.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.tasks_heading_5.setText(QCoreApplication.translate("MainWindow", u"All Projects.", None))
        self.pushButton_3.setText("")
        self.label_4.setText("")
        self.tasks_heading_6.setText(QCoreApplication.translate("MainWindow", u"Focus Sprint.", None))
        self.timer2.setText(QCoreApplication.translate("MainWindow", u"25:00", None))
        self.start_button_3.setText(QCoreApplication.translate("MainWindow", u"Start.", None))
        self.tasks_heading.setText(QCoreApplication.translate("MainWindow", u"All Tasks.", None))
        self.pushButton.setText("")
        self.label_21.setText("")
        self.tasks_heading_2.setText(QCoreApplication.translate("MainWindow", u"Focus Sprint.", None))
        self.timer3.setText(QCoreApplication.translate("MainWindow", u"25:00", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start.", None))
        self.analytics_heading.setText(QCoreApplication.translate("MainWindow", u"Analytics.", None))
        self.arrow.setText("")
        self.new_task_heading.setText(QCoreApplication.translate("MainWindow", u"    New Task.", None))
        self.change_task_name.setText("")
        self.change_task_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.dframe_label.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.task_datetime.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd-MM-yyyy hh:mm", None))
        self.pframe_label.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.save_task_change.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.cancel_task_change.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.new_project_heading.setText(QCoreApplication.translate("MainWindow", u"    New Project.", None))
        self.change_project_name.setText("")
        self.change_project_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.save_project_change.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.cancel_project_change.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.edit_project_heading.setText(QCoreApplication.translate("MainWindow", u"     Edit Project.", None))
        self.edit_project_name.setText("")
        self.edit_project_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.save_project_edit.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.cancel_project_edit.setText(QCoreApplication.translate("MainWindow", u"Cancel Edit", None))
        self.project_name_main.setText(QCoreApplication.translate("MainWindow", u"*Project Name*", None))
        self.delete_project.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.project_settings.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.addnew_task_btn.setText(QCoreApplication.translate("MainWindow", u"New ", None))
        self.tasks_heading_4.setText(QCoreApplication.translate("MainWindow", u"Focus Sprint.", None))
        self.timer4.setText(QCoreApplication.translate("MainWindow", u"25:00", None))
        self.start_button_2.setText(QCoreApplication.translate("MainWindow", u"Start.", None))
        self.task_name_solo.setText(QCoreApplication.translate("MainWindow", u"   Task Name.", None))
        self.task_project_name.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.task_description_solo.setText(QCoreApplication.translate("MainWindow", u"Task Description", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.task_status.setText(QCoreApplication.translate("MainWindow", u"*enter status*", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Deadline", None))
        self.task_deadline.setText(QCoreApplication.translate("MainWindow", u"*enter deadline*", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.task_priority.setText(QCoreApplication.translate("MainWindow", u"*enter priority*", None))
        self.mark_task_completed.setText(QCoreApplication.translate("MainWindow", u"Mark as completed", None))
        self.delete_task.setText(QCoreApplication.translate("MainWindow", u"Delete Task", None))

mycon = mys.connect(user = 'root', host = 'localhost', passwd = 'capt')
mycur = mycon.cursor()
mycur.execute('create database if not exists lpapp')
mycur.execute('use lpapp')
mycur.execute('create table if not exists projects(pno int primary key, pname varchar(100), pdes varchar(16000), doc datetime)')
mycur.execute('create table if not exists tasks(tno int primary key, pno int, tname varchar(100), tdes varchar(16000), priority varchar(60), status varchar(60), dos datetime, doc datetime)')
mycon.commit()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('icons/flash.png'))
        # Setting default page and Project Number for MySQL Debugging
        self.current_pno = 1
        self.cur_page = 'home'
        # Setting timer
        self.timerstate = 'Start.'
        self.timer = QTimer()
        self.timer.setInterval(1500)
        self.timer.timeout.connect(lambda: self.counter())
        self.c = 1500
        # Combobox options
        self.ui.priority_task_combo.addItems(['Urgent', 'Low'])

        # Default view for Home Page
        mycur.execute(f'select tname from tasks where date(dos) = curdate() and status = "TODO"')
        tasks = mycur.fetchall()
        for elements in tasks:
            if elements[0]: 
                self.ui.home_content.addItem(elements[0])
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.home_content.itemDoubleClicked.connect(self.open_task)

        # Status bar message  
        self.statusBar().showMessage("An App by Pavan, Siddharth and Nandu")

        # Set default text for Add Project and Add Tasks
        self.ui.change_project_name.setText('Project Name')
        self.ui.new_project_desc.setText('Project Description')
        self.ui.change_task_name.setText('Task Name')
        self.ui.new_task_desc.setText('Task Description')
        self.ui.change_task_name.setText('Task Name')
        self.ui.new_task_desc.setText('Task Description')

        # TOGGLE/BURGUER MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))

        # Opening Main Menu Pages
        self.ui.home_btn.clicked.connect(lambda: self.todays_tasks()) # Home Page
        self.ui.project_btn.clicked.connect(lambda: self.all_projects()) # Projects Page
        self.ui.tasks_btn.clicked.connect(lambda: self.all_tasks()) # Tasks Page
        self.ui.analytics_btn.clicked.connect(lambda: self.analytics_page()) # Analytics Page
        
        # For Adding New Projects and Tasks
        self.ui.addnew_project_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.addnew_project))
        self.ui.addnew_task_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.addnew_task))

        # Save Changes
        self.ui.save_task_change.clicked.connect(lambda: self.task_save())
        self.ui.save_project_change.clicked.connect(lambda: self.project_save())

        # Cancel Changes
        self.ui.cancel_project_edit.clicked.connect(lambda: self.all_projects())
        self.ui.cancel_task_change.clicked.connect(lambda: self.task_cancel())
        self.ui.cancel_project_change.clicked.connect(lambda: self.project_cancel())

        # To Edit Existing Project
        self.ui.save_project_edit.clicked.connect(lambda: self.project_save_settings())

        # Marking Task as Completed
        self.ui.mark_task_completed.clicked.connect(lambda: self.task_completed())

        # Deleting Projects and Tasks
        self.ui.delete_project.clicked.connect(lambda: self.del_proj())
        self.ui.delete_task.clicked.connect(lambda: self.del_task())

        # Timer Buttons
        self.ui.start_button.clicked.connect(lambda: self.timer_fun())
        self.ui.start_button_2.clicked.connect(lambda: self.timer_fun())
        self.ui.start_button_3.clicked.connect(lambda: self.timer_fun())
        self.ui.start_button_4.clicked.connect(lambda: self.timer_fun())

        # Show Main Window
        self.show()

    def timer_fun(self):
        if self.timerstate == "Start.":
            self.timer.start()
            self.timerstate = "Stop."
        elif self.timerstate == "Stop.":
            self.timer.stop()
            self.c = 1500
            self.timerstate = "Start."
            self.ui.timer1.setText("25:00")
            self.ui.timer2.setText("25:00")     
            self.ui.timer3.setText("25:00")
            self.ui.timer4.setText("25:00")
        self.ui.start_button.setText(self.timerstate)
        self.ui.start_button_2.setText(self.timerstate)
        self.ui.start_button_3.setText(self.timerstate)
        self.ui.start_button_4.setText(self.timerstate)

    def counter(self):
        self.c -= 1
        if self.c == 0:
            self.timer_fun()
        self.ui.timer1.setText(f'{self.c//60}:{self.c%60}')
        self.ui.timer2.setText(f'{self.c//60}:{self.c%60}')
        self.ui.timer3.setText(f'{self.c//60}:{self.c%60}')
        self.ui.timer4.setText(f'{self.c//60}:{self.c%60}')

    def todays_tasks(self):
        self.ui.home_content.clear()
        self.cur_page = 'home'
        mycur.execute(f'select tname from tasks where date(dos) = curdate() and status = "TODO"')
        tasks = mycur.fetchall()
        for elements in tasks:
            if elements[0]: 
                self.ui.home_content.addItem(elements[0])
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.home_content.itemDoubleClicked.connect(self.open_task)

    def all_projects(self):
        self.ui.projects_list.clear()
        mycur.execute('select * from projects')
        projects = mycur.fetchall()
        for elements in projects:
            if elements[1]: 
                self.ui.projects_list.addItem(elements[1])
        self.ui.stackedWidget.setCurrentWidget(self.ui.projects_page)
        self.ui.projects_list.itemDoubleClicked.connect(self.open_project)

    def open_project(self): 
        project_name = str(self.ui.projects_list.currentItem().text())
        mycur.execute(f"select * from projects where pname = '{project_name}'")
        project_details = mycur.fetchone()
        self.current_pno = project_details[0]
        self.ui.project_name_main.setText(project_details[1])
        self.ui.projects_tasklist.clear()
        mycur.execute(f'select tname, projects.pno from tasks, projects where tasks.pno = projects.pno and pname = "{project_name}"')
        tasks = mycur.fetchall()
        for elements in tasks:
            if elements[0]: 
                self.ui.projects_tasklist.addItem(elements[0])
        self.ui.stackedWidget.setCurrentWidget(self.ui.current_project)
        self.cur_page = 'proj'
        self.ui.projects_tasklist.itemDoubleClicked.connect(self.open_task)
        self.ui.project_settings.clicked.connect(lambda: self.project_settings())

    def project_save(self):
        mycur.execute('select max(pno) from projects')
        max_pno = mycur.fetchone()[0]
        if max_pno != None:
            current_pno = int(max_pno) + 1
        else:
            current_pno = 1
        project_name = self.ui.change_project_name.text()
        project_desc = self.ui.new_project_desc.toPlainText()
        if project_name.strip() not in ('', 'Project Name'):
            mycur.execute(f'insert into projects values({current_pno}, "{project_name}", "{project_desc}", sysdate())')
            mycon.commit()
        self.ui.change_project_name.setText('Project Name')
        self.ui.new_project_desc.setText('Project Description')
        self.all_projects()

    def project_cancel(self):
        self.all_projects()
        self.ui.change_project_name.setText('Project Name')
        self.ui.new_project_desc.setText('Project Description')

    def project_settings(self):
        project_name = str(self.ui.projects_list.currentItem().text())
        mycur.execute(f"select * from projects where pname = '{project_name}'")
        project_details = mycur.fetchone()
        self.current_pno = project_details[0]
        self.ui.edit_project_name.setText(project_details[1])
        self.ui.edit_project_desc.setText(project_details[2])
        self.ui.stackedWidget.setCurrentWidget(self.ui.edit_project)
    
    def project_save_settings(self):
        mycur.execute(f'update projects set pname = "{self.ui.edit_project_name.text()}", pdes = "{self.ui.edit_project_desc.toPlainText()}" where pno = {self.current_pno}')
        self.ui.edit_project_name.setText('Project Name')
        self.ui.edit_project_desc.setText('Project Description')
        mycon.commit()
        self.all_projects()

    def del_proj(self):
        mycur.execute(f'delete from projects where pname = "{self.ui.project_name_main.text()}"')
        mycon.commit()
        self.all_projects()

    def del_task(self):
        mycur.execute(f'select tno from tasks, projects where tasks.pno = projects.pno and tname = "{self.ui.task_name_solo.text()}" and pname = "{self.ui.task_project_name.text()}" and tdes = "{self.ui.task_description_solo.text()}"')
        cur_tno = mycur.fetchone()[0]
        mycur.execute(f'delete from tasks where tno = {cur_tno}')
        mycon.commit()
        self.all_tasks()

    def all_tasks(self):
        self.ui.tasks_list.clear()
        mycur.execute(f'select tname from tasks')
        tasks = mycur.fetchall()
        for elements in tasks:
            if elements[0]: 
                self.ui.tasks_list.addItem(elements[0])
        self.ui.stackedWidget.setCurrentWidget(self.ui.tasks_page)
        self.cur_page = 'task'
        self.ui.tasks_list.itemDoubleClicked.connect(self.open_task)

    def open_task(self):
        if self.cur_page == 'home': 
            task_name = str(self.ui.home_content.currentItem().text())
        elif self.cur_page == 'proj':
            task_name = str(self.ui.projects_tasklist.currentItem().text())
        elif self.cur_page == 'task':
            task_name = str(self.ui.tasks_list.currentItem().text())
        elif self.cur_page == 'analy':
            task_name = str(self.ui.analytics_tasks.currentItem().text())
        mycur.execute(f'select tname, pname, projects.pno, tdes, status, priority, dos from tasks, projects where tasks.pno = projects.pno and tname = "{task_name}"')
        tasks_details = mycur.fetchone()
        if tasks_details[4] == 'Completed':
            self.ui.mark_task_completed.hide()
        else:
            self.ui.mark_task_completed.show()
        self.current_pno = tasks_details[2]
        self.ui.task_name_solo.setText(str(tasks_details[0]))
        self.ui.task_project_name.setText(str(tasks_details[1]))
        self.ui.task_description_solo.setText(str(tasks_details[3]))
        self.ui.task_status.setText(tasks_details[4])
        self.ui.task_priority.setText(tasks_details[5])
        self.ui.task_deadline.setText(str(tasks_details[6]))
        self.ui.stackedWidget.setCurrentWidget(self.ui.current_task)

    def task_save(self):
        self.ui.new_task_heading.setText('Add New Task')
        mycur.execute('select max(tno) from tasks')
        latest = mycur.fetchone()
        current_tno = 1 if latest[0] == None else int(latest[0]) + 1
        task_name = self.ui.change_task_name.text()
        task_desc = self.ui.new_task_desc.toPlainText()
        priority = self.ui.priority_task_combo.currentText()
        temp_doc = self.ui.task_datetime.dateTime()
        doc = temp_doc.toString(Qt.ISODate)
        doc = f'{doc[:10]}-{doc[11:13]}-{doc[14:16]}-{doc[17:19]}'
        if task_name not in ('', 'Task Name'):
            mycur.execute(f'insert into tasks values({current_tno}, {self.current_pno}, "{task_name}", "{task_desc}", "{priority}", "TODO", "{doc}", sysdate())')
            mycon.commit()
        self.ui.change_task_name.setText('Task Name')
        self.ui.new_task_desc.setText('Task Description')
        self.all_tasks()
    
    def task_cancel(self):
        self.all_tasks()
        self.ui.change_task_name.setText('Task Name')
        self.ui.new_task_desc.setText('Task Description')

    def task_completed(self):
        mycur.execute(f'select tno from tasks, projects where tasks.pno = projects.pno and pname = "{self.ui.task_project_name.text()}" and tname = "{self.ui.task_name_solo.text()}" and tdes = "{self.ui.task_description_solo.text()}"')
        tno = mycur.fetchone()[0]
        mycur.execute(f'update tasks set status = "Completed" where tno = "{tno}"')
        mycon.commit()
        self.all_tasks()

    def analytics_page(self):
        self.cur_page = 'analy'
        self.ui.home_content.clear()
        selected_date = self.ui.analytics_calendar.selectedDate().toString(Qt.ISODate)
        selected_date = f'{selected_date[:10]}-{selected_date[11:13]}-{selected_date[14:16]}-{selected_date[17:19]}'
        mycur.execute(f"select tname from tasks where date(dos) = '{selected_date}'")
        tasks = mycur.fetchall()
        self.ui.analytics_tasks.clear()
        for elements in tasks:
            if elements[0]: 
                self.ui.analytics_tasks.addItem(elements[0])
        self.ui.analytics_calendar.selectionChanged.connect(self.grab_date)
        self.ui.stackedWidget.setCurrentWidget(self.ui.analytics_page)
        self.ui.analytics_tasks.itemDoubleClicked.connect(self.open_task)

    def grab_date(self):
        selected_date = self.ui.analytics_calendar.selectedDate().toString(Qt.ISODate)
        selected_date = f'{selected_date[:10]}-{selected_date[11:13]}-{selected_date[14:16]}-{selected_date[17:19]}'
        mycur.execute(f"select tname from tasks where date(dos) = '{selected_date}'")
        tasks = mycur.fetchall()
        self.ui.analytics_tasks.clear()
        for elements in tasks:
            if elements[0]: 
                self.ui.analytics_tasks.addItem(elements[0])

# For the animation and functioning of the Toggle Menu Button
class UIFunctions(MainWindow):
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 0
            # SET MAX WIDTH
            if width in range(90):
                widthExtended = maxExtend
            else:
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
