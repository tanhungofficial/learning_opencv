import  cv2 as cv
import numpy as np

def click_event(event, x, y,flag, parma):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print("Location: ",x,"x",y,sep='')
        font = cv.FONT_HERSHEY_COMPLEX
        text = str(x) +'-'+str(y)
        cv.putText(img,text,(x,y),font,1,(255,255,255),1,cv.LINE_AA)
        cv.imshow("Image", img)
    if event == cv.EVENT_RBUTTONDBLCLK:
        print('Color: ', img[x,y,:])
        b,g,r =int(img[x,y,0]), int(img[x,y,1]), int(img[x,y,2])
        cv.rectangle(img,(x,y),(x+50,y+50),(b,g,r),-1)
        cv.imshow("Image", img)
    if event ==cv.EVENT_LBUTTONDOWN:
        point.append((x,y))
        b, g, r = int(img[x, y, 0]), int(img[x, y, 1]), int(img[x, y, 2])
        cv.circle(img,point[0],3,(255,255,255),-1)
        if len(point) >=2:
            cv.line(img,point[-2],point[-1],(255,255,255),3)
            print(point)
        cv.imshow("Image",img)


point =[]
img = cv.imread("ma_dan_chua_yeu.jpg",-1)
x=10
y=10
event=np.array([i for i in dir(cv) if "EVENT" in i]).reshape(18,1)
print(event)
cv.imshow("Image",img)
cv.setMouseCallback("Image", click_event)
cv.waitKey(0)
cv.destroyAllWindows()
