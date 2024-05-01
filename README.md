# USB Webcam Timelapse

This python script (webcam.py) creates timelapse videos using webcam images. Usage is as follows:

    $ ./webcam.py 10 4h webcamImages 0

where:

- 10 is the interval between images in seconds.

- 4h is the time to keep recording. You can use d, h, m, or s for days, hours, minutes and seconds respectively.

- webcamImages is the name of the folder the images will be saved in. It will be created in the current working directory, determined by `os.getcwd()`

- 0 is the camera port of the connected usb webcam. If you do this on a laptop 0 will mostly likely be the built-in camera. 

# Credits
This project is a modified version of https://github.com/mbjd/WebcamTimelapse. I used it as a base as it was perfect for my purpose with a few modifications. 
