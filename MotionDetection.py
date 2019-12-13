import cv2
import numpy as np
import matplotlib.pyplot as plt
def nothing(x):
    pass

cap= cv2.VideoCapture("vtest.avi")
cv2.namedWindow("Inter")
cv2.createTrackbar("Thresholding","Inter",50,255,nothing)
cv2.createTrackbar("Area min","Inter",500,1000,nothing)
cv2.createTrackbar("Area max","Inter",2000,2000,nothing)
frame1= cap.read()[1]
frame2= cap.read()[1]
kernel = np.ones((2,2),dtype=np.uint8)
while cap.isOpened():
    frame_Diff= cv2.absdiff(frame1,frame2)
    cv2.imshow('Frame diff', frame_Diff)
    frame_Diff_Gray= cv2.cvtColor(frame_Diff, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame diff gray', frame_Diff_Gray)
    frame_Diff_Gray_Blur = cv2.GaussianBlur(frame_Diff_Gray,(5,5),1)
    cv2.imshow("Frame diff gray blur", frame_Diff_Gray_Blur)
    #frame_Diff_Gray_Blur= cv2.Canny(frame_Diff_Gray_Blur,50,50)
    th = cv2.getTrackbarPos("Thresholding","Inter")
    thresh = cv2.threshold(frame_Diff_Gray_Blur,th,255,cv2.THRESH_BINARY)[1]
    cv2.imshow("Thresholding", thresh)
    dilated = cv2.dilate(thresh,None, iterations=3)
    cv2.imshow("Dilation", dilated)
    contours = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
    frame=frame1.copy()
    min= cv2.getTrackbarPos("Area min","Inter")
    max= cv2.getTrackbarPos("Area max","Inter")
    for contour in contours:
        x,y,w,h= cv2.boundingRect(contour)
        if min<cv2.contourArea(contour) <max:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Motion Detection",(20,20),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.imshow("Inter", frame1)
    frame2= frame
    frame1 = cap.read()[1]
    if cv2.waitKey(50)== ord("b"):
        break

cap.release()
cv2.destroyAllWindows()