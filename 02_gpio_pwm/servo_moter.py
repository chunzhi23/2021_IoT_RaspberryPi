# servo_moter.py
# 1~2ms from datasheet, Max ±0.5ms

import RPi.GPIO as GPIO

SERVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5)

try:
    while True:
        val = int(input("1. 0°, 2. -90°, 3. 90°, 9. Exit > "))
        if val == 1:
            pwm.ChangeDutyCycle(7.5)  # 0°
        elif val == 2:
            # pwm.ChangeDutyCycle(5)  # -45°
            pwm.ChangeDutyCycle(2.5)  # -90°
        elif val == 3:
            # pwm.ChangeDutyCycle(10) # 45°
            pwm.ChangeDutyCycle(12.5) # 90°
        elif val == 9: # Exit
            break
finally:
    pwm.stop()
    GPIO.cleanup()
    print("cleanup and exit")