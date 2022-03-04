import serial
import time
import voicemeeter
import json

kind = 'potato'
ser = serial.Serial('COM11', 9800, timeout=1)

def __main__(): 
#    print("Starting..")
    voicemr = initializeVoicemeeter()
    initializeSerial()
    if voicemr != None: 
        readSerial(voicemr)

def readSerial(voicemr):
    lastValues = [0,0,0,0,0,0]
    while True:
        try:
            line = ser.readline()
            if line:
                string = line.decode()           
                j = json.loads(string)
                count = 0
                for i in lastValues:
                    check = "Slider"+str(count)
                    if i < j[check]-2 or i > j[check]+2:
                        lastValues[count] = int(j[check])
                        value = round(int(j[check]) / 655 * 72 -60, 2)
                        voicemr.inputs[count].gain = float(value)
                    count = count + 1 
        except:
#            print("Keyboard Interrupt")
            ser.close()
            break

def initializeSerial():
    ser.flushInput()
    time.sleep(2)

def initializeVoicemeeter():
#    print("Ensure that Voicemeeter is launched..")
    voicemeeter.launch(kind)

    vmr = voicemeeter.remote(kind)
    vmr.login()
    return vmr


__main__()

