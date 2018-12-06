import cv2
import numpy as np
import math
import time
import MySQLdb

def main():
	check1 = True
	check2 = False
	check3 = False
	check4 = False
	check5 = False
	check6 = False

	#Establish Database, josh fill in the login
	#db = MySQLdb.connect(host = "172.114.132.151", user = "will", passwd = "123", db = "parking", port = 3306)
	#cur = db.cursor()
		
	cap = cv2.VideoCapture(0)
	#Set the resolution to 720p, default was 480p
	cap.set(3, 1280)#Width
	cap.set(4, 720)#Height
	
	while(cap.isOpened()):
		ret, img = cap.read()
		
		#rectangle: width = 220, height = 300, gapX = 30, gapY = 40
		#make rectangle (image, bottom right xy, top left xy, color, thickness)
		#first row of rectangles:
		cv2.rectangle(img,(30,40),(250,340),(0,255,0),2)
		cv2.rectangle(img,(280,40),(500,340),(0,255,0),2)
		cv2.rectangle(img,(530,40),(750,340),(0,255,0),2)
	
		#second row of rectangles:
		cv2.rectangle(img,(530,380),(750,680),(0,255,0),2)
		cv2.rectangle(img,(780,380),(1000,680),(0,255,0),2)
		cv2.rectangle(img,(1030,380),(1250,680),(0,255,0),2)
		
		if check1 == True:
			crop_img1 = img[40:340, 30:250]
			#Convert image to gray scale
			grey = cv2.cvtColor(crop_img1, cv2.COLOR_BGR2GRAY)
			value = (11, 11)
			#Gaussian blur smooths out the pixilated image
			#Thresh_OTSU cleans up grainy noise from 'sandy' pixels
			blurred = cv2.GaussianBlur(grey, value, 0)
			cv2.imshow('blurred', blurred)
			#_, thresh1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			thresh1 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
				cv2.THRESH_BINARY_INV,11,2)
			cv2.imshow('thresh1', thresh1)
			(version, _, _) = cv2.__version__.split('.')
			#Counters are like the magic wand tool in photoshop. It traces the outline of a color.
			if version is '3':
				image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
					   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)        
			elif version is '2':
				contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
					   cv2.CHAIN_APPROX_NONE)
			cnt1 = max(contours, key = lambda x: cv2.contourArea(x))
			#bounding rectangle inscribes image (in this case found contour) in a rectangle. (Makes box around object)
			x1,y1,w1,h1 = cv2.boundingRect(cnt1)
			cv2.rectangle(crop_img1,(x1,y1),(x1+w1,y1+h1),(0,0,255),0)
			if (w1*h1) >= .3*(200*300):
				Ocf1 = True
			else:
				Ocf1 = False
			check1 = False
			check2 = True

		if check2 == True:
			crop_img2 = img[40:340, 280:500]
			grey = cv2.cvtColor(crop_img2, cv2.COLOR_BGR2GRAY)
			value = (11, 11)
			#Gaussian blur smooths out the pixilated image
			#Thresh_OTSU cleans up grainy noise from 'sandy' pixels
			blurred = cv2.GaussianBlur(grey, value, 0)
			#_, thresh2 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			thresh2 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
				cv2.THRESH_BINARY_INV,11,2)
			(version, _, _) = cv2.__version__.split('.')
			#Counters are like the magic wand tool in photoshop. It traces the outline of a color.
			if version is '3':
				image, contours, hierarchy = cv2.findContours(thresh2.copy(), \
					   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			elif version is '2':
				contours, hierarchy = cv2.findContours(thresh2.copy(),cv2.RETR_TREE, \
					   cv2.CHAIN_APPROX_NONE)
			cnt2 = max(contours, key = lambda x: cv2.contourArea(x))
			#bounding rectangle inscribes image (in this case found contour) in a rectangle. (Makes box around object)
			x2,y2,w2,h2 = cv2.boundingRect(cnt2)
			cv2.rectangle(crop_img2,(x2,y2),(x2+w2,y2+h2),(0,0,255),0)
			if (w2*h2) >= .3*(200*300):
				Ocf2 = True
			else:
				Ocf2 = False
			check2 = False
			check3 = True
			
		if check3 == True:
			crop_img3 = img[40:340, 530:750]
			grey = cv2.cvtColor(crop_img3, cv2.COLOR_BGR2GRAY)
			value = (11, 11)
			#Gaussian blur smooths out the pixilated image
			#Thresh_OTSU cleans up grainy noise from 'sandy' pixels
			blurred = cv2.GaussianBlur(grey, value, 0)
			#_, thresh3 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			thresh3 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
				cv2.THRESH_BINARY_INV,11,2)
			(version, _, _) = cv2.__version__.split('.')
			#Counters are like the magic wand tool in photoshop. It traces the outline of a color.
			if version is '3':
				image, contours, hierarchy = cv2.findContours(thresh3.copy(), \
					   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			elif version is '2':
				contours, hierarchy = cv2.findContours(thresh3.copy(),cv2.RETR_TREE, \
					   cv2.CHAIN_APPROX_NONE)
			cnt3 = max(contours, key = lambda x: cv2.contourArea(x))
			#bounding rectangle inscribes image (in this case found contour) in a rectangle. (Makes box around object)
			x2,y2,w2,h2 = cv2.boundingRect(cnt3)
			cv2.rectangle(crop_img3,(x2,y2),(x2+w2,y2+h2),(0,0,255),0)
			if (w2*h2) >= .3*(200*300):
				Ocf3 = True
			else:
				Ocf3 = False
			check3 = False
			check4 = True
			
		if check4 == True:
			crop_img4 = img[380:680, 530:750]
			grey = cv2.cvtColor(crop_img4, cv2.COLOR_BGR2GRAY)
			value = (11, 11)
			#Gaussian blur smooths out the pixilated image
			#Thresh_OTSU cleans up grainy noise from 'sandy' pixels
			blurred = cv2.GaussianBlur(grey, value, 0)
			#_, thresh4 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			thresh4 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
				cv2.THRESH_BINARY_INV,11,2)
			(version, _, _) = cv2.__version__.split('.')
			#Counters are like the magic wand tool in photoshop. It traces the outline of a color.
			if version is '3':
				image, contours, hierarchy = cv2.findContours(thresh4.copy(), \
					   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			elif version is '2':
				contours, hierarchy = cv2.findContours(thresh4.copy(),cv2.RETR_TREE, \
					   cv2.CHAIN_APPROX_NONE)
			cnt4 = max(contours, key = lambda x: cv2.contourArea(x))
			#bounding rectangle inscribes image (in this case found contour) in a rectangle. (Makes box around object)
			x2,y2,w2,h2 = cv2.boundingRect(cnt4)
			cv2.rectangle(crop_img4,(x2,y2),(x2+w2,y2+h2),(0,0,255),0)
			if (w2*h2) >= .3*(200*300):
				Ocf4 = True
			else:
				Ocf4 = False
			check4 = False
			check5 = True
		
		if check5 == True:
			crop_img5 = img[380:680, 780:1000]
			grey = cv2.cvtColor(crop_img5, cv2.COLOR_BGR2GRAY)
			value = (11, 11)
			#Gaussian blur smooths out the pixilated image
			#Thresh_OTSU cleans up grainy noise from 'sandy' pixels
			blurred = cv2.GaussianBlur(grey, value, 0)
			#_, thresh5 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			thresh5 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
				cv2.THRESH_BINARY_INV,11,2)
			(version, _, _) = cv2.__version__.split('.')
			#Counters are like the magic wand tool in photoshop. It traces the outline of a color.
			if version is '3':
				image, contours, hierarchy = cv2.findContours(thresh5.copy(), \
					   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			elif version is '2':
				contours, hierarchy = cv2.findContours(thresh5.copy(),cv2.RETR_TREE, \
					   cv2.CHAIN_APPROX_NONE)
			cnt5 = max(contours, key = lambda x: cv2.contourArea(x))
			#bounding rectangle inscribes image (in this case found contour) in a rectangle. (Makes box around object)
			x2,y2,w2,h2 = cv2.boundingRect(cnt5)
			cv2.rectangle(crop_img5,(x2,y2),(x2+w2,y2+h2),(0,0,255),0)
			if (w2*h2) >= .3*(200*300):
				Ocf5 = True
			else:
				Ocf5 = False
			check5 = False
			check6 = True
		
		if check6 == True:
			crop_img6 = img[380:680, 1030:1250]
			grey = cv2.cvtColor(crop_img6, cv2.COLOR_BGR2GRAY)
			value = (11, 11)
			#Gaussian blur smooths out the pixilated image
			#Thresh_OTSU cleans up grainy noise from 'sandy' pixels
			blurred = cv2.GaussianBlur(grey, value, 0)
			#_, thresh6 = cv2.threshold(blurred, 127, 255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
			thresh6 = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
				cv2.THRESH_BINARY_INV,11,2)
			(version, _, _) = cv2.__version__.split('.')
			#Counters are like the magic wand tool in photoshop. It traces the outline of a color.
			if version is '3':
				image, contours, hierarchy = cv2.findContours(thresh6.copy(), \
					   cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
			elif version is '2':
				contours, hierarchy = cv2.findContours(thresh6.copy(),cv2.RETR_TREE, \
					   cv2.CHAIN_APPROX_NONE)
			cnt6 = max(contours, key = lambda x: cv2.contourArea(x))
			#bounding rectangle inscribes image (in this case found contour) in a rectangle. (Makes box around object)
			x2,y2,w2,h2 = cv2.boundingRect(cnt6)
			cv2.rectangle(crop_img6,(x2,y2),(x2+w2,y2+h2),(0,0,255),0)
			if (w2*h2) >= .3*(200*300):
				Ocf6 = True
			else:
				Ocf6 = False
			check6 = False
			check1 = True

		str = "Spot1"
		cv2.putText(img, str, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
		str = "Spot2"
		cv2.putText(img, str, (280,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
		str = "Spot3"
		cv2.putText(img, str, (530,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
		str = "Spot4"
		cv2.putText(img, str, (530,710), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,255,0),2)
		str = "Spot5"
		cv2.putText(img, str, (780,710), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,255,0),2)
		str = "Spot6"
		cv2.putText(img, str, (1030,710), cv2.FONT_HERSHEY_SIMPLEX,  1, (0,255,0),2)
		
		if Ocf1 == True:
			str = "Occupied"
			cv2.putText(img, str, (65,190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
			#Josh this is where you Specify database tables and such
			occupySpot1 = ("UPDATE spots SET taken = 'closed' where spot_id = '1'")
			#cur.execute(occupySpot1)
		else:
			str = "Open"
			cv2.putText(img, str, (100,190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
			occupySpot1 = ("UPDATE spots SET taken = 'open' where spot_id = '1'")
			#cur.execute(occupySpot1)
			
		if Ocf2 == True:
			str = "Occupied"
			cv2.putText(img, str, (315,190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
			occupySpot2 = ("UPDATE spots SET taken = 'closed' where spot_id = '2'")
			#cur.execute(occupySpot2)
		else:
			str = "Open"
			cv2.putText(img, str, (350,190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
			occupySpot2 = ("UPDATE spots SET taken = 'open' where spot_id = '2'")
			#cur.execute(occupySpot2)
			
		if Ocf3 == True:
			str = "Occupied"
			cv2.putText(img, str, (565,190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
			occupySpot3 = ("UPDATE spots SET taken = 'closed' where spot_id = '3'")
			#cur.execute(occupySpot3)
		else:
			str = "Open"
			cv2.putText(img, str, (600,190), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
			occupySpot3 = ("UPDATE spots SET taken = 'open' where spot_id = '3'")
			#cur.execute(occupySpot3)
			
		if Ocf4 == True:
			str = "Occupied"
			cv2.putText(img, str, (565,530), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
			occupySpot4 = ("UPDATE spots SET taken = 'closed' where spot_id = '4'")
			#cur.execute(occupySpot4)
		else:
			str = "Open"
			cv2.putText(img, str, (600,530), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
			occupySpot4 = ("UPDATE spots SET taken = 'open' where spot_id = '4'")
			#cur.execute(occupySpot4)
			
		if Ocf5 == True:
			str = "Occupied"
			cv2.putText(img, str, (815,530), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
			occupySpot5 = ("UPDATE spots SET taken = 'closed' where spot_id = '5'")
			#cur.execute(occupySpot5)
		else:
			str = "Open"
			cv2.putText(img, str, (850,530), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
			occupySpot5 = ("UPDATE spots SET taken = 'open' where spot_id = '5'")
			#cur.execute(occupySpot5)
			
		if Ocf6 == True:
			str = "Occupied"
			cv2.putText(img, str, (1065,530), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
			occupySpot6 = ("UPDATE spots SET taken = 'closed' where spot_id = '6'")
			#cur.execute(occupySpot6)
		else:
			str = "Open"
			cv2.putText(img, str, (1100,530), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
			occupySpot6= ("UPDATE spots SET taken = 'open' where spot_id = '6'")
			#cur.execute(occupySpot6)
			
	
		#Transfrom cropped images into an array
		drawing1 = np.zeros(crop_img1.shape,np.uint8)
		drawing2 = np.zeros(crop_img2.shape,np.uint8)
		drawing3 = np.zeros(crop_img3.shape,np.uint8)
		drawing4 = np.zeros(crop_img4.shape,np.uint8)
		drawing5 = np.zeros(crop_img5.shape,np.uint8)
		drawing6 = np.zeros(crop_img6.shape,np.uint8)
		
		cv2.drawContours(drawing1,[cnt1],0,(0,255,0),0)
		cv2.drawContours(drawing2,[cnt2],0,(0,255,0),0)
		cv2.drawContours(drawing3,[cnt3],0,(0,255,0),0)
		cv2.drawContours(drawing4,[cnt4],0,(0,255,0),0)
		cv2.drawContours(drawing5,[cnt5],0,(0,255,0),0)
		cv2.drawContours(drawing6,[cnt6],0,(0,255,0),0)

		cv2.imshow('Gesture', img)
		#Combine arrays into one image
		all_img1 = np.hstack((drawing1, crop_img1))
		all_img2 = np.hstack((drawing2, crop_img2))
		all_img3 = np.hstack((drawing3, crop_img3))
		all_img4 = np.hstack((drawing4, crop_img4))
		all_img5 = np.hstack((drawing5, crop_img5))
		all_img6 = np.hstack((drawing6, crop_img6))
		#cv2.imshow('Contours1', all_img1)
		#cv2.imshow('Contours2', all_img2)
		#cv2.imshow('Contours3', all_img3)
		#cv2.imshow('Contours4', all_img4)
		#cv2.imshow('Contours5', all_img5)
		#cv2.imshow('Contours6', all_img6)
		k = cv2.waitKey(10)
		if k == 27:
			break
		#time.sleep(5)
#cur.close
#db.close
	cap.release()
	cv2.destroyAllWindows()
main()
