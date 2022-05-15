
from picamera import Picamera
import subprocess
import time

cmd = "raspistill - t 30000 - tl 2000 - o image % 04 d.jpg - w 720 - h 480"
subprocess.call(cmd, shell=True)
print("Done")

#add naming the pictures and assigning to folders labeled Journey 1, 2, ...
#call nivi's image processing code afterwards
orbit_number = 0
orbit_type= 10 #"high resolution"
for orbit_number in range(11):
    #orbit_type = 10  # "high resolution"
    print(orbit_type)
    if orbit_number % 2 == 0: #orbit number is even
        # #toggle orbit type
        if orbit_type== 10:
            orbit_type = 0 #switch it
            #print("print low resolution picture")
            print(orbit_type)
            time.sleep(5)
            raspistill -t 30000 -tl 2000 -o image%04d.jpg -w 720 -h 480
        else:
            orbit_type == 10 #switch it
			#Monitor the cubesat’s current latitude/longitude coordinates
			#When the current coordinates is a member of the list of lat/long coordinates received from ground station
			raspistill -t 30000 -tl 2000 -o image%04d.jpg -w 1920 -h 1080
            #print ("print high resolution picture")
            print(orbit_type)
            time.sleep(5)
    else: #orbit number is odd
		#consider what orbit_type is currently equal to.
        if orbit_type == 0:
			raspistill -t 30000 -tl 2000 -o image%04d.jpg -w 720 -h 480
            #print ("print low resolution picture")
            print(orbit_type)
            time.sleep(5)
        else: #If (orbit_type == high resolution):
			#Monitor the cubesat’s current latitude/longitude coordinates
			#When the current coordinates is a member of the list of lat/long coordinates received from ground station,
			raspistill -t 30000 -tl 2000 -o image%04d.jpg -w 1920 -h 1080
            #print ("print high resolution picture")
            print(orbit_type)
            time.sleep(5)
    orbit_number = orbit_number +1
'''
from picamera import Picamera

camera = PiCamera()
camera.resolution = (1280, 720)
camera.vflip = True
camera.contrast = 10
time.sleep(2)
file_name = "<directory name>/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)
print("Done.")
'''