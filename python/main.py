import serial
import time
import voicemeeter
import json
from plyer import notification

kind = 'potato'
ser = serial.Serial('COM11', 9800, timeout=1)


def loop(voicemr):
    notification.notify(
        title='VoicemeeterSlider',
        message=voicemr.type,
        app_icon=None,
        timeout=10,
    )
    time.sleep(10)
    loop(voicemr)


def __main__():
    notification.notify(
        title='VoicemeeterSlider',
        message='Starting VoicemeeterSlider',
        app_icon=None,
        timeout=10,
    )
    voicemr = initializeVoicemeeter()
    initializeSerial()
    loop(voicemr)
    if voicemr != None:
        readSerial(voicemr)


def readSerial(voicemr):
    lastValues = [0, 0, 0, 0, 0, 0]
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
                        value = round(int(j[check]) / 655 * 60 - 60, 2)
                        if value >= 0.0:
                            value = 0.0
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
