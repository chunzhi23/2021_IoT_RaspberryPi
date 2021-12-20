# ultrasonic.py
# 초음파 차량 감지 실습

import RPi.GPIO as GPIO
import time

TRIG_PIN = 4
ECHO_PIN = 5
BUZZER_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 392)

try:
    while True:
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN) == GPIO.LOW:
            pass
        start = time.time()

        while GPIO.input(ECHO_PIN) == GPIO.HIGH:
            pass
        stop = time.time()

        duar = stop - start
        length = 34321 * (duar / 2)

        if length <= 10:
            pwm.start(50)
            time.sleep(0.5)
        elif length <= 30:
            pwm.start(50)
            time.sleep(1)
        else:
            print("400 ERROR")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("cleanup and exit")