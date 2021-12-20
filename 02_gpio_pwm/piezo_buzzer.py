# 도(Do) 출력하기

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 : 도(262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) #start(Duty Cycle(0~100))

try:
    time.sleep(10)
    pwm.ChangeDutyCycle(0)

finally:
    pwm.stop()
    GPIO.cleanup()
