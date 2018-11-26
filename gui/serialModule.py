import time
import serial
import serial.tools.list_ports
import sys


class SerialClass():
    
    def __init__(self):
        pass

    def list_ports(self):
        ports_list = []
        
        for port in list(serial.tools.list_ports.comports()):
            ports_list.append(port.device)
        return ports_list


    def connect(self,port):
        self.uart = serial.Serial(
            port=port,
            baudrate=115200,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS
        )
        
    def disconnect(self):
        self.uart.close()

    def handshake(self):
        ack = False
        
        self.uart.write(bytes('A','utf-8'))
        time.sleep(1)
        
        if(self.uart.read(1) == b'a'):
            ack = True
                
        return ack

    def readSerial(self):
        return int.from_bytes(self.uart.read(1), byteorder='big', signed=True)