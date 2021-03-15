import bluetooth
import time

ADDRESS = "58:BD:A3:B9:2E:72"
socket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
socket.connect((ADDRESS, 0x13))

def write(value):
        socket.send(('a2' + value).decode('hex'))

def read(bytes):
        return socket.recv(bytes).encode('hex')