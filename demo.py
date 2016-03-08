'''
Author: Anjith George
IIT Kharagpur, 2016
anjith2006@gmail.com

'''

import glob
import numpy as np
import cv2
import video
import  pic2video # import the pic to video module



path='/home/lab//BioID/BioID-FaceDatabase-V1.2/'+"*.pgm"  #path to the folder containing the images (with the proper extension)

#cap=pic2video.cap(path)  # For reading images 

cap = cv2.VideoCapture(1) # For reading from the webcam



while True:
	
	
	
	ret, frame = cap.read() # Captures the next frame for camera/ next image in the list 
 
	if ret==True:
		
		frame=np.array(frame)
		cv2.imshow("Frame",frame)    
	kf = cv2.waitKey(1) 



