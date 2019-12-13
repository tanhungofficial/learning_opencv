import cv2
import numpy as np
import matplotlib.pyplot as plt

imgBGR =  cv2.imread("opencv-logo.png",1)
imgGray= cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
threshold = cv2.threshold(imgGray,150,255,cv2.THRESH_BINARY_INV)[1]
contours, hierarchy= cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgBGR,contours,-1,(100,55,50),2,cv2.LINE_AA)
cv2.imshow("Thresholding", threshold)
cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image BGR", imgBGR)
print("Number of contours: ",len(contours))
cv2.waitKey(0)
cv2.destroyAllWindows()