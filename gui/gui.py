import sys
import PyQt5.QtWidgets as w
#(QMainWindow, QMenu, QVBoxLayout, 
#    QSizePolicy, QMessageBox, QWidget, QPushButton, QHBoxLayout)
from PyQt5.QtGui import QIcon
#******************************************************************
import matplotlib
matplotlib.use("Qt5Agg")
#******************************************************************
from PyQt5 import QtCore 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from serialModule import SerialClass
 

class App(w.QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'RSSI Tools'
        self.menu_x_cord = 500
        self.menu_width = 140
        self.width = 640
        self.height = 400
        self.s = SerialClass()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.m = PlotCanvas(self, width=5, height=4)

        l_uart_ports = w.QLabel('UART Ports:', self)
        l_uart_ports.move(self.menu_x_cord,0)
        l_uart_ports.resize(self.menu_width,20)

        l_dropdown = w.QComboBox(self)
        l_dropdown.move(self.menu_x_cord, 30)
        # adding each port
        [l_dropdown.addItem(port) for port in self.s.list_ports()]
        l_dropdown.activated[str].connect(self.connect_to_board)

        l_samples = w.QLabel('Samples:', self)
        l_samples.move(self.menu_x_cord,70)
        l_samples.resize(self.menu_width,20)
        self.li_samples = w.QLineEdit(self)

        self.li_samples.move(self.menu_x_cord, 90)
        self.li_samples.resize(self.menu_width, 30)

        b_start = w.QPushButton('Start experiment', self)
        b_start.move(self.menu_x_cord,350)
        b_start.resize(self.menu_width,50)
        b_start.clicked.connect(self.experiment)

        self.show()

    def connect_to_board(self, port):
        try:
            self.s.connect(port)
            device = self.s.handshake()
            w.QMessageBox.about(self, "Connection Status", "Connected to " + device)
        except:
            w.QMessageBox.about(self, "Connection Status", "Connection Failed!")

    def experiment(self):
        try:
            samples = self._get_samples()
        except: 
            w.QMessageBox.about(self, "Error", "Must number greater than zero!")
            return
        print(samples)
        
    
    def _get_samples(self):
        try:
            samples = int(self.li_samples.text())
        except:
            raise
        if samples <= 0:
            raise
        return samples



class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.updateGeometry(self)
        self.data = []

        #self.plot()

 
    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.plot(self.data, 'r-')
        ax.set_title('RSSI samples')
        ax.set_ylabel("RSSI [dBm]")
        ax.set_xlabel("Samples")
        self.draw()

    def update_data(data):
        self.data = data
