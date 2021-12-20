import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    while True:
        shi, wen = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if shi is not None and wen is not None:
            print("Temperature: %.1lf℃" % wen)
            print("Humidity: %.1lf%%" % shi)
        else:
            print("Read Error")
finally:
    print("system exit")