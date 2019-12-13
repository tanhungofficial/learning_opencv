import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("messi5.jpg",0)
images =[img,lap,sobelX,sobelY, sobelXY]
titles = ["Original", 'Laplacian','Sobel X', 'Sobel Y', "Sobel Combine"]
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