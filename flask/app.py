from flask import Flask, render_template, request
import os
from flask import send_from_directory
import RPi.GPIO as GPIO

app = Flask(__name__)

class Motor:
    LF = 21
    LB = 22
    RF = 23
    RB = 24

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.reset()

    def __del__(self):
        self.reset()
        GPIO.cleanup()

    def reset(self):
        GPIO.setup(self.LF, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.LB, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.RF, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.RB, GPIO.OUT, initial=GPIO.LOW)

    def control(self, value):
        self.reset()
        if value == "go":
            GPIO.output(self.LF, GPIO.HIGH)
            GPIO.output(self.RF, GPIO.HIGH)
        elif value == "back":
            GPIO.output(self.LB, GPIO.HIGH)
            GPIO.output(self.RB, GPIO.HIGH)
        elif value == "stop":
            pass
        elif value == "tr":
            GPIO.output(self.LB, GPIO.HIGH)
            GPIO.output(self.RF, GPIO.HIGH)
        elif value == "tl":
            GPIO.output(self.LF, GPIO.HIGH)
            GPIO.output(self.RB, GPIO.HIGH)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def greeting():
    return "Hello!!"

@app.route("/index")
def index():
    name = request.args.get("name")
    value = request.args.get("value")
    return render_template("index.html", name=name, value=value)

@app.route("/index", methods=["POST"])
def post():
    ctrl = request.form.get("ctrl", None)
    control(ctrl)
    name = request.args.get("name")
    value = request.args.get("value")
    return render_template("index.html", name=name, value=value)

def control(ctrl):
    #print("ctrl = {0}".format(ctrl))
    motor.control(ctrl)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup()

motor = Motor()
    
if __name__ == "__main__":
    try:
        #app.run(debug=False, host="0.0.0.0", port=443)
        #app.run(debug=False, host="0.0.0.0", port=80)
        app.run()
    except Exception as e:
        print(type(e))
        print(e)
        del motor
