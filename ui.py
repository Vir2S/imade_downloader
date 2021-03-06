import urllib.request
from config import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QTextEdit, QGridLayout, QWidget, QListWidget
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = TITLE
        self.icon = ICON
        self.dir = DIR
        self.create_ui()
        self.urls = []
        # self.setupUi(self)

    def create_ui(self):
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))

        self.urls_entry = QListWidget()
        self.url_entry = QLineEdit("URL", self)
        self.add_button = QPushButton("Add", self)
        self.download_button = QPushButton("Download", self)

        self.layout = QGridLayout()
        self.layout.addWidget(self.url_entry, 0, 0)
        self.layout.addWidget(self.add_button, 0, 1)
        self.layout.addWidget(self.urls_entry, 1, 0, 1, 2)
        self.layout.addWidget(self.download_button, 2, 1)

        self.setLayout(self.layout)

        self.add_button.clicked.connect(self.add_url)
        self.download_button.clicked.connect(self.download)

    def add_url(self):
        self.urls.append(self.url_entry.text())
        self.urls_entry.addItem(self.url_entry.text())
        self.url_entry.clear()

    def download(self):
        for url in self.urls:
            name = url.split("/")[-1]
            urllib.request.urlretrieve(url, self.dir + name)
