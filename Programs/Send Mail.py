import os
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import smtplib
from email.message import EmailMessage
GPIO.setmode(GPIO.BCM)
sensor = Adafruit_DHT.DHT11
pin = 18
hum, temp = Adafruit_DHT.read_retry(sensor, pin)
if hum is None and temp is None:
    print("Failed to read, Try Again!")
else:
    print("Temperature: "+str(temp) + " *C " + " & Humidity:"+ str(hum) + "%")
raspi = 'touser2k23@gmail.com'
password = 'lgisesmrvwooblxn'
to =  'touser2k23@gmail.com'
fromras = raspi
msg = EmailMessage()
msg['Subject'] = "Temperature and Humidity"
msg['From'] = raspi
msg['To'] = 'touser2k23@gmail.com'
msg.set_content("Temperature: "+str(temp) + " *C " + " & Humidity:"+ str(hum) + "%")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(raspi, password)
print("Login Successfull")
server.send_message(msg)
server.quit()
print("Email has been sent")
