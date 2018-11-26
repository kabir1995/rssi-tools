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
import time
 

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
        self.error_msg = ''
        self.connected = False
        self.s = SerialClass()
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.m = PlotCanvas(self, width=5, height=4)

        # Dropdown menu
        l_uart_ports = w.QLabel('UART Ports:', self)
        l_uart_ports.move(self.menu_x_cord,0)
        l_uart_ports.resize(self.menu_width,20)

        l_dropdown = w.QComboBox(self)
        l_dropdown.move(self.menu_x_cord, 30)
        [l_dropdown.addItem(port) for port in self.s.list_ports()]
        l_dropdown.activated[str].connect(self.connect_to_board)

        # Samples
        l_samples = w.QLabel('Samples:', self)
        l_samples.move(self.menu_x_cord,70)
        l_samples.resize(self.menu_width,20)
        self.li_samples = w.QLineEdit(self)

        self.li_samples.move(self.menu_x_cord, 90)
        self.li_samples.resize(self.menu_width, 30)

        # Sample rate
        l_srate = w.QLabel('Sample Rate [ms]:', self)
        l_srate.move(self.menu_x_cord,120)
        l_srate.resize(self.menu_width,20)
        self.l_srate = w.QLineEdit(self)

        self.l_srate.move(self.menu_x_cord, 140)
        self.l_srate.resize(self.menu_width, 30)

        # Distance
        l_distance = w.QLabel('Distance [m]:', self)
        l_distance.move(self.menu_x_cord,170)
        l_distance.resize(self.menu_width,20)
        self.l_distance = w.QLineEdit(self)

        self.l_distance.move(self.menu_x_cord, 190)
        self.l_distance.resize(self.menu_width, 30)

        # Start experiment
        b_start = w.QPushButton('Start experiment', self)
        b_start.move(self.menu_x_cord,350)
        b_start.resize(self.menu_width,50)
        b_start.clicked.connect(self.experiment)

        self.show()

    def connect_to_board(self, port):
        if self.s.handshake():
            msg = "Connected to radio!"
            self.connected = True
        else:
            msg = "Connection Failed!"
            self.connected = False
        w.QMessageBox.about(self, "Connection Status", msg)

    def experiment(self):
        # Dealing with input
        try:
            samples = self._get_samples()
            sample_rate = self._get_sample_rate()
            distance = self._get_distance()
            self._test_connection()
        except: 
            w.QMessageBox.about(self, "Error", self.error_msg)
            return

        print("Starting experiment")
        print("{} samples, one every {} ms, at {} meters".format(
            samples, sample_rate, distance)
        )

        filename = "{}s_{}ms_{}m.txt".format(
            samples, sample_rate, distance
        )

        # Experiment
        for n in range(1, samples+1):
            self.append_to_file(self.s.readSerial(), filename)
            self.m.plot(filename)
            self.show()
            time.sleep(sample_rate/1000)

        w.QMessageBox.about(self, "Experiment Status", "Finished!")

    def append_to_file(self, data, filename):
        with open(filename, "a+") as f:
            f.write(str(data)+"\r\n")

    # Helper funcions
    def _get_samples(self):
        try:
            samples = int(self.li_samples.text())
        except:
            self.error_msg = "Samples must be integer!"
            raise
        if samples <= 0:
            self.error_msg = "Samples must be greater than zero!"
            raise
        return samples

    def _get_sample_rate(self):
        try:
            sample_rate = int(self.l_srate.text())
        except:
            self.error_msg = "Sample Rate must be integer!"
            raise
        if sample_rate < 20:
            self.error_msg = "Sample Rate must greater than 20 ms!"
            raise
        return sample_rate

    def _get_distance(self):
        try:
            distance = float(self.l_distance.text())
        except:
            self.error_msg = "Distance must be float!"
            raise
        if distance <= 0:
            self.error_msg = "Distance must greater than zero!"
            raise
        return distance

    def _test_connection(self):
        if not self.connected:
            self.error_msg = "Must be connected to a radio"
            raise

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4):
        fig = Figure(figsize=(width, height))
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                w.QSizePolicy.Expanding,
                w.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self) 
        #self.plot()
 
    def plot(self, filename): 
        print("plot")
        ax = self.figure.add_subplot(111)
        with open(filename) as f: 
            data = [int(x) for x in f.read().splitlines()] 
        ax.plot(data, 'r-')
        ax.set_title('RSSI samples')
        ax.set_ylabel("RSSI [dBm]")
        ax.set_xlabel("Samples")
        self.draw()
