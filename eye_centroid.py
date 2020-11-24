import cv2
import numpy as np

cap = cv2.VideoCapture("D:\\TeleMed\\daniel-ir\\daniel-ir.mkv")

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


'''def contours_method(gray, frame):
	 # _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

	 # contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	 # # print(contours)
	 # contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

	 # for cnt in contours:
	 # 	(x, y, w, h) = cv2.boundingRect(cnt)
	 # 	#cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 3)
	 # 	cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
	 cv2.imshow("Thresholded", threshold)

	 return frame


def hough_method(gray, frame):

	 gray = cv2.medianBlur(gray, 3)
	 # circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,800, param1=200,param2=9,minRadius=70,maxRadius=100)
	 # if circles is None:
	 # 	cv2.imshow('detected circles1',frame)
	 # 	continue
	 # circles = np.uint16(np.around(circles))
	 # for i in circles[0,:]:
	 # 	cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
	 # 	cv2.circle(frame,(i[0],i[1]),3,(0,0,255),1
	 return frame'''


def find_eye(coords, gray, frame):

	delta = 20
	gray_roi = gray[coords[1]:coords[3]
	    , coords[0]:coords[2]]

	if len(gray_roi) == 0:
		return frame

	circles = cv2.HoughCircles(gray_roi, cv2.HOUGH_GRADIENT, 1,
	                            800, param1=200, param2=9, minRadius=70, maxRadius=100)
	if circles is None:
	 return frame
	 
	circles = np.uint16(np.around(circles))
	for i in circles[0, :]:
	 cv2.circle(frame, (i[0]+coords[0], i[1]+coords[1]), i[2], (0, 255, 0), 2)
	 cv2.circle(frame, (i[0]+coords[0], i[1]+coords[1]), 3, (0, 0, 255), 1)


	cv2.imshow("Eyes", gray_roi)
	return frame


def haarcascade_method(gray, frame):
	eyes=eye_cascade.detectMultiScale(
	    gray, 1.3, 5, minSize=(100, 100), maxSize=(300, 300))

	for (x, y, w, h) in eyes:
		cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (0, 225, 255), 2)
		coords=(x-20, y-20, x+w+20, y+h+20)

		final_frame=find_eye(coords, gray, frame)

	return frame

frame_no=1
while True:
	 ret, frame=cap.read()

	 if not ret:
	 	break


	 gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	 frame=haarcascade_method(gray, frame)


	 if not ret:
	 	print("Frame not recieved")
	 	break



	 cv2.putText(frame, "Frame count : " + str(frame_no), (20, 40),
	             cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 255), 2, cv2.LINE_AA)

	 key = cv2.waitKey(1) & 0xff


	 if key == ord('p'):
	 	while True:
	 		key2 = cv2.waitKey(1) or 0xff
	 		
	 		if key2 == ord('p'):
	 			break

	 # if key == 27: 
	 # 	break



	 cv2.imshow('detected circles1', frame)




	 if cv2.waitKey(1) & 0xFF == ord('q'):
	 	break
	 frame_no += 1

cap.release()
cv2.destroyAllWindows()
