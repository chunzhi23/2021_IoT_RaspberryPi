import RPi.GPIO as GPIO
import time

PIR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

time.sleep(5)
print("PIR Set")

try:
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:
            print("Movement: ●")
        else:
            print("Movement: ○")
        
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print("Cleanup and exit")