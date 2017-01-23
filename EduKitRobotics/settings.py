#!/usr/bin/env python

"""setting.py: variables to customise extra code for CamJam Edukit 3 Robotics on Raspberry Pi."""

__author__ = "ArtMG"
__contact__ = "https://github.com/artmg/MuGammaPi/blob/master/EduKitRobotics/settings.py"
__status__ = "Production"

# For more on this see the accompanying article https://github.com/artmg/MuGammaPi/wiki/CamJam-Robotics-Kit

# Set variables for the GPIO motor pins
### SWAP THESE PAIRS DEPENDING on your wiring ###
pinMotorLeftForwards = 7
pinMotorLeftBackwards = 8

pinMotorRightForwards = 9
pinMotorRightBackwards = 10

# Set variables for proprotional control
# How long the pin stays on each cycle, as a percent
### ADJUST THESE VALUES TO COMPENSATE FOR ANY SPEED DIFFERENCE BETWEEN THE MOTORS
### e.g. leave one at MAXIMUM 100 (%) and reduce the other
DutyCycleLeft = 100
DutyCycleRight = 100

# How many times to turn the pin on and off each second
Frequency = 20

# Only start the motors when the inputs go above the following threshold
inputThreshold = 0.60
