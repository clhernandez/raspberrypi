import RPi.GPIO as GPIO
import time

def ledOn(port, t):
	GPIO.output(port ,1)
	time.sleep(t)
	ledOff(port)

def ledOff(port):
	GPIO.output(port, 0)
	time.sleep(0.2)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
ledOff(12);

ledOn(12, 0.5)
ledOn(12, 0.5)
ledOn(12, 0.5)
ledOn(12, 1)
ledOn(12, 1)
ledOn(12, 1)
ledOn(12, 0.5)
ledOn(12, 0.5)
ledOn(12, 0.5)

GPIO.cleanup()