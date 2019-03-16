import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('myVideo3.avi',cv2.VideoWriter_fourcc(*'XVID'),20,(width,height))
while True:
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
writer.release()
cap.release()
cv2.destroyAllWindows()