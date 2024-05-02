#!/usr/bin/env python

import time
import sys
import os
import cv2 
import datetime

print(" _   _ ____  ____     __        __   _                             _____ _                _                       ")
print("| | | / ___|| __ )    \ \      / /__| |__   ___ __ _ _ __ ___     |_   _(_)_ __ ___   ___| | __ _ _ __  ___  ___  ")
print("| | | \___ \|  _ \ ____\ \ /\ / / _ \ '_ \ / __/ _` | '_ ` _ \ _____| | | | '_ ` _ \ / _ \ |/ _` | '_ \/ __|/ _ \ ")
print("| |_| |___) | |_) |_____\ V  V /  __/ |_) | (_| (_| | | | | | |_____| | | | | | | | |  __/ | (_| | |_) \__ \  __/ ")
print(" \___/|____/|____/       \_/\_/ \___|_.__/ \___\__,_|_| |_| |_|     |_| |_|_| |_| |_|\___|_|\__,_| .__/|___/\___| ")           
print("                                                                                                 |_|              ")
print("")
print("A script based on the work of mbjd's WebcamTimelapse on GitHub, modified to work with USB camera's by perplexityjeff")
print("https://github.com/perplexityjeff/USB-Webcam-Timelapse")
print("")

# Process arguments
print("Process arguments")
period = float(sys.argv[1])
folder = str(sys.argv[3])
cam_port = str(sys.argv[4])
cam_width = int(sys.argv[5])
cam_height = int(sys.argv[6])
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
print("Setting directory parameters")
homeDirectory = os.getcwd()
absPath = homeDirectory + '/' + folder
if not os.path.exists(folder):
    os.makedirs(folder)

# Webcam stuff
print("Setting camera parameters")
vid = cv2.VideoCapture(cam_port)
#forces MJPG, this will be an option in the future maybe
#vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
vid.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

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
print("Starting the timelapse")
while currentTime < endTime:
    currentTime = time.time()

    if currentTime >= nextTime:
        nextTime += period

        named_tuple = time.localtime()
        time_string = time.strftime("%Y-%m-%d-%H%M%S", named_tuple)
        timeStr = '{0}.jpg'.format(time_string)
        getCameraImage(folder, timeStr)

    # Sleep 0.1 seconds to make sure nothing is missed
    # Also you can set the interval to something like 0.3 secs
    time.sleep(0.1)
