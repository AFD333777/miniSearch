from Draw import MiniSearch
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniSearch()
    ex.show()
    sys.exit(app.exec_())
