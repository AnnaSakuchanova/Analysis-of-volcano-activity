import cv2
import numpy as np

cap = cv2.VideoCapture('speed_car_slowww.mp4')

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('vid5.avi',fourcc, 30.0, (1280,720), False)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.Canny(frame,100,200)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
