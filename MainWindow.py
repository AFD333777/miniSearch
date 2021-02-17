# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLon = QtWidgets.QLabel(self.centralwidget)
        self.labelLon.setGeometry(QtCore.QRect(20, 20, 51, 16))
        self.labelLon.setObjectName("labelLon")
        self.labelLat = QtWidgets.QLabel(self.centralwidget)
        self.labelLat.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.labelLat.setObjectName("labelLat")
        self.labelScale = QtWidgets.QLabel(self.centralwidget)
        self.labelScale.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.labelScale.setObjectName("labelScale")
        self.lon = QtWidgets.QLineEdit(self.centralwidget)
        self.lon.setGeometry(QtCore.QRect(80, 20, 113, 22))
        self.lon.setStyleSheet("")
        self.lon.setObjectName("lon")
        self.lat = QtWidgets.QLineEdit(self.centralwidget)
        self.lat.setGeometry(QtCore.QRect(80, 50, 113, 22))
        self.lat.setObjectName("lat")
        self.scale = QtWidgets.QLineEdit(self.centralwidget)
        self.scale.setGeometry(QtCore.QRect(80, 80, 113, 22))
        self.scale.setObjectName("scale")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(270, 30, 500, 450))
        self.photo.setStyleSheet("border-style:outset;\n"
"    border-width: 2px;\n"
"    border-color: black;")
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.showMapbtn = QtWidgets.QPushButton(self.centralwidget)
        self.showMapbtn.setGeometry(QtCore.QRect(20, 110, 221, 31))
        self.showMapbtn.setStyleSheet("")
        self.showMapbtn.setObjectName("showMapbtn")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(270, 10, 211, 16))
        self.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelErrorData = QtWidgets.QLabel(self.centralwidget)
        self.labelErrorData.setGeometry(QtCore.QRect(10, 0, 211, 16))
        self.labelErrorData.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelErrorData.setText("")
        self.labelErrorData.setObjectName("labelErrorData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "МиниПоисковик"))
        self.labelLon.setText(_translate("MainWindow", "Долгота"))
        self.labelLat.setText(_translate("MainWindow", "Широта"))
        self.labelScale.setText(_translate("MainWindow", "Масштаб "))
        self.lon.setPlaceholderText(_translate("MainWindow", "Введите долготу"))
        self.lat.setPlaceholderText(_translate("MainWindow", "Введите широту"))
        self.scale.setPlaceholderText(_translate("MainWindow", "Введите масштаб"))
        self.showMapbtn.setText(_translate("MainWindow", "Отобразить карту"))