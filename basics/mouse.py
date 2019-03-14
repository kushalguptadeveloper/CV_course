import numpy as np
import cv2

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    
cv2.namedWindow(winname='myDrawing')
cv2.setMouseCallback('myDrawing',draw_circle)


img = np.zeros((512,512,3),dtype=np.int8)

while True:
    cv2.imshow('myDrawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()