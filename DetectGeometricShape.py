import cv2
import numpy as np
import matplotlib.pyplot as plt
imgBGR = cv2.imread('shape.jpg',1)
imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(imgGray, 240,255,cv2.THRESH_BINARY)[1]
mask= np.ones((5,5), dtype=np.uint8)
median = cv2.medianBlur(thresh,7)
dilation = cv2.dilate(median,mask,iterations=5)
cv2.imshow("Thresholding", dilation)
contours = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)[0]
cv2.drawContours(imgBGR, contours, -1,(0,255,0),1)
cv2.imshow("Image", imgBGR)
cv2.imshow("Gray", imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()