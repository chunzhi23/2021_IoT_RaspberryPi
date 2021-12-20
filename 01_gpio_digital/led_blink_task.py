import RPi.GPIO as GPIO
import time

LED_PIN_RED = 18
LED_PIN_YEL = 15
LED_PIN_GRE = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED, GPIO.OUT)
GPIO.setup(LED_PIN_YEL, GPIO.OUT)
GPIO.setup(LED_PIN_GRE, GPIO.OUT)

GPIO.output(LED_PIN_RED, GPIO.HIGH)
print("LED RED ON")
time.sleep(2)
GPIO.output(LED_PIN_RED, GPIO.LOW)

GPIO.output(LED_PIN_YEL, GPIO.HIGH)
print("LED YELLOW ON")
time.sleep(2)
GPIO.output(LED_PIN_YEL, GPIO.LOW)

GPIO.output(LED_PIN_GRE, GPIO.HIGH)
print("LED GREEN ON")
time.sleep(2)
GPIO.output(LED_PIN_GRE, GPIO.LOW)

GPIO.cleanup()