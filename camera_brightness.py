from picamera import PiCamera
from time import sleep
from picamera import Color


camera =PiCamera()

camera.start_preview()

for i in range(100): #Changes the value of the brightness of screen
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()
