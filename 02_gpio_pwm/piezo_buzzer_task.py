import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 392)
pwm.start(50)

melody = [
    392, 392, 440, 440, 392, 392, 330,
    392, 392, 330, 330, 294, 1,
    392, 392, 440, 440, 392, 392, 330,
    392, 330, 294, 330, 262
]

wait = [
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
    0.5, 0.5, 0.5, 0.5, 1, 0.2,
    0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
    0.5, 0.5, 0.5, 0.5, 1
]

try:
    for i in range(25):
        pwm.ChangeFrequency(melody[i])
        time.sleep(wait[i])

finally:
    pwm.stop()
    GPIO.cleanup()
    print("cleanup and exit")