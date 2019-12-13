import  cv2
import  numpy as np

def function(x):
    x=x
img =cv2.imread("smarties.png",1)
cv2.namedWindow("Image")

cv2.createTrackbar("Width","Image",0,img.shape[0]-1,function)
cv2.createTrackbar("Height","Image",0,img.shape[1]-1,function)
cv2.createTrackbar("BGR/GRAY","Image",0,1,function)
while True:
    key= cv2.waitKey(1)&0xff
    if key== ord("b"):
        break
    img_temp = img.copy()
    x = cv2.getTrackbarPos("Width","Image")
    y= cv2.getTrackbarPos("Height", "Image")
    color= cv2.getTrackbarPos("BGR/GRAY", 'Image')
    cv2.circle(img_temp, (x,y),5,(0,0,255),-1)
    if color==1:
        print("Color: ", img_temp[x, y,:])
        cv2.imshow("Image", img_temp)
    else:
        img_gray= cv2.cvtColor(img_temp,cv2.COLOR_BGR2GRAY)
        print("Color: ", img_gray[x, y])
        cv2.imshow("Image", img_gray)

cv2.destroyAllWindows()