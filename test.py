#!/user/bin/python
import RPi.GPIO as GPIO
import time


up = 20
down = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(up, GPIO.OUT)
GPIO.setup(down, GPIO.OUT)

def Wait():
    time.sleep(0.1)
    
def Up(*num):
    if len(num) == 0:
        iter = 1
    else:
        iter = num[0]
    for i in range(iter):
        GPIO.output(up, GPIO.HIGH)
        Wait()
        GPIO.output(up, GPIO.LOW)
        Wait()
    
def Down(*num):
    if len(num) == 0:
        iter = 1
    else:
        iter = num[0]
    for i in range(iter):
        GPIO.output(down, GPIO.HIGH)
        Wait()
        GPIO.output(down, GPIO.LOW)
        Wait()

    
Up()
Down(4)
GPIO.cleanup()