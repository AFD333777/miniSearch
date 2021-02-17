from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow
from RequestsSystem import RequestsSystem
import os


class MiniSearch(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.requestsSystem = RequestsSystem()
        self.setFixedSize(800, 600)
        self.showMapbtn.clicked.connect(lambda: self.showMap(
            [self.lon.text(), self.lat.text()], self.scale.text(), "map"))

    def showMap(self, coords, scale, viewMap="map", mark=""):
        # валидаторы
        if not (self.lon.text() and self.lat.text() and self.scale.text()) != "":
            self.labelErrorData.setText("Введите данные")
        else:
            self.currentCoords = coords
            self.currentScale = scale
            self.currentViewMap = viewMap
            self.currentMark = mark
            self.labelErrorData.setText("")
            self.labelError.setText("")
            self.mapFile = "map.png"
            with open(self.mapFile, "wb") as file:
                self.respone = self.requestsSystem.getMap(
                    self.currentCoords, self.currentScale, self.currentViewMap, self.currentMark)
                if self.respone.ok:
                    file.write(self.respone.content)
                else:
                    self.labelError.setText("Ошибка запроса")
            self.pixmap = QPixmap(self.mapFile)
            self.photo.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            if 0 <= int(self.scale.text()) < 17:
                self.currentScale = str(int(self.currentScale) + 1)
                self.scale.setText(self.currentScale)
                self.showMap(self.currentCoords, self.currentScale, self.currentViewMap, self.currentMark)
        if event.key() == Qt.Key_PageDown:
            if 0 <= int(self.scale.text()) <= 17:
                self.currentScale = str(int(self.currentScale) - 1)
                self.scale.setText(self.currentScale)
                self.showMap(self.currentCoords, self.currentScale, self.currentViewMap, self.currentMark)

    def closeEvent(self, event):
        os.remove(self.mapFile)
