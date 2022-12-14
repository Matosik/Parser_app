from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

import os

class Ui_parser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#FFFFF0;")
        self.centralwidget.setObjectName("centralwidget")
        self.name_app = QtWidgets.QLabel(self.centralwidget)
        self.name_app.setGeometry(QtCore.QRect(-10, -10, 791, 241))
        self.name_app.setStyleSheet("background-color:#9E93CF")
        self.name_app.setText("")
        self.name_app.setObjectName("name_app")
        self.take_request = QtWidgets.QPushButton(self.centralwidget)
        self.take_request.setGeometry(QtCore.QRect(20, 400, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.take_request.setFont(font)
        self.take_request.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.take_request.setStyleSheet("QPushButton{\n"
"    background-color: #FFFFF0;\n"
"    border: 4px solid #9E93CF;\n"
"    border-radius: 35%;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    cursor: closed_hand;\n"
"    background-color: #f5f0ef;\n"
"    border-radius: 40%;\n"
"}\n"
"")
        self.take_request.setObjectName("take_request")
        self.take_folder = QtWidgets.QPushButton(self.centralwidget)
        self.take_folder.setGeometry(QtCore.QRect(560, 400, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.take_folder.setFont(font)
        self.take_folder.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.take_folder.setStyleSheet("QPushButton{\n"
"    background-color: #FFFFF0;\n"
"    border: 4px solid #9E93CF;\n"
"    border-radius: 35%;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"    border-radius: 40%;\n"
"}\n"
"")
        self.take_folder.setObjectName("take_folder")
        self.take_the_path = QtWidgets.QPushButton(self.centralwidget)
        self.take_the_path.setGeometry(QtCore.QRect(290, 400, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.take_the_path.setFont(font)
        self.take_the_path.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.take_the_path.setStyleSheet("QPushButton{\n"
"    background-color: #FFFFF0;\n"
"    border: 4px solid #9E93CF;\n"
"    border-radius: 35%;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"    border-radius: 40%;\n"
"}\n"
"")
        self.take_the_path.setObjectName("take_the_path")
        self.name_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.name_folder.setGeometry(QtCore.QRect(540, 290, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.name_folder.setFont(font)
        self.name_folder.setStyleSheet("background-color: #FFFFF0;\n"
"border: 4px solid #9E93CF;\n"
"border-radius: 10%;\n"
"color:#1e3d59")
        self.name_folder.setAlignment(QtCore.Qt.AlignCenter)
        self.name_folder.setObjectName("name_folder")
        self.full_path = QtWidgets.QLineEdit(self.centralwidget)
        self.full_path.setGeometry(QtCore.QRect(260, 290, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.full_path.setFont(font)
        self.full_path.setStyleSheet("background-color: #FFFFF0;\n"
"border: 4px solid #9E93CF;\n"
"border-radius: 10%;\n"
"color:#1e3d59")
        self.full_path.setAlignment(QtCore.Qt.AlignCenter)
        self.full_path.setObjectName("full_path")
        self.name_reqeust = QtWidgets.QLineEdit(self.centralwidget)
        self.name_reqeust.setGeometry(QtCore.QRect(20, 290, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.name_reqeust.setFont(font)
        self.name_reqeust.setStyleSheet("background-color: #FFFFF0;\n"
"border: 4px solid #9E93CF;\n"
"border-radius: 10%;\n"
"color:#1e3d59")
        self.name_reqeust.setAlignment(QtCore.Qt.AlignCenter)
        self.name_reqeust.setObjectName("name_reqeust")
        self.start_parsing = QtWidgets.QPushButton(self.centralwidget)
        self.start_parsing.setGeometry(QtCore.QRect(270, 560, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.start_parsing.setFont(font)
        self.start_parsing.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.start_parsing.setStyleSheet("QPushButton{\n"
"    background-color: #FFFFF0;\n"
"    border: 4px solid #9E93CF;\n"
"    border-radius: 35%;\n"
"    color:#1e3d59\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #f5f0ef;\n"
"    border-radius: 40%;\n"
"}\n"
"")
        self.start_parsing.setObjectName("start_parsing")
        self.change_amount = QtWidgets.QSlider(self.centralwidget)
        self.change_amount.setGeometry(QtCore.QRect(30, 500, 20, 181))
        self.change_amount.setMinimum(2)
        self.change_amount.setMaximum(1300)
        self.change_amount.setOrientation(QtCore.Qt.Vertical)
        self.change_amount.setTickInterval(50)
        self.change_amount.setObjectName("change_amount")
        self.amount_img = QtWidgets.QLabel(self.centralwidget)
        self.amount_img.setGeometry(QtCore.QRect(80, 550, 141, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.amount_img.setFont(font)
        self.amount_img.setStyleSheet("background-color: #FFFFF0;border: 4px solid #9E93CF;border-radius: 35%;color:#1e3d59")
        self.amount_img.setAlignment(QtCore.Qt.AlignCenter)
        self.amount_img.setObjectName("amount_img")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(320, 60, 141, 151))
        self.logo.setStyleSheet("background-color:#9E93CF")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/logo/????????.png"))
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 0, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#9E93CF")
        self.label.setObjectName("label")
        self.iconBrouser = QtWidgets.QLabel(self.centralwidget)
        self.iconBrouser.setGeometry(QtCore.QRect(100, 50, 151, 151))
        self.iconBrouser.setStyleSheet("background-color:#9E93CF")
        self.iconBrouser.setText("")
        self.iconBrouser.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/logo/??????????????.png"))
        self.iconBrouser.setObjectName("iconBrouser")
        self.iconImg = QtWidgets.QLabel(self.centralwidget)
        self.iconImg.setGeometry(QtCore.QRect(530, 50, 151, 151))
        self.iconImg.setStyleSheet("background-color:#9E93CF")
        self.iconImg.setText("")
        self.iconImg.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/logo/img.png"))
        self.iconImg.setObjectName("iconImg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.take_request.setText(_translate("MainWindow", "?????????????? ????????????"))
        self.take_folder.setText(_translate("MainWindow", "?????????????? ??????????"))
        self.take_the_path.setText(_translate("MainWindow", "?????????????? ????????"))
        self.start_parsing.setText(_translate("MainWindow", "???????????? ??????????????"))
        self.amount_img.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "???????????? ???????????????? ???? ??????????????????"))

