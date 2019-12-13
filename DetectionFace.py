import cv2
import numpy as np
import datetime
from RPi import  GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
cap= cv2.VideoCapture(0)
#cap.set(3,480)
#cap.set(4,480)
#eyes_cascade = cv2.CascadeClassifier('face_detection/parojosG.xml')
face_cascade = cv2.CascadeClassifier('face_detection\\haarcascade_frontalface_alt.xml')
#noise_cascade = cv2.CascadeClassifier('face_detection/Mouth.xml')
while cap.isOpened():
    frame = cap.read()[1]#cv2.imread('my_class.jpg',1)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(frame_gray)
    #eyes = eyes_cascade.detectMultiScale(frame_gray)
    if len(faces)==0:
        GPIO.output(12,True)
        print("False")
    else:
        GPIO.output(12,False)
        print('True')
    date_time = str(datetime.datetime.now())[:19]
    cv2.putText(frame, date_time,(10,10),cv2.FONT_HERSHEY_COMPLEX,.5,(0,255,255),1,cv2.LINE_4)
    #noise = noise_cascade.detectMultiScale(frame_gray)
    for (x,y,width,height) in faces:
        cv2.rectangle(frame,(x,y),(x+width, y+height),(0,255,0),2)
    #for x,y,height,width in eyes:
        #cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) == ord('b'):
        break
cap.release()
cv2.destroyAllWindows()


