import cv2
import numpy as np

def nothing():
    pass

cv2.namedWindow("Customize")
cv2.createTrackbar("Thresholding","Customize",0,255,nothing)
cv2.createTrackbar("Value","Customize",255,255,nothing)
img = cv2.imread("gradient.jpg", 0)
cv2.imshow("Customize", img)
while True:
    thresh = cv2.getTrackbarPos("Thresholding","Customize")
    value = cv2.getTrackbarPos("Value",'Customize')
    _,th_binary= cv2.threshold(img,thresh,value,cv2.THRESH_BINARY)
    _,th_binary_inv=cv2.threshold(img,thresh,value,cv2.THRESH_BINARY_INV)
    #duoi thresh giu nguyen, tren threh = thresh
    _,th_trunc = cv2.threshold(img, thresh,value, cv2.THRESH_TRUNC)
    #duoi thresh =0, tren thresh giu nguyen , tozero_onv nguoc lai
    _, th_tozero = cv2.threshold(img, thresh, value, cv2.THRESH_TOZERO_INV)
    cv2.imshow("Thresholding tozero", th_tozero)
    cv2.imshow("Thresholding trunc", th_trunc)
    cv2.imshow("Thresholding binary", th_binary)
    cv2.imshow("Thresholding binary invert", th_binary_inv)
    print(_)
    if cv2.waitKey(100)== ord('b'):
        break

cv2.destroyAllWindows()