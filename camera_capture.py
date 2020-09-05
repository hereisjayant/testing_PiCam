from picamera import PiCamera
from time import sleep

camera =PiCamera()
camera.rotation = 0
camera.start_preview(alpha=200)
sleep(10)
camera.capture('/home/pi/Testing/TestPycam/testImage.jpg')
camera.stop_preview()
