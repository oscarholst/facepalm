# facepalm
Proof of concept

Background: The optional bluetooth proximity lock in Windows is a good idea but not good enough.

Idea: Run as a background process every minute or so. If no face is detected within 15 seconds of run. Activate built-in screenlock.
This script assumes that the webcam being used is listed as /dev/video4 in my case, yours will most likely differ.

This has only been tested on a machine running Ubuntu 23.10, with a Logitech C922 Pro Stream Webcam and running python version 3.

Also, the standard nerd like myself is not the ones in need of a utility like this. Will most likely be beneficial running on a Windows machine for the average business user.

This does not do any facial recognition, anyone in front of the webcam will keep the computer unlocked with this poc.

Also a potential issue is obviously if the webcam used is already in use by another program/videochat etc, it will most likely not work as intended.

But again, this was just a crazy idea.

#### License
BSD 3-Clause License
