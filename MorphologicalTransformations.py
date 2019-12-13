import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
def nothing(z):
    pass
cv2.namedWindow("Customize")
cv2.createTrackbar("Iteration","Customize",0,40,nothing)

img = cv2.imread("smarties.png",0)
_, mask= cv2.threshold(img,200,255,cv2.THRESH_BINARY)
kernel = np.ones([2,2],dtype=np.uint8)
while True:
    iteration = cv2.getTrackbarPos("Iteration", "Customize")
    dilation = cv2.dilate(mask, kernel, iterations=iteration)
    erosion = cv2.erode(mask, kernel, iterations=iteration)
    titles = ["Original", "Mask", "Dilation", 'Erosion']
    images = [img, mask, dilation, erosion]
    for i in range(len(images)):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], "gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    if cv2.waitKey(100)==ord("b"):
        break
