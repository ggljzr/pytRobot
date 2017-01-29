PyRobot API
===========

PytRobot has basic REST API provided via Flask application. This provides interface to build other applications to control the robot. API bascially mirros functions of the web interface.

Move
----

Move command moves the robot in chosen direction for given period of time (in seconds):

::

	/move/<direction>/<period>/

This will move robot in ``<direction>`` for ``<period>>`` seconds. For example ``/move/forward/1.5``.

``<direction>`` is a mandatory parameter and has to be one of ``forward``, ``left``, ``right``. ``<period>`` is an optional parameter, default being 0.5 seconds.

Succesful move command redirects user back to index page (``/``), 302 status code can expected.

Unsuccessful move command can be caused either by invalid direction (not ``left``, ``right``, ``forward``) or invalid period if given (<period> parameter is not a parsable float). It will return 406 status code.

System info
-----------

Returns system info in a json with following format (example):

::

	{
		'nodename' : 'raspberrypi',
		'os' : 'Linux',
		'kernel' : '4.1.19-v7+',
		'uptime' : '6:12',
		'interfaces' : {
			'lo' : {
				'ip' : '127.0.0.1',
				'hwaddr' : '00:00:00:00:00:00'
			}
		}
	}

Streaming
---------

Video stream can be started/stoped with these commands:

::

	/start_stream/
	/stop_stream/

Both of these commands redirect to index page. If no streamer is present (application was run with ``--no-stream`` option), both commands will do nothing (just redirect to the index page).

Note that video stream is also available at `http://raspberrypi.local:8080/?action=stream` when mjpg-streamer is running.

Capturing images
----------------

Images can be captured with following command:

::

	/capture/

You can specifi vertical flip with ``<vflip>`` parameter:

::

	/capture/<vflip>

Default value is ``True``, values ``1``, ``true`` will be resolved as ``True``, anything else as ``False``.

This command returns captured image in ``.jpg`` format. Image is saved on Raspberry Pi in ``/tmp`` with timestamp as file name and then send to the client. Command returns status code 200 if everything goes well.

This command uses ``capture_img()`` function from ``camera`` module by default. If this function cannot be used because of active streaming (via mjpg streamer), command simply redirects to current stream snapshot on `http://raspberrypi.local:8080/?action=snapshot`.

Note that this snapshot is directly from mjpg streamer and therefore uses settings specified in ``config.ini``, so ``<vflip>`` parameter is disregarded in this case. 
