from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from MainWindow import Ui_MainWindow
from RequestsSystem import RequestsSystem
import os

EPSILON = 0.001


class MiniSearch(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.requestsSystem = RequestsSystem()
        self.setFixedSize(800, 600)
        self.showMapbtn.clicked.connect(lambda: self.showMap())
        self.mapFile = "map.png"
        self.currentViewMap = "map"

    def loadMap(self):
        with open(self.mapFile, "wb") as file:
            self.respone = self.requestsSystem.getMap(
                [self.currentLon, self.currentLat], self.currentScale,
                self.currentViewMap, self.currentMark)
            if self.respone.ok:
                file.write(self.respone.content)
            else:
                self.labelError.setText("Ошибка запроса")
        self.pixmap = QPixmap(self.mapFile)
        self.photo.setPixmap(self.pixmap)

    def updateData(self, mark=""):
        self.currentLon = self.lon.text()
        self.currentLat = self.lat.text()
        self.currentScale = self.scale.text()
        self.currentMark = mark

    def clearErrors(self):
        self.labelErrorData.setText("")
        self.labelError.setText("")

    def showMap(self, mark=""):
        # валидаторы
        self.updateData()
        if not (self.lon.text() and self.lat.text() and self.scale.text()) != "":
            self.labelErrorData.setText("Введите данные")
        else:
            self.clearErrors()
            self.loadMap()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if 0 <= int(self.scale.text()) < 17:
                self.scale.setText(str(int(self.currentScale) + 1))
                self.showMap()
        if event.key() == Qt.Key_PageDown:
            if 0 <= int(self.scale.text()) <= 17:
                self.scale.setText(str(int(self.currentScale) - 1))
                self.showMap()
        if event.key() == Qt.Key_Up:
            if abs(float(self.currentLon)) <= 180:
                self.lat.setText(str(round(float(self.currentLat) + EPSILON, 6)))
                self.showMap()
        if event.key() == Qt.Key_Down:
            if abs(float(self.currentLon)) <= 180:
                self.lat.setText(str(round(float(self.currentLat) - EPSILON, 6)))
                self.showMap()
        if event.key() == Qt.Key_Left:
            if abs(float(self.currentLon)) <= 180:
                self.lon.setText(str(round(float(self.currentLon) - EPSILON, 6)))
                self.showMap()
        if event.key() == Qt.Key_Right:
            if abs(float(self.currentLon)) <= 180:
                self.lon.setText(str(round(float(self.currentLon) + EPSILON, 6)))
                self.showMap()

    def closeEvent(self, event):
        if os.path.exists("map.png"):
            os.remove(self.mapFile)
