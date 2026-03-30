import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print('LED on')
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print('LED off')
GPIO.output(18,GPIO.LOW)
#Yang Letian 26/3/30 this is a program to let LED on for a second
