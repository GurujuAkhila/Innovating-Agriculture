import os
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11
pin = 18
while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    if hum is None and temp is None:
        print("Failed to read, Try Again!")
    else:
        print("Temperature: "+str(temp) + " *C " + " & Humidity:"+ str(hum) + "%")
