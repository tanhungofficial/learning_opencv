import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.png",0)
lap= cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap= np.uint8(np.absolute(lap))
sobelX= cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY= cv2.Sobel(img, cv2.CV_64F,0,1)
sobelX= np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelXY= np.bitwise_or(sobelX,sobelY)
canny= cv2.Canny(img,0,50)
images = [img,lap ,sobelX ,sobelY, sobelXY,canny]
titles = ["Original", 'Laplacian','Sobel X', 'Sobel Y', "Sobel Combine", "Canny"]
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    cv2.imshow(titles[i],images[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()