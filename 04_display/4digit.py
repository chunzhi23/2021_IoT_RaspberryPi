# 4digit.py
import RPi.GPIO as GPIO
import time

# GPIO_PINS  :  A  B  C  D  E  F  G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]
DIGIT_PINS = [10, 11, 12, 13]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

# 자리 수 제어 핀 : HIGH -> OFF, LOW -> ON
for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9


def display(digit, num): # 자릿수, 숫자
    #해당하는 자릿수의 핀에만 LOW로 설정
    for i in range(4):
        if i + 1 == digit:
            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
    
    # 숫자 출력
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[num][i])
    time.sleep(0.001)

try:
    while True:
        shuzi = [2, 0, 2, 1]
        for i in range(4):
            display(i+1, shuzi[i])

finally:
    GPIO.cleanup()
    print("cleanup and exit")