# Copyright (c) 2024, Oscar Holst
# This work is licensed under the terms of the BSD 3-Clause license.  
# https://github.com/oscarholst/facepalm/
# Disclaimer: Use at your own risk! It's only a simple PoC!

import cv2
import dlib
import time
import os
import shutil
import time

# Try to detect all possible webcams
available_cameras = []
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap is None or not cap.isOpened():
        cap.release()
    else:
        available_cameras.append(i)
        cap.release()

# If no camera is detected, exit the program
if not available_cameras:
    print("No camera detected.")
    exit(1)

camera_index = None

# Test each camera
for index in available_cameras:
    cap = cv2.VideoCapture(index)
    hog_face_detector = dlib.get_frontal_face_detector()

    face_detected = False
    for _ in range(10):  # Read 10 frames
        ret, frame = cap.read()
        if not ret:
            continue

        faces = hog_face_detector(frame, 1)
        if len(faces) > 0:
            face_detected = True
            camera_index = index
            break

    cap.release()

    if face_detected:
        break

if camera_index is None:
    print("No camera detected a face.")
    exit(1)

while True:  # Infinite loop
    # Open the chosen video source
    cap = cv2.VideoCapture(camera_index)

    # Initialize the HOG face detector from the dlib library
    hog_face_detector = dlib.get_frontal_face_detector()

    start_time = time.time()
    face_detected = False

    print("Start face detection...")  # Print message when face detection starts

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
        if shutil.which('xdg-screensaver'):
            os.system('xdg-screensaver lock')
        elif shutil.which('gnome-screensaver-command'):
            os.system('gnome-screensaver-command -l')
        else:
            print("No known screen lock command found.")

    # Wait for 60 seconds before checking the camera again
    time.sleep(60)