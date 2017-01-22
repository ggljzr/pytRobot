from flask import Flask, render_template, redirect, url_for, request
import json

from .utils import sys_info, handled_float

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/forward')
def forward():
	period = handled_float(request.args.get('per'), 0.5)
	app.robot.forward(period)
	return redirect(url_for('index'))

@app.route('/left')
def left():
	period = handled_float(request.args.get('per'), 0.5)
	app.robot.left(period)
	return redirect(url_for('index'))

@app.route('/right')
def right():
	period = handled_float(request.args.get('per'), 0.5)
	app.robot.right(period)
	return redirect(url_for('index'))

@app.route('/info')
def info():
	return json.dumps(sys_info())

if __name__ == '__main__':
	app.run()