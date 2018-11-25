import sys
from gui import App
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())   

if __name__ == '__main__':
    main()