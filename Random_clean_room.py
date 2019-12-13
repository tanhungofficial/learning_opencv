import cv2
import numpy as np
work =['Lavabo','Nha tam','Toilet','Nen nha ve sinh','Qet mang nhen','Cua so','Khu vuc cua vao']
img = np.zeros((100,300))
cv2.imshow("image", img)
print("\n\nHello, press <SPACE> to choose your working!")
print("------------------------------------------------------------")
print("Con lai %d viec:"%np.size(work), work)
while True:
    index = int(np.random.randint(0,np.size(work) ,[1,1]))
    if cv2.waitKey(200)== ord(' '):
        print(index)
        print("Cong viec cua ban: ", work[index].upper())
        print("------------------------------------------------------------")
        work.pop(index)
        if np.size(work)==0:
            print("Da chia cong viec xong!")
            break
cv2.destroyAllWindows()