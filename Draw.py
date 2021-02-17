from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow
from RequestsSystem import RequestsSystem


class MiniSearch(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.requestsSystem = RequestsSystem()
        self.setFixedSize(800, 600)
        self.showMapbtn.clicked.connect(lambda: self.showMap("map", "pmwtm"))

    def showMap(self, viewMap="map", mark=""):
        # валидаторы
        if not (self.lon.text() and self.lat.text() and self.scale.text()) != "":
            self.labelErrorData.setText("Введите данные")
        else:
            self.labelErrorData.setText("")
            self.labelError.setText("")
            self.mapFile = "map.png"
            with open(self.mapFile, "wb") as file:
                self.respone = self.requestsSystem.getMap(
                    [self.lon.text(), self.lat.text()], self.scale.text(), viewMap, mark)
                if self.respone.ok:
                    file.write(self.respone.content)
                else:
                    self.labelError.setText("Ошибка запроса")
            self.pixmap = QPixmap(self.mapFile)
            self.photo.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            print("увеличение карты")
        if event.key() == Qt.Key_PageDown:
            print("уменьшение карты")
