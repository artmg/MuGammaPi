#!/usr/bin/env python

"""ps3ControlCamJamCar.py: Control CamJam Edukit 3 Robotics on Raspberry Pi with PS3 Controller over Bluetooth."""

__author__ = "ArtMG"
__contact__ = "https://github.com/artmg/MuGammaPi/blob/master/EduKitRobotics/ps3ControlCamJamCar.py"
__status__ = "Production"

# For more on this see the accompanying article https://github.com/artmg/MuGammaPi/wiki/CamJam-Robotics-Kit

import RPi.GPIO as GPIO # GPIO output
import sys				# exit with error
import os 				# shutdown
import pygame 			# PS3 input
import signal			# sigterm handler

# get variables from settings.py module 
from settings import *


# Initialise the pygame library
pygame.init()

# test that a controller is connected, else quit
pygame.joystick.init()
if pygame.joystick.get_count() == 0:
	sys.exit("pygame says you have NO controllers connected")

# section credit - http://www.instructables.com/id/Remote-Raspberry-Pi-Robot-PS3-Controller-Fablab-Ne/?ALLSTEPS
# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()


# section credit https://github.com/CamJam-EduKit/EduKit3/blob/master/Code/4-driving.py

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO Pin mode
# NB these are variables stored in the settings.py module
GPIO.setup(pinMotorLeftForwards, GPIO.OUT)
GPIO.setup(pinMotorLeftBackwards, GPIO.OUT)
GPIO.setup(pinMotorRightForwards, GPIO.OUT)
GPIO.setup(pinMotorRightBackwards, GPIO.OUT)

# Set all motors off
def turn_off_motors():
	GPIO.output(pinMotorLeftForwards, 0)
	GPIO.output(pinMotorLeftBackwards, 0)
	GPIO.output(pinMotorRightForwards, 0)
	GPIO.output(pinMotorRightBackwards, 0)

turn_off_motors()

# Handle service termination
# credit - https://blog.lanyonm.org/articles/2015/01/11/raspberry-pi-init-script-python.html#python-to-handle-the-term-signal
def sigterm_handler(_signo, _stack_frame):
    print("Received signal {}, exiting...".format(_signo))
    turn_off_motors()
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

# workaround for pygame issues with lack of display
# credit - https://www.raspberrypi.org/forums/viewtopic.php?t=130201&p=869560
os.putenv('DISPLAY', ':0.0') 
pygame.display.init()
# however this now forces you to **run as root** with sudo


# section shared credit - https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=163814
# section shared credit - http://www.instructables.com/id/Remote-Raspberry-Pi-Robot-PS3-Controller-Fablab-Ne/?ALLSTEPS
# inputThreshold now in settings.py module
LeftTrack = 0
RightTrack = 0

# Configure the motors to match the current settings.

# Try and run the main code, and in case of failure we can stop the motors
try:

    # This is the main loop
    while True:

        # Check for any queued events and then process each one
        events = pygame.event.get()
        for event in events:
          UpdateMotors = 0

          # Check if one of the joysticks has moved
          if event.type == pygame.JOYAXISMOTION:
            if event.axis == 1:
              LeftTrack = event.value
              UpdateMotors = 1

            elif event.axis == 3:
              RightTrack = event.value
              UpdateMotors = 1


            # Check if we need to update what the motors are doing
            if UpdateMotors:

              # Check how to configure the LEFT motor
              # Move FORWARDS
              if (LeftTrack > inputThreshold):
                  GPIO.output(pinMotorLeftForwards, 1)
                  GPIO.output(pinMotorLeftBackwards, 0)
              # Move BACKWARDS
              elif (LeftTrack < -inputThreshold):
                  GPIO.output(pinMotorLeftForwards, 0)
                  GPIO.output(pinMotorLeftBackwards, 1)
              # Otherwise stop
              else:
                  GPIO.output(pinMotorLeftForwards, 0)
                  GPIO.output(pinMotorLeftBackwards, 0)

              # And do the same for the RIGHT motor
              # Move FORWARDS
              if (RightTrack > inputThreshold):
                  GPIO.output(pinMotorRightForwards, 1)
                  GPIO.output(pinMotorRightBackwards, 0)
              # Move BACKWARDS
              elif (RightTrack < -inputThreshold):
                  GPIO.output(pinMotorRightForwards, 0)
                  GPIO.output(pinMotorRightBackwards, 1)
              # Stopping
              else:
                  GPIO.output(pinMotorRightForwards, 0)
                  GPIO.output(pinMotorRightBackwards, 0)



except KeyboardInterrupt:
    print("Received keyboard interrupt, exiting...")
	
finally:
    turn_off_motors()
    j.quit()#!/usr/bin/env python

GPIO.cleanup()


### Other links

# shut down the Pi on given command...
# credit https://github.com/recantha/EduKit3-Bluetooth/blob/master/wii_controller.py
# credit http://www.raspberrypi-spy.co.uk/?p=1101


# maybe check out
# why you might need pygame.event.pump() - http://stackoverflow.com/a/14900231
# pygame tutorial - https://lorenzod8n.wordpress.com/2007/05/25/pygame-tutorial-1-getting-started/
# slightly fancy threading class-based loop https://github.com/urbanzrim/ps3controller/blob/master/ps3controller.py


