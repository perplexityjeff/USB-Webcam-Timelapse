# USB Webcam Timelapse

This python script (webcam.py) creates timelapse videos using usb webcam images. 

## Usage 
The usage of the script is as follows:

    $ ./webcam.py 10 4h webcamImages 0 1920 1080

- 10 is the interval between images in seconds.

- 4h is the time to keep recording. You can use d, h, m, or s for days, hours, minutes and seconds respectively.

- webcamImages is the name of the folder the images will be saved in. It will be created in the current working directory, determined by `os.getcwd()`

- 0 is the camera port of the connected usb webcam. If you do this on a laptop 0 will mostly likely be the built-in camera. Try and test to see what number works for you.

- 1920 and 1080 are part of the camera's resolution. You can use it to take smaller pictures if you prefer.

## Requirements
[opencv-python](https://pypi.org/project/opencv-python/) is required for this script to run as it is used to connect to your webcam. 

## Credits
This project is a modified version of [mbjd's WebcamTimelapse](https://github.com/mbjd/WebcamTimelapse). I used it as a base as it was perfect for my purpose with a few modifications. 

