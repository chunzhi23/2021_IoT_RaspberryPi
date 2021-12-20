# ultrasonic.py
import RPi.GPIO as GPIO
import time

TRIG_PIN = 4
ECHO_PIN = 14
LED_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(TRIG_PIN, GPIO.HIGH) 
        # 1㎲ > 0.000001s
        time.sleep(0.00001) # 10㎲
        GPIO.output(TRIG_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN) == GPIO.LOW:
            pass
        start = time.time()

        while GPIO.input(ECHO_PIN) == GPIO.HIGH:
            pass
        stop = time.time()

        distance = stop - start
        length = 34321 * (distance / 2)

        if distance <= 20:
            GPIO.output(LED_PIN, GPIO.HIGH)
            led_status = "●"
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            led_status = "○"

        print("Distance: %.lfcm %c" % length, led_status)

        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print("cleanup and exit")