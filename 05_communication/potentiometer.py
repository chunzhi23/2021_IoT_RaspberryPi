import spidev
import time

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
        # analog to voltage
        voltage = reading * 3.3 / 1023
        print(f"Reading={reading}, Voltage={voltage}")
        time.sleep(0.5)
finally:
    spi.close()