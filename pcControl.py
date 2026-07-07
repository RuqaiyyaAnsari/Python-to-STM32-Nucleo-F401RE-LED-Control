import serial
import pyautogui

ser = serial.Serial('COM4',115200)

while True:
    data = ser.readline().decode().strip()
    print(data)

    if data == '1':
        print("Volume UP")
        pyautogui.press('volumeup')

    elif data == '2':
        print('Volume DOWN')
        pyautogui.press('volumedown')

    elif data =='3':
        print('Opening Notepad')
        pyautogui.press('win')
        pyautogui.write('notepad')
        pyautogui.press('enter')