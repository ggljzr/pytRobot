from flask import Flask, render_template, redirect, url_for, flash, abort
import json

from .robotdriver import DirError
from .utils import sys_info

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def index():
	sinfo = sys_info()
	return render_template('index.html', 
							is_stream=app.is_stream,
							sys_info=sinfo)

@app.route('/move/<direction>/')
@app.route('/move/<direction>/<period>')
def move(direction, period=0.5):
	try:
		app.robot.move(direction, float(period))
	except (DirError, TypeError, ValueError):
		abort(406)

	flash('Moving {} for {}s'.format(direction, period))
	return redirect(url_for('index'))

@app.route('/info')
def info():
	return json.dumps(sys_info())

@app.route('/start_stream')
def start_stream():
	if app.streamer is not None:
		app.streamer.start_stream()
		app.is_stream = True
		flash('Starting stream')
	else:
		flash('Runing in --no-stream mode')
	return redirect(url_for('index'))

@app.route('/stop_stream')
def stop_stream():
	if app.streamer is not None:
		app.streamer.stop_stream()
		app.is_stream = False
		flash('Stopping stream')
	else:
		flash('Runing in --no-stream mode')
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run()