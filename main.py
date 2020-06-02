import sys
import time
import RPi.GPIO as GPIO


# Callback called when switch is pressed.
def sensor1_callback(channel):
    p.ChangeDutyCycle(5)
    print("sensor1")
    time.sleep(0.5)
def sensor2_callback(channel):
    p.ChangeDutyCycle(6)
    print("sensor2")
    time.sleep(0.5)
def sensor3_callback(channel):
    print("sensor3")
    p.ChangeDutyCycle(7)
    time.sleep(0.5)
def sensor4_callback(channel):
    print("sensor4")
    p.ChangeDutyCycle(8)
    time.sleep(0.5)
def sensor5_callback(channel):
    print("sensor5")
    p.ChangeDutyCycle(9)
    time.sleep(0.5)
def sensor6_callback(channel):
    print("sensor6")
    p.ChangeDutyCycle(10)
    time.sleep(0.5) 
sensor1 = 2  # Red
sensor2 = 4  # Green
sensor3 = 17  # Yellow
sensor4 = 10  # Red
sensor5 = 19  # Green
sensor6 = 3
servoPIN = 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50) # GPIO 10 for PWM with 50Hz
p.start(7.5) 
GPIO.setup(sensor1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sensor6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(sensor1, GPIO.FALLING, callback=sensor1_callback)
GPIO.add_event_detect(sensor2, GPIO.FALLING, callback=sensor2_callback)
GPIO.add_event_detect(sensor3, GPIO.FALLING, callback=sensor3_callback)
GPIO.add_event_detect(sensor4, GPIO.FALLING, callback=sensor4_callback)
GPIO.add_event_detect(sensor5, GPIO.FALLING, callback=sensor5_callback)
GPIO.add_event_detect(sensor6, GPIO.FALLING, callback=sensor6_callback)
while True:
     time.sleep(0.1)