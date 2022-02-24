#Photoshoot and recording program for CanSat
#Importing libraries
from picamera import PiCamera
from time import sleep

#Sent countdown for launch
countdown = int()
#Setting up the camera
camera = PiCamera()

#Actual program
sleep(countdown) #Insert value in seconds in brackets

#TESTING
#camera.start_preview()

camera.start_recording('/home/pi/Desktop/launch/launch.h264')
sleep(15)
camera.stop_recording()

for i in range (4):
    sleep(3)
    camera.capture('/home/pi/Desktop/captures/image%s.jpg' % i)


#TESTING
#camera.stop_preview()


