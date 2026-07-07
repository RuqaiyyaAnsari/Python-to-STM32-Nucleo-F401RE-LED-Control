import serial
import time

ser = serial.Serial('COM4', 115200)  # COM port change karo

time.sleep(2)

while True:
    cmd = input("Enter 1 (ON) or 0 (OFF): ")
    ser.write(cmd.encode())