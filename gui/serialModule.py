import time
import serial


class SerialClass():
    def __init__(self):
        pass

    def list_ports(self):
        ports_list = ["COM2", "COM3", "COM4"]
        # must return a list of strings
        # code here
        return ports_list


    def connect(port):
        self.uart = serial.Serial(
            port=port,
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )

    def handshake(self):
        device_name = "radio1" # device name
        # something to do hand send banana receive banana
        # returns the name of the device
        return device_name

    def read(self):
        #metodo que le do serial
        pass


#ser.open()
#ser.isOpen()

#print('Enter your commands below.\r\nInsert "exit" to leave the application.')

#inp =1
#while 1 :
     # get keyboard input
         # Python 3 users
#    inp = input(">> ")
#    if inp == 'exit':
#        ser.close()
#        exit()
#    else:
         # send the character to the device
         # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
#        ser.write(bytes(inp + '\r\n','utf-8'))
#        out = ''
        # let's wait one second before reading output (let's give device time to answer)
#        time.sleep(1)
#    while ser.inWaiting() > 0:
#        out += ser.read(1).decode('utf-8')

#    if out != '':
#        print(out + "<<")