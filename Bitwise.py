import cv2
import numpy as np

img1 = np.zeros((250,500,3))
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = np.zeros((250,500,3))
img2[:,250:500,:]=[255,255,255]
cv2.imshow("Image 1", img1)
cv2.waitKey(0)
cv2.imshow("Image 2", img2)
cv2.waitKey(0)
bitAnd= cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitXor= cv2.bitwise_xor(img1,img2)
bitNot = cv2.bitwise_not(img2)
cv2.imshow("Image",bitNot)
cv2.waitKey(0)
cv2.destroyAllWindows()