from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/forward')
def forward():
	app.robot.forward()
	return redirect(url_for('index'))

@app.route('/left')
def left():
	app.robot.left()
	return redirect(url_for('index'))

@app.route('/right')
	app.robot.right()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run()