import RPi.GPIO as GPIO

LED_PIN = 12
SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#스위치를 눌렀을 때 1을 출력

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        GPIO.output(LED_PIN, val)
        print(val)

finally:
    GPIO.cleanup()
    print("cleanup and exit")
