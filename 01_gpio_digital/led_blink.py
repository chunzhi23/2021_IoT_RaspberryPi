import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)  #GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN, GPIO.OUT)  #GPIO.OUT or GPIO.IN

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH) #1, True
    print("LED on")
    time.sleep(0.2)

    GPIO.output(LED_PIN, GPIO.LOW)  #0, False
    print("LED off")
    time.sleep(0.2)

GPIO.cleanup()  #GPIO 핀 상태 초기화