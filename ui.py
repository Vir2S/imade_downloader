from config import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QTextEdit, QGridLayout, QWidget, QListWidget
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = TITLE
        self.icon = ICON
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

        self.layout = QGridLayout()
        self.layout.addWidget(self.url_entry)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.urls_entry)

        self.setLayout(self.layout)

        self.add_button.clicked.connect(self.add_url)

    def add_url(self):
        self.urls.append(self.url_entry.text())
        self.urls_entry.addItem(self.url_entry.text())
