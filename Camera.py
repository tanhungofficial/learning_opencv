import  cv2
import numpy as np
import  datetime

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Original resolution: ", width,"x",height,sep="")
cap.set(3,640)
cap.set(4,480)
print("Changed Resolution: ",cap.get(3),"x",cap.get(4),sep="")
font = cv2.FONT_HERSHEY_COMPLEX
text = "Resolution: "+ str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+"x"+ str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
     ret, frame = cap.read()
     date_time = str(datetime.datetime.now())[:22]
     if ret == True:
         frame = cv2.putText(frame,text,(10,25),font,1,(0,255,255),1,cv2.LINE_AA)
         frame= cv2.putText(frame,date_time,(10,55),font,1,(0,255,255),1,cv2.LINE_AA)
         cv2.imshow("From your camera", frame)
         if cv2.waitKey(1)& 0xff == ord("b"):
             break
     else:
         break
cap.release()
cv2.destroyAllWindows()