from lcd import drivers
import time

display = drivers.Lcd()

try:
    display.lcd_display_string('Hello World', 1)
    while True:
        display.lcd_display_string('** Welcome **', 2)
        time.sleep(2)
        display.lcd_display_string('   Welcome   ', 2)
        time.sleep(2)
finally:
    display.lcd_clear()
    print(' Cleaning up!')