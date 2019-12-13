import  cv2
import numpy as np
import matplotlib.pyplot as plt
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
apple_orange = np.hstack((apple[:,:256],orange[:,256:]))
n=6
gp_apple =[apple.copy()]
for i in range(n):
    gp_apple.append(cv2.pyrDown(gp_apple[-1]))
print(len(gp_apple))
gp_orange = [orange.copy()]
for i in range(n):
    gp_orange.append(cv2.pyrDown(gp_orange[-1]))
print(len(gp_orange))
lp_apple = [gp_apple[-1].copy()]
for i in range(n,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = np.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)
print(len(lp_apple))
lp_orange = [gp_orange[-1].copy()]
for i in range(n,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = np.subtract(gp_orange[i-1],gaussian_expanded)
    lp_orange.append(laplacian)
print(len(lp_orange))
apple_orange_pyramid=[]
for i in range(len(lp_apple)):
    apple_lp   = lp_apple[i]
    orange_lp  = lp_orange[i]
    laplacian= np.hstack((apple_lp[:,0:int(apple_lp.shape[0]/2)], orange_lp[:,int(orange_lp.shape[0]/2):]))
    apple_orange_pyramid.append(laplacian)
print(apple_orange_pyramid[-1].shape)
apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,n+1,1):
    apple_orange_reconstruct= cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct= cv2.add(apple_orange_reconstruct, apple_orange_pyramid[i])
print(apple_orange_reconstruct.shape)
cv2.imshow(" Apple Orange Reconstruct", apple_orange_reconstruct)
cv2.imshow("Apple Orange", apple_orange)
cv2.imshow("Apple",apple)
cv2.imshow("Orange", orange)
cv2.waitKey(0)
cv2.destroyAllWindows()