import sys

from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QDesktopWidget


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('eyetrain.ui', self)
        self.button.clicked.connect(self.hide)

    def printvalue(self):
        print(self.lineEdit.text())

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.show()


class LockScreen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('lockscreen.ui', self)
        self.pushButton.clicked.connect(self.hide)

    def center(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # setting  the geometry of window
        self.setGeometry(100, 100, 400, 300)
        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    lock_screen = LockScreen()
    tray_icon = QSystemTrayIcon(QIcon('crying.png'), parent=app)
    # Menu
    menu = QMenu()
    show = menu.addAction('Show')
    show.triggered.connect(demo.show)
    hide = menu.addAction('Hide')
    hide.triggered.connect(demo.hide)
    chiqish = menu.addAction('Exit')
    chiqish.triggered.connect(app.quit)
    tray_icon.setContextMenu(menu)
    tray_icon.show()
    demo.center()
    lock_screen.center()
    sys.exit(app.exec_())
