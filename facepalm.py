# Copyright (c) 2024, Oscar Holst
# This work is licensed under the terms of the BSD 3-Clause license.  
# https://github.com/oscarholst/facepalm/
# Disclaimer: Use at your own risk! It's only a simple PoC!

import cv2
import dlib
import time
import os

# Open video source
cap = cv2.VideoCapture(4)

# Initialize the HOG face detector from the dlib library
hog_face_detector = dlib.get_frontal_face_detector()

start_time = time.time()
face_detected = False

while True:
    # If 15 seconds have passed, exit the loop
    if time.time() - start_time > 15:
        break

    # Read a frame from the video source
    ret, frame = cap.read()

    # If the frame was not read correctly, exit the loop
    if not ret:
        break

    # Use the face detector to detect faces in the frame
    faces = hog_face_detector(frame, 1)

    # If any faces were detected, print a message and draw a rectangle around each face
    if len(faces) > 0:
        print("Face detected!")
        face_detected = True
        break

# Release the video source when you're done
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

# If no face was detected in 15 seconds, lock the screen
if not face_detected:
    os.system('xdg-screensaver lock')