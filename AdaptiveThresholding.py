import cv2 as cv

def nothing(x):
    pass

img = cv.imread("sudoku.png",0)
cv.namedWindow("Customize")
cv.createTrackbar("Max value", "Customize",255,255,nothing)
cv.createTrackbar("Block", "Customize",1,100,nothing)
cv.createTrackbar("C", "Customize",0,30,nothing)
cv.setTrackbarMin("Block", "Customize",1)
cv.imshow('Customize', img)
while True:
    max_value = cv.getTrackbarPos("Max value", "Customize")
    block = cv.getTrackbarPos("Block", "Customize")*2 +1
    c= cv.getTrackbarPos("C", "Customize")
    adpt_th_mean_c = cv.adaptiveThreshold(img,max_value,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,block,c)
    adpt_th_gaussian_c = cv.adaptiveThreshold(img,max_value,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,block,c)
    cv.imshow("Adaptive tresholding mean c", adpt_th_mean_c)
    cv.imshow("Adaptive thresholding gaussian c",adpt_th_gaussian_c)
    if cv.waitKey(100) == ord('b'):
        break
cv.waitKey(0)
cv.destroyAllWindows()

