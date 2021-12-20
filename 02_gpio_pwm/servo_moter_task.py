# servo_moter_task.py
# 서보 모터 실습

import RPi.GPIO as GPIO
import time

SWITCH_PIN = 4
SERVO_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5)

count = 1   # 0˚ → -90˚ → 0˚ → 90˚
            # 7.5 → 2.5 → 7.5 → 12.5

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        
        if val:
            if count == 1 or count == 3:
                pwm.ChangeDutyCycle(7.5)
            elif count == 2:
                pwm.ChangeDutyCycle(2.5)
            elif count == 4:
                pwm.ChangeDutyCycle(12.5)
            else:
                print("404 ERROR")
            
            if count + 1 >= 5:
                count = 1
            else:
                count += 1
finally:
    pwm.stop()
    GPIO.cleanup()
    print("cleanup and exit")