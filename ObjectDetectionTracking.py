import cv2
import numpy as np
cap= cv2.VideoCapture(0)
cap.set(3,360)
cap.set(4,360)

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("Upper H", "Tracking",255,255,nothing)
cv2.createTrackbar("Upper S", "Tracking",255,255,nothing)
cv2.createTrackbar("Upper V", "Tracking",255,255,nothing)

cv2.createTrackbar("Lower H", "Tracking",0,255,nothing)
cv2.createTrackbar("Lower S", "Tracking",0,255,nothing)
cv2.createTrackbar("Lower V", "Tracking",0,255,nothing)
while cap.isOpened():
    if ord("b")== cv2.waitKey(1):
        break
    ret, img_bgr = cap.read()
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    upper_H = cv2.getTrackbarPos("Upper H", "Tracking")
    lower_H = cv2.getTrackbarPos("Lower H", "Tracking")

    upper_S = cv2.getTrackbarPos("Upper S", "Tracking")
    lower_S = cv2.getTrackbarPos("Lower S", "Tracking")

    upper_V = cv2.getTrackbarPos("Upper V", "Tracking")
    lower_V = cv2.getTrackbarPos("Lower V", "Tracking")

    upper = np.array([upper_H,upper_S,upper_V])
    lower = np.array([lower_H,lower_S,lower_V])
    mask = cv2.inRange(img_hsv,lower,upper)
    res= cv2.bitwise_and(img_bgr,img_bgr,mask=mask)
    cv2.imshow("BGR", img_bgr)
    #cv2.imshow("HSV", img_hsv)
    cv2.imshow("res", res)
    cv2.imshow("Tracking", mask)

cap.release()
cv2.destroyAllWindows()
