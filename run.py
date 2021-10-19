import serial
import time
import pyautogui

ser = serial.Serial('COM11', 9600, timeout=0,
                    parity=serial.PARITY_NONE, rtscts=1)

send = True
time.sleep(5)
last_send = ''

while 1:
    # time.sleep(0.5)
    bytesToRead = ser.inWaiting()
    s = ser.read(bytesToRead)
    # print(s,bytesToRead)
    # print(s.decode('Ascii').split(' '))
    # print('s',s)
    val = s.decode('Ascii').split('g\r\n')
    # print('val0',val)
    if len(val)>1:
        val = val[0]
    # print('val',val)
    if 'ST' not in val:
        time.sleep(0.5)
        continue

    w = val.strip().replace('ST,+','')
    print('w',w)

    # if cur != w[:]:
    #     cur = w[:]


    if not w:
        time.sleep(1)
        continue
    # print("sending..",send,w)
    if float(w) > 1.0 and w!=last_send:
        send = 1

    if send and float(w):
        print('typing..',w)
        pyautogui.write(w)
        pyautogui.press('enter')
        send = 0
        last_send = w[:]
        time.sleep(5)

    time.sleep(1)

