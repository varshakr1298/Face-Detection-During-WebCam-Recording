import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascades1/haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()                        # Reading the Frame
	faces = face_cascade.detectMultiScale(frame,1.3,5)
	for (x,y,w,h) in faces:
		cv2.putText(frame,'Face',(x,y), font, 1,(0,0,255),2)
		cv2.rectangle(frame,(x,y),((x + w),(y + h)),(255,0,0),3)    
	cv2.imshow('result', frame)
	if cv2.waitKey(33) == 27:
		break;
cap.release()
cv2.destroyAllWindows()
