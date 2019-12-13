import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("lena.jpg",1)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5))/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
median = cv2.medianBlur(img,5)
gblur = cv2.GaussianBlur(img,(5,5),0)
bilateral = cv2.bilateralFilter(img,9,75,75)

images =[img, dst,blur,gblur, median, bilateral]
titles = ["Original","2D convalution",'Blurring', "Gaussian Bluer", "Median Blur", 'Bilateral']
for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    cv2.imshow(titles[i],images[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()