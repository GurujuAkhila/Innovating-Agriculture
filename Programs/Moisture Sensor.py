import os
import RPi.GPIO as GPIO
import time
import smtplib

GPIO.setmode(GPIO.BOARD)
moisture_sensor = 36
GPIO.setup(moisture_sensor, GPIO.IN)

moisture = GPIO.input(moisture_sensor)

while True:
    if (moisture):
        print("Need of Water")
    else:
        print(" No Need of Water")
    
    time.sleep(2)
