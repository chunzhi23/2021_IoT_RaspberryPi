from lcd import drivers
import Adafruit_DHT
import time, datetime

display = drivers.Lcd()

sensor = Adafruit_DHT.DHT11
DHT_PIN = 21

try:
    while True:
        now = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        
        if h is not None and t is not None:
            display.lcd_display_string('{}'.format(now.strftime('%x%X')), 1)
            display.lcd_display_string('%.1lf*C, %.1lf%%' % (t, h), 2)
        else:
            print('ERROR 400')

        time.sleep(0.5)

finally:
    display.lcd_clear()
    print('System paused')

