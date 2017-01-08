#!/usr/bin/env python

"""Ps3ControlCamJamCar.py: Control CamJam Edukit 3 Robotics on Raspberry Pi with PS3 Controller over Bluetooth."""

__author__ = "ArtMG"
__contact__ = "https://github.com/artmg/MuGammaPi/blob/master/Ps3ControlCamJamCar.py"
__status__ = "Production"

# For more on this see the accompanying article https://github.com/artmg/MuGammaPi/wiki/CamJam-Robotics-Kit

import RPi.GPIO as GPIO # GPIO output
import os 				# shutdown
import pygame 			# PS3 input


# section credit - http://www.instructables.com/id/Remote-Raspberry-Pi-Robot-PS3-Controller-Fablab-Ne/?ALLSTEPS
# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()


# section credit https://github.com/CamJam-EduKit/EduKit3/blob/master/Code/4-driving.py

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


## SWAP THESE PAIRS DEPENDING on your wiring

# Set variables for the GPIO motor pins
pinMotorRightForwards = 10
pinMotorRightBackwards = 9

pinMotorLeftForwards = 8
pinMotorLeftBackwards = 7


# Set the GPIO Pin mode
GPIO.setup(pinMotorLeftForwards, GPIO.OUT)
GPIO.setup(pinMotorLeftBackwards, GPIO.OUT)
GPIO.setup(pinMotorRightForwards, GPIO.OUT)
GPIO.setup(pinMotorRightBackwards, GPIO.OUT)

# Set all motors off
GPIO.output(pinMotorLeftForwards, 0)
GPIO.output(pinMotorLeftBackwards, 0)
GPIO.output(pinMotorRightForwards, 0)
GPIO.output(pinMotorRightBackwards, 0)


# credit - https://www.raspberrypi.org/forums/viewtopic.php?t=130201&p=869560
os.putenv('DISPLAY', ':0.0') 
pygame.display.init()
# however this now forces you to **run as root** with sudo


# section shared credit - https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=163814
# section shared credit - http://www.instructables.com/id/Remote-Raspberry-Pi-Robot-PS3-Controller-Fablab-Ne/?ALLSTEPS

# Only start the motors when the inputs go above the following threshold
threshold = 0.60

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
              if (LeftTrack > threshold):
                  GPIO.output(pinMotorLeftForwards, 1)
                  GPIO.output(pinMotorLeftBackwards, 0)
              # Move BACKWARDS
              elif (LeftTrack < -threshold):
                  GPIO.output(pinMotorLeftForwards, 0)
                  GPIO.output(pinMotorLeftBackwards, 1)
              # Otherwise stop
              else:
                  GPIO.output(pinMotorLeftForwards, 0)
                  GPIO.output(pinMotorLeftBackwards, 0)

              # And do the same for the RIGHT motor
              # Move FORWARDS
              if (RightTrack > threshold):
                  GPIO.output(pinMotorRightForwards, 1)
                  GPIO.output(pinMotorRightBackwards, 0)
              # Move BACKWARDS
              elif (RightTrack < -threshold):
                  GPIO.output(pinMotorRightForwards, 0)
                  GPIO.output(pinMotorRightBackwards, 1)
              # Stopping
              else:
                  GPIO.output(pinMotorRightForwards, 0)
                  GPIO.output(pinMotorRightBackwards, 0)



except KeyboardInterrupt:
    # Turn off the motors
    GPIO.output(pinMotorLeftForwards, 0)
    GPIO.output(pinMotorLeftBackwards, 0)
    GPIO.output(pinMotorRightForwards, 0)
    GPIO.output(pinMotorRightBackwards, 0)
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


