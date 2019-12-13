import cv2
import numpy as np

#img = cv2.imread('lena.jpg', -1)
img= np.zeros((512,512),np.uint8)
#img =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image",img)
img= cv2.rectangle(img,(512,0),(462,50),(255,0,255),-1)
img  = cv2.circle(img,(255,255),128,(0,0,255),-1)
img = cv2.line(img, (0,0), (img.shape[0],img.shape[1]),(59, 231, 237),8)
img = cv2.arrowedLine(img, (0,255), (255,255),(59, 231, 237),8)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"OpenCV",(10,100),font,1,(255,255,0),-1,cv2.LINE_AA)
cv2.imshow("Lena.jgp", img)
cv2.waitKey(0)
cv2.destroyAllWindows()