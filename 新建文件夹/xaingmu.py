import sys,time
from PyQt5.QtWidgets import QApplication,QAction,QMessageBox,QWidget,QMainWindow,QTableWidgetItem
from PyQt5.QtGui import QColor
from dier import Ui_MainWindow
import random
from PyQt5.QtCore import  pyqtSignal
from PyQt5 import QtWidgets,QtCore
import pymysql as a
from yx  import *
from PyQt5.QtCore import Qt

 
ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','0','1','2','3','4','5','6','7','8','9']

class myform1(QMainWindow,Ui_MainWindow):
    signal=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.jizhu=1
        self.i=1
        self.db = a.connect(host='localhost',user='root',\
            password='123456',database='jiemain',charset='utf8')
        self.cur=self.db.cursor()   
        self.cur.execute("select * from jizhu;")
        s=self.cur.fetchall()
        for i in s:
            if i[0]==1:
                self.lineEdit1.setText("%s"%i[1])
                self.lineEdit2.setText("***************")
                self.cur.execute("select uname,upassword from youhu;")
                s1=self.cur.fetchall()
                for m in s1:
                    if m[0]==i[1]:
                        self.i=m[1]
        self.b1.clicked.connect(self.ok)
        self.b2.clicked.connect(self.ok1)
        self.checkBox.clicked.connect(self.jizhu1)
        self.show()

        self.setStyleSheet('QMainWindow{background-color:green}')
        bar=QMainWindow.menuBar(self)
        color=bar.addMenu('更换颜色')
        red_action=QAction('red',self,triggered=self.red_evet)
        yellow_action=QAction('yellow',self,triggered=self.yellow_evet)
        green_action=QAction('green',self,triggered=self.green_evet)
        color.addAction(red_action)
        color.addAction(yellow_action)
        color.addAction(green_action)

    def jizhu1(self):
        self.jizhu+=1
        if self.jizhu%2==0:
            return 110
        else:
            return 120

    def red_evet(self):
        r=QColor(255,0,0)
        self.setStyleSheet('QMainWindow{background-color:%s}'%r.name())
    def yellow_evet(self):
        r=QColor(255,255,0)
        self.setStyleSheet('QMainWindow{background-color:%s}'%r.name())
    def green_evet(self):
        r=QColor(0,128,0)
        self.setStyleSheet('QMainWindow{background-color:%s}'%r.name())
    def ok(self):
        self.db = a.connect(host='localhost',user='root',\
            password='123456',database='jiemain',charset='utf8')
        self.cur=self.db.cursor()   
        self.cur.execute("select uname,upassword from youhu;")
        s=self.cur.fetchall()

        for i in s:
            if i[0]==self.lineEdit1.text() and i[1]==self.i:
                QMessageBox.warning(self,'成功','登录成功')
                self.close()
                diyi()
                if self.jizhu1()==120:
                    self.cur.execute("insert into jizhu value ('1','%s');"%i[0])
                    self.db.commit()
                    self.db.close()
                else:
                    self.cur.execute("delete from jizhu where id=1;")
                    self.db.commit()
                    self.db.close()
                return
            if i[0]==self.lineEdit1.text() and i[1]==self.lineEdit2.text():
                QMessageBox.warning(self,'成功','登录成功')
                self.signal.emit()
                self.close()
                if self.jizhu1()==120:
                    self.cur.execute("insert into jizhu value ('1','%s');"%i[0])
                    self.db.commit()
                    self.db.close()
                else:
                    self.cur.execute("delete from jizhu where id =1;")
                    self.db.commit()
                    self.db.close()
                returnaaa
        QMessageBox.warning(self,'错误','你输入的账号和密码不匹配，请重新输入')
                

                
    def ok1(self):
            self.close()





