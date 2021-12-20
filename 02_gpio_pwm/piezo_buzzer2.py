# 도레미파솔라시도 출력

import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(50)

melody = [262, 294, 330, 349, 392, 440, 494, 523]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(2)

finally:
    pwm.stop()
    GPIO.cleanup()
    print("cleanup and exit")