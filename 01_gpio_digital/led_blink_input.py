import RPi.GPIO as GPIO

LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        val = int(input("1: ON, 0: OFF, 9: EXIT > "))
        if val == 0:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("LED off")
        elif val == 1:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("LED on")
        elif val == 9:
            break
        else:
            print("403 None")
finally:
    GPIO.cleanup()
    print("Cleanup and exit")