class zi(QWidget):
    signal=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setObjectName("注册")
        self.resize(500, 333)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 800, 600))
        self.textBrowser.setStyleSheet("background-image:url(C:/Users/Administrator/Desktop/0123.jpg);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        #无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 170, 90, 12))
        self.label_7.setObjectName("label_7")
        self.l3 = QtWidgets.QLineEdit(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(230, 160, 171, 20))
        self.l3.setObjectName("l3")
        #设置密码不可见
        self.l3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.l1 = QtWidgets.QLineEdit(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(230, 50, 171, 20))
        self.l1.setObjectName("l1")
        self.l2 = QtWidgets.QLineEdit(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(230, 110, 171, 20))
        self.l2.setObjectName("l2")
        #设置密码不可见
        self.l2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(110, 280, 75, 23))
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(290, 280, 75, 23))
        self.b4.setObjectName("b4")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(375, 205, 70, 30))
        self.b6.setObjectName("b6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(405, 20, 50, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(455,20, 50, 23))
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.showMinimized)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 205, 91, 31))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)    
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("selection-background-color:black;")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 215, 111, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.retranslateUi(QWidget)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, QWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("QWidget", "账号"))
        self.label_2.setText(_translate("QWidget", "密码"))
        self.label_7.setText(_translate("QWidget", "请再次输入密码"))
        self.b3.setText(_translate("QWidget", "重置"))
        self.b4.setText(_translate("QWidget", "提交"))
        self.b6.setText(_translate("QWidget", "获取验证码"))
        self.label_3.setText(_translate("QWidget", "验证码"))
        self.b7.setText(_translate("MainWindow", "X"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))

        self.b3.clicked.connect(self.clear)
        self.b4.clicked.connect(self.tijiao)
        self.b6.clicked.connect(self.sj)
        s=random.sample(ab,6)
        self.data=''
        for i in s:
            self.data += i+' '
        d=QTableWidgetItem(str(self.data))
        self.tableWidget.setItem(0,0,d)
    def sj(self):
        s=random.sample(ab,6)
        self.data=''
        for i in s:
            self.data += i+' '
        d=QTableWidgetItem(str(self.data))
        self.tableWidget.setItem(0,0,d)
    def clear(self):
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.lineEdit.clear()
    def tijiao(self):
        self.db = a.connect(host='localhost',user='root',\
            password='123456',database='jiemain',charset='utf8')
        self.cur=self.db.cursor()
        uname=self.l1.text()
        upwd=self.l2.text()
        uzpwd=self.l3.text()
        if upwd==uzpwd:
            pass
        else:
            QMessageBox.warning(self,'提示','两次密码输入不一致去，请重新输入')
            return
        if uname=='' and upwd=='':
            QMessageBox.warning(self,'提示','请填入账号和密码')
            return
        for i in uname:
            if i==' ':
                QMessageBox.warning(self,'提示','账号内容不许存在空格或为空')
                return
        for i in upwd:
            if i ==' ':
                QMessageBox.warning(self,'提示','密码内容不许存在空格')
                return
            
        self.cur.execute("select uname from youhu;")
        s=self.cur.fetchall()
        for i  in s:
            if i[0]==uname:
                QMessageBox.warning(self,'提示','用户已存在')
                return
        p = ''
        for i in self.data:
            if i!=' ':
                p+=i           
        if self.lineEdit.text()==p:
            if len(upwd)>=6:
                QMessageBox.warning(self,'成功','恭喜你 注册成功')
            else:
                QMessageBox.warning(self,'提示','密码不能小于六位数，请重新输入')
                return
        else:
            QMessageBox.warning(self,'提示','请确认验证码')
            return
        self.cur.execute("insert into youhu values ('%s','%s');"% (uname,upwd))
        self.db.commit()
        self.cur.close()
        self.db.close()
        self.close()
        self.signal.emit()



if __name__=='__main__':
    app=QApplication(sys.argv)
    w=myform1()
    s=zi()
    s.signal.connect(w.show)
    w.b2.clicked.connect(s.show)
    app.exec_()