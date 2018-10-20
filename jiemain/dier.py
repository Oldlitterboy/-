# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dier.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("登录")
        MainWindow.resize(641, 360)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 641, 301))
        self.textBrowser.setStyleSheet("background-image:url(C:/Users/Administrator/Desktop/12345.jpg);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 110, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(270, 40, 163, 20))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(270, 110, 163, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(170, 165, 71, 16))
        self.checkBox.setObjectName("jizhu")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(170, 230, 100, 23))
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(340, 230, 100, 23))
        self.b2.setObjectName("b2")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(380, 160, 55, 23))
        self.label5.setOpenExternalLinks(True)
        self.label5.setObjectName("label5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.gupTransparency = QtWidgets.QGroupBox(self)
        self.gupTransparency.setGeometry(QtCore.QRect(465, 320, 171, 51))
        self.hsdTransparency = QtWidgets.QSlider(self.gupTransparency)
        self.hsdTransparency.setGeometry(QtCore.QRect(10, 20, 151, 19))
        self.hsdTransparency.setMinimum(10)
        self.hsdTransparency.setMaximum(100)
        self.hsdTransparency.setValue(100)
        self.hsdTransparency.setOrientation(QtCore.Qt.Horizontal)
        self.hsdTransparency.setObjectName("hsdTransparency")
        self.hsdTransparency.valueChanged.connect(self.ChangeTransparency)
    def ChangeTransparency(self, e):
        self.setWindowOpacity(self.hsdTransparency.value() / 100)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "账号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.b1.setText(_translate("MainWindow", "登录"))
        self.b2.setText(_translate("MainWindow", "注册"))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.label5.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"www.baidu.com\"><span style=\" text-decoration: underline; color:#0000ff;\">忘记密码</span></a></p></body></html>"))

