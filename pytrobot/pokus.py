from camera import MjpgStreamer
import time

path = '/home/pi/git/mjpg-streamer/mjpg-streamer-experimental'

streamer = MjpgStreamer(path)

streamer.start_stream()

time.sleep(30)

streamer.stop_stream()