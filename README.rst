pytRobot
========

Interface for controlling simple tread robot (with `Raspberry
Pi <https://www.raspberrypi.org/>`__ as brain). Robot can be controlled
via CLI based commands or web application. Web application uses REST
API, which can be used to make other apps.

Robot uses Raspberry Pi with
`Picoborg <https://www.piborg.org/picoborg>`__ board to controll pair of
treads. Motors are powered by two AA batteries, Raspberry Pi is powered
via USB by a small powerbank. Robot is also equipped with
`camera <https://www.raspberrypi.org/products/camera-module/>`__.

Requirements
------------

- Python3.5
- click
- Flask
- RPi.GPIO
- picamera

These are requirements that can be installed via ``pip`` package manager. Web application also uses `mjpg streamer <https://github.com/jacksonliam/mjpg-streamer>`__, which is used to stream video from Pi's camera to the browser.

Streamer is a standalone program, and path to it has to be specified in ``config.ini`` file (more `here <#Installation>`__).

Alternatively you can run web app without video stream.

Installation
------------

You can get this package directly from github:

::

    $ git clone https://github.com/ggljzr/pytrobot
    $ cd pytrobot
    $ python3.5 setup.py install

If you want to use application with `mjpg streamer <https://github.com/jacksonliam/mjpg-streamer>`__, you have to compile it, and then create ``config.ini`` file specifying its location.

Default location of the ``config.ini`` is ``/etc/xdg/pytrobot/config.ini``.

::

    #create default directory for config
    $ sudo mkdir -p /etc/xdg/pytrobot/
    #copy example config in place
    $ sudo cp config.ini.example /etc/xdg/pytrobot/config.ini

``config.ini`` should look like this:

::

    [streamer]
    path = /path/to/mjpg-streamer
    fps = 25
    resx = 640
    resy = 480

``path`` should be pointg to the folder with ``mjpg_streamer`` executable. For example if you cloned mjpg streamer from Github to your default home directory, it will be ``/home/pi/mjpg-streamer/mjpg-streamer-experimental``. Note there is no trailing ``/``.

Streamer is used only in web application, so you don't need it for cli mode. If you don't want to install it at all, you can run web application with ``--no-stream`` option. In this case you don't need a config file.

Usage
-----

Application works in CLI or WEB mode. Both modes provide simple interface for controlling the robot.

Since both modes require access to GPIO pins (for obvious reasons), you'll probably have to run them as ``root``.

CLI Application
~~~~~~~~~~~~~~~

CLI app allows to send simple commands to controll the robot when
connecting to Raspberry Pi via SSH.

::

    # 90 deg turn to the left 
    $ sudo pyrobot turn left
    # take a shot with the camera
    $ sudo pyrobot capture img.jpg

Web Application
~~~~~~~~~~~~~~~

Web application is written using `Flask <http://flask.pocoo.org/>`__.
It's main purpose is to provide simple interface for controlling robot
and to display video feed from the camera. It also displays data from
various sensors as well as Raspberry Pi status (IP address etc...).
Other important role of web application is to provide REST API.

::

	#run web app with default config
	$ sudo pytrobot web

