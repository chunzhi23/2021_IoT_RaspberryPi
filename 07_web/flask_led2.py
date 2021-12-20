from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("led.html")


@app.route("/led/<cmd>")
def led_op(cmd):
    if cmd == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif cmd == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"
    else:
        return "404 error"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    finally:
        GPIO.cleanup()
