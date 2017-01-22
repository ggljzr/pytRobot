from flask import Flask, render_template, redirect, url_for, request
import json

from .utils import sys_info, handled_float

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', is_stream=app.is_stream)

@app.route('/forward')
def forward():
	period = handled_float(request.args.get('per'), 0.5)
	app.robot.forward(period)
	return render_template('index.html', is_stream=app.is_stream)

@app.route('/left')
def left():
	period = handled_float(request.args.get('per'), 0.5)
	app.robot.left(period)
	return render_template('index.html', is_stream=app.is_stream)

@app.route('/right')
def right():
	period = handled_float(request.args.get('per'), 0.5)
	app.robot.right(period)
	return render_template('index.html', is_stream=app.is_stream)

@app.route('/info')
def info():
	return json.dumps(sys_info())

@app.route('/start_stream')
def start_stream():
	if app.streamer is not None:
		app.streamer.start_stream()
		app.is_stream = True
	return render_template('index.html', is_stream=app.is_stream)

@app.route('/stop_stream')
def stop_stream():
	if app.streamer is not None:
		app.streamer.stop_stream()
		app.is_stream = False
	return render_template('index.html', is_stream=app.is_stream)

if __name__ == '__main__':
	app.run()