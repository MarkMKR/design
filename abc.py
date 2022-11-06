import serial
import time
arduino = serial.Serial(port='COM6', baudrate=57600, timeout=.1)
def write_read(x):
    s = str(x)
    string = "<BLACKOUT>"
    arduino.write(bytes(string, 'utf-8'))
    string = "<LEDBLINK"+"\0"+s+"\0"+"100"+"\0"+"100"+">"
    arduino.write(bytes(string, 'utf-8'))
    time.sleep(.5)
    data = arduino.read_all()
    print(data.decode())
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
