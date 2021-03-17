from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_ui()
        # self.setupUi(self)

    def create_ui(self):
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle("=>[ Image Downloader ]>=")
        self.setWindowIcon(QIcon("gui/icon.png"))
