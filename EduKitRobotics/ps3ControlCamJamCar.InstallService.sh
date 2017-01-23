#!/bin/bash

### ps3ControlCamJamCar.InstallService.sh: Install PS3 Controller service for CamJam Edukit 3 Robotics on Raspberry Pi ###

## author:  ArtMG
## contact: https://github.com/artmg/MuGammaPi/blob/master/EduKitRobotics/ps3ControlCamJamCar.InstallService.sh
## status:  Production

# For more on this see the accompanying article https://github.com/artmg/MuGammaPi/wiki/CamJam-Robotics-Kit

# Simply paste this code onto the command line to install the python script as a service



# set up Unit file
sudo tee /etc/systemd/system/ps3ControlCamJamCar.service >/dev/null <<'EOF!'
[Unit]
Description=ps3ControlCamJamCar
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/sudo /usr/bin/python3 /home/pi/EduKitRobotics/ps3ControlCamJamCar.py

[Install]
WantedBy=multi-user.target
EOF!

#...with correct permissions
sudo chmod 644 /etc/systemd/system/ps3ControlCamJamCar.service

# then register it with systemd
sudo systemctl daemon-reload
sudo systemctl enable ps3ControlCamJamCar.service

# now reboot to test
sudo reboot

# to test whether the service is running...
# sudo systemctl status ps3ControlCamJamCar.service
