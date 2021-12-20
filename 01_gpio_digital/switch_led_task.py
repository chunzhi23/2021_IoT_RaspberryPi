import RPi.GPIO as GPIO
import time

SWITCH_RED = 10
SWITCH_YEL = 9
SWITCH_GRE = 11

LED_RED = 17
LED_YEL = 27
LED_GRE = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_RED, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_YEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_GRE, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YEL, GPIO.OUT)
GPIO.setup(LED_GRE, GPIO.OUT)

try:
    while True:
        val_R = GPIO.input(SWITCH_RED)
        GPIO.output(LED_RED, val_R)
        
        val_Y = GPIO.input(SWITCH_YEL)
        GPIO.output(LED_YEL, val_Y)
        
        val_G = GPIO.input(SWITCH_GRE)
        GPIO.output(LED_GRE, val_G)

finally:
    GPIO.cleanup()
    print('cleanup and exit')