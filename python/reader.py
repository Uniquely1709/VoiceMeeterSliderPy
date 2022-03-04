import serial
import time
ser = serial.Serial('COM11', 9800, timeout=1)
ser.flushInput()
time.sleep(2)

while True:
    try:
        line = ser.readline()
        if line:
            string = line.decode()  # convert the byte string to a unicode string
            #num = int(string) # convert the unicode string to an int
            print(string)
    except:
        print("Keyboard Interrupt")
        ser.close()
        break

ser.close()