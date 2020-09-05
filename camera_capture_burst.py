from picamera import PiCamera
from time import sleep

camera =PiCamera()
camera.rotation = 0
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Testing/TestPycam/test2Image.jpg' % i )
camera.stop_preview()
