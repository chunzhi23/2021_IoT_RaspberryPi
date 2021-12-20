import RPi.GPIO as GPIO
import time

LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# PWM 인스턴스 생성
# 주파수 설정(50Hz)
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0) #Duty cycle(0~100) 초깃값

try:
    for i in range(3):
        #서서히 커지도록    
        for j in range(0, 101, 10):  #range(start=0, end, step=1)
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
        #서서히 꺼지도록
        for j in range(100, -1, -10):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
finally:
    pwm.stop()  #PWM 종료문
    GPIO.cleanup()
    print("cleanup and exit")