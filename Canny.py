#Импорт нужных библиотек
import cv2
import numpy as np

#Загружаем видео
cap = cv2.VideoCapture('speed_car_slowww.mp4')

#Считываем кадры видео и делаем преобразование Кэнни
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.Canny(frame,100,200)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
