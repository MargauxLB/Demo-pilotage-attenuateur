# Script pour att USB et socket.
# Script écrit en python 3.
# Pour connaitre tous les mots de commande sur le site: http://hytem3.free.fr .
# Par Margaux Leblanc Hytem v1.0

import serial
import socket
import time

class Attenuateur :
    def __init__(self):
        self.ser=None
        self.sock = None

    def connexion_serial(self, COM):
        print("Ports: ", COM)
        try:
            self.ser = serial.Serial()
            self.ser.baudrate = 38400
            self.ser.parity = serial.PARITY_NONE
            self.ser.stopbits = serial.STOPBITS_ONE
            self.ser.bytesize = serial.EIGHTBITS
            self.ser.port = COM
            self.ser.timeout = .5
            self.ser.open()
        except:
            self.ser = None


    def connexion_network(self, ip, port=10001):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP with STREAM
            print("IP: ", ip,", Port: ",port)
            self.sock.connect((ip, port))
            time.sleep(.1)
            self.sock.send("IDN?\n".encode('ascii'))
            name = (self.sock.recv(1024))
            print('Name: ', name.decode('ascii'))
        except:
            self.sock=None


    def set_value(self,value):
        value10 = 'ATT 0 {:03n}\n'.format(value * 10)
        if self.ser != None:
            self.ser.write(value10.encode())

        if self.sock != None:
            self.sock.send(value10.encode())


    def close(self):
        if self.ser != None:
            self.ser.close()
        if self.sock != None:
            self.sock.close()


if __name__ == '__main__':
    att =Attenuateur()
    try:
        att.connexion_serial('COM4')
    except:
        pass
    try:
        att.connexion_network('192.168.150.108')
    except:
        pass

    for i in range(5):
        for value in (0.5,1,2,4,8,16,32,93.5):
            att.set_value(value)
            time.sleep(0.5)
    att.close()
