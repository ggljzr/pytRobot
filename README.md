# pytRobot
Interface for controlling simple tread robot (with Raspberry Pi as brain). Robot can be controlled via CLI based commands or web application. Web application uses REST API, which can be used to make other apps.

Robot uses Raspberry Pi with [Picoborg](https://www.piborg.org/picoborg) board to controll pair of treads. Motors are powered by two AA batteries, Raspberry Pi is powered via USB by a small powerbank. Robot is also equipped with [camera](https://www.raspberrypi.org/products/camera-module/).

## CLI Application

CLI app allows to send simple commands to controll the robot when connecting to Raspberry Pi via SSH.

```
# 90 deg turn to the left 
$ pyRobot turn left
# take a shot with the camera
$ pyRobot capture img.jpg
```

## Web Application

Web application is written using [Flask](http://flask.pocoo.org/). It's main purpose is to provide simple interface for controlling robot and to display video feed from the camera. It also displays data from various sensors as well as Raspberry Pi status (IP address etc...). Other important role of web application is to provide REST API.

Web server with application will run directly on Raspberry Pi.
