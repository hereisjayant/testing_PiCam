# testing_PiCam
## camera.py
Demonstrates how to get a transparent preview for debugging
````
from picamera import PiCamera
from time import sleep

camera =PiCamera()
camera.rotation = 0
camera.start_preview(alpha=200)
sleep(10)
camera.stop_preview()
````
