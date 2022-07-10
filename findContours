import cv2
import numpy as np

cap = cv2.imread('35989872.jpg')
gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY)
contorurs, hierarc = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cap_copy = cap.copy()
cv2.drawContours(cap_copy,contorurs, -1, (0,255,0),2,cv2.LINE_AA)
cv2.imshow('simple conturs', cap_copy)
cv2.waitKey(0)
cap_copy2 = cap_copy.copy()
height, width, channels = cap_copy2.shape
for i, contour in enumerate(contorurs):
    for j,contour_point in enumerate(contour):
        cv2.circle(cap_copy2,((contour_point[0][0],contour_point[0][1])),2,(0,255,0),2, cv2.LINE_AA)
cv2.imshow('countours_', cap_copy2)
cv2.waitKey(0)

#cv2.imwrite('countours.ipg',cap_copy2)
cv2.destroyAllWindows()
