'''
Author: Anjith George
IIT Kharagpur, 2016
anjith2006@gmail.com

'''

import cv2
import glob

class cap(object):
	
	def __init__(self,path):
		self.path=path
		self.file_list=glob.glob(path)
		self.count=0
		self.length=len(self.file_list)
		
		
	def read(self):
		self.count=self.count+1
		if self.count<self.length:
			image_name=self.file_list[self.count]
			img=cv2.imread(image_name) 
			return True,img
		else:
			return False,[]
		
		
		
	   
	   
		
	
