#!/usr/bin/env python


import RPi.GPIO as GPIO # GPIO output
import os 				# shutdown
import pygame 			# PS3 input


# credit - http://www.instructables.com/id/Remote-Raspberry-Pi-Robot-PS3-Controller-Fablab-Ne/?ALLSTEPS

# Initialise the pygame library
pygame.init()

# Connect to the first JoyStick
j = pygame.joystick.Joystick(0)
j.init()


print 'Initialized Joystick : %s' % j.get_name()


# credit https://github.com/CamJam-EduKit/EduKit3/blob/master/Code/4-driving.py

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set all motors off
GPIO.output(pinMotorAForwards, 0)
GPIO.output(pinMotorABackwards, 0)
GPIO.output(pinMotorBForwards, 0)
GPIO.output(pinMotorBBackwards, 0)


# credit - http://www.instructables.com/id/Remote-Raspberry-Pi-Robot-PS3-Controller-Fablab-Ne/?ALLSTEPS

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

              # Check how to configure the left motor

              # Move forwards
              if (RightTrack > threshold):
				  GPIO.output(pinMotorBForwards, 1)
				  GPIO.output(pinMotorBBackwards, 0)
              # Move backwards
              elif (RightTrack < -threshold):
				  GPIO.output(pinMotorBForwards, 0)
				  GPIO.output(pinMotorBBackwards, 1)
              # Stopping
              else:
				  GPIO.output(pinMotorBForwards, 0)
				  GPIO.output(pinMotorBBackwards, 0)

              # And do the same for the right motor
              if (LeftTrack > threshold):
				  GPIO.output(pinMotorAForwards, 1)
				  GPIO.output(pinMotorABackwards, 0)
              # Move backwards
              elif (LeftTrack < -threshold):
				  GPIO.output(pinMotorAForwards, 0)
				  GPIO.output(pinMotorABackwards, 1)
              # Otherwise stop
              else:
				  GPIO.output(pinMotorAForwards, 0)
				  GPIO.output(pinMotorABackwards, 0)


except KeyboardInterrupt:
    # Turn off the motors
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 0)
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


