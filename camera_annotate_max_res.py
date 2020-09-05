from picamera import PiCamera
from time import sleep
from picamera import Color


camera =PiCamera()

camera.resolution = (2592,1944) #to get the max resolution
camera.framerate = 15 #Max framerate
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text_size = 132
camera.annotate_text = "Hello World!"
sleep(5)
camera.capture('/home/pi/Testing/TestPycam/cap_annotate.jpg')
camera.stop_preview()
