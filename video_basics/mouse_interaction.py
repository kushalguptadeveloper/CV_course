import cv2

# event function
def draw_rect(event,x,y,flags,params):
    global pt1,pt2,topLeft_clicked,botRight_clicked
    if event==cv2.EVENT_LBUTTONDOWN:
        #reset
        if topLeft_clicked and botRight_clicked:
            pt1=(0,0)
            pt2=(0,0)
            topLeft_clicked = False
            botRight_clicked = False
        if topLeft_clicked == False:
            pt1=(x,y)
            topLeft_clicked=True
        elif botRight_clicked==False:
            pt2=(x,y)
            botRight_clicked=True 
# global variables
pt1=(0,0)
pt2=(0,0)
topLeft_clicked = False
botRight_clicked = False

# connecting window
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rect)

while True:
    ret,frame = cap.read()
    
    if topLeft_clicked:
        cv2.circle(frame,pt1,5,(0,0,255),3)
    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,255,0),3)
    
    cv2.imshow('Test',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()