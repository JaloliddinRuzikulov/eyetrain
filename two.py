from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # this will hide the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # setting  the geometry of window
        self.setGeometry(100, 100, 400, 300)
        self.showFullScreen()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setPen(QPen(Qt.darkRed, 6))
        qp.drawRect(self.rect())

        qp.setOpacity(0.51)
        qp.setPen(Qt.NoPen)
        qp.setBrush(self.palette().window())
        qp.drawRect(self.rect())


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
window.show()
# start the app
sys.exit(App.exec())