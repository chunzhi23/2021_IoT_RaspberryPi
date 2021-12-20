from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_PIN = 4
YEL_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YEL_PIN, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("led2.html")


@app.route("/led/<hex>/<cmd>")
def led_op(hex, cmd):
    if hex == "red":
        if cmd == "on":
            GPIO.output(RED_PIN, GPIO.HIGH)
        elif cmd == "off":
            GPIO.output(RED_PIN, GPIO.LOW)

        return "%s LED %s" % (hex.upper(), cmd.upper())

    elif hex == "yellow":
        if cmd == "on":
            GPIO.output(YEL_PIN, GPIO.HIGH)
        elif cmd == "off":
            GPIO.output(YEL_PIN, GPIO.LOW)

        return "%s LED %s" % (hex.upper(), cmd.upper())

    else:
        return "403 error"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    finally:
        GPIO.cleanup()
