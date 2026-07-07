import serial
import pyautogui
import time
import os


ser = serial.Serial('COM4', 115200, timeout=1)

time.sleep(2)  

print("Listening...")

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode(errors='ignore').strip()
        print("Received:", data)

        if "OPEN" in data:   
            print("Opening Notepad...")
            os.system("notepad")
            time.sleep(2)
            pyautogui.write("Hello 👋! Ruqaiyya Here..\n  Connect with me to explore more interactive projects.", interval=0.1)




            #os.system("notepad")
          