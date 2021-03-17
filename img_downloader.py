import sys
from ui import *
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
