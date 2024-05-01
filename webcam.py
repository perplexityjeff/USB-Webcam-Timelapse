#!/usr/bin/env python

import time
import sys
import os
import cv2 
import datetime

# Process arguments
period = float(sys.argv[1])
folder = str(sys.argv[3])
cam_port = str(sys.argv[4])
cam_width = str(sys.argv[5])
cam_height = str(sys.argv[6])
duration = int(sys.argv[2][:-1])

# Convert duration of recording to seconds
if sys.argv[2].endswith("d"):
    endTime = time.time() + 24 * 60 * 60 * duration
elif sys.argv[2].endswith("h"):
    endTime = time.time() + 60 * 60 * duration
elif sys.argv[2].endswith("m"):
    endTime = time.time() + 60 * duration
elif sys.argv[2].endswith("s"):
    endTime = time.time() + duration
else:
    print("Invalid argument: sys.argv[2] must be an integer + 'd', 'h', 'm' or 's'")

# Directory stuff
homeDirectory = os.getcwd()
absPath = homeDirectory + '/' + folder

# Webcam stuff
vid = cv2.VideoCapture(cam_port)
vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
vid.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

if not os.path.exists(folder):
    os.makedirs(folder)

# Saving of webcam image
def getCameraImage(dir, name):   
    result, image = vid.read() 
    if result: 
        cv2.imwrite(os.path.join(dir, name), image) 
        print('Saved image: ' + folder + '/' + name)

# Timing
nextTime = time.time()
currentTime = time.time()

# Get the images for as long as specified
while currentTime < endTime:
    currentTime = time.time()

    if currentTime >= nextTime:
        nextTime += period

        named_tuple = time.localtime()
        time_string = time.strftime("%Y-%m-%d-%H%M%S", named_tuple)
        timeStr = '{0}.jpg'.format(time_string)

        now = datetime.datetime.now()
        if now.hour >= 7 and now.hour < 18:
            getCameraImage(folder, timeStr)
        else:
            print("Skipped image")

    # Sleep 0.1 seconds to make sure nothing is missed
    # Also you can set the interval to something like 0.3 secs
    time.sleep(0.1)
