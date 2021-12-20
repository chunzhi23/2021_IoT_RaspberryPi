from flask import Flask
import RPi.GPIO as GPIO

RED_PIN = 4
BLUE_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def main():
    return '''
        <h2>Hello, Flask!</h2>
        <h3>RED LED</h3>
        <a href="/led/red/on">LED ON</a>
        <a href="/led/red/off">LED OFF</a>
        
        <h3>BLUE LED</h3>
        <a href="/led/blue/on">LED ON</a>
        <a href="/led/blue/off">LED OFF</a>
    '''

@app.route('/led/<hex>/<cmd>')
def led_op(hex, cmd):
    if hex == 'red':
        if cmd == 'on':
            GPIO.output(RED_PIN, GPIO.HIGH)
        elif cmd == 'off':
            GPIO.output(RED_PIN, GPIO.LOW)
            
        return '''
            <p>LED %s %s</p>
            <a href="/">Go Home</a>
        ''' % (hex.upper(), cmd.upper())

    elif hex == 'blue':
        if cmd == 'on':
            GPIO.output(BLUE_PIN, GPIO.HIGH)
        elif cmd == 'off':
            GPIO.output(BLUE_PIN, GPIO.LOW)
            
        return '''
            <p>LED %s %s</p>
            <a href="/">Go Home</a>
        ''' % (hex.upper(), cmd.upper())
        
    else:
        return '<p>403 error</p>'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', debug=True)
    finally:
        GPIO.cleanup()