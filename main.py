from PyQt5.QtWidgets import QApplication
from qt import Stats

if __name__ == '__main__':
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()
