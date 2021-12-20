import RPi.GPIO as GPIO
import spidev
import time

LED_PIN = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# create SPI instance
spi = spidev.SpiDev()
# SPI start
spi.open(0, 0)  # bus: 0, dev: 0(CE0, CE1)

# set SPI maximum speed
spi.max_speed_hz = 100000

# read SPI data from 0~7 channels
def analog_read(channel):
    # [byte_1, byte_2, byte_3]
    # byte_1: 1
    # byte_2: (channel + 8) << 4
    # byte_3: 0
    ret = spi.xfer2([1, (channel + 8) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0) # 0~1023

        if reading < 512:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else :
            GPIO.output(LED_PIN, GPIO.LOW)

        print(f"Reading={reading}")
        time.sleep(0.5)

finally:
    spi.close()
    GPIO.cleanup()