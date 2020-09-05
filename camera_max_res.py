from picamera import PiCamera
from time import sleep



camera =PiCamera()

camera.resolution = (2592,1944) #to get the max resolution
camera.framerate = 15 #Max framerate
camera.start_preview()
camera.annotate_text = "Hello World!"
sleep(5)
camera.capture('/home/pi/Testing/TestPycam/cap_annotate.jpg')
camera.stop_preview()
