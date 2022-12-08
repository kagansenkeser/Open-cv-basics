import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    succes, img =cap.read()
    imgHSV =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


    lower = np.array([0,0,0])
    upper = np.array([10,255,255])
    mask=cv2.inRange(imgHSV,lower,upper)
    #creating mask
    #maske oluşturuyoruz
    result =cv2.bitwise_and(img,img,mask=mask)
    #resmin üzerine maskeyi eklliyoruz
    #puting mask on img
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    cv2.imshow("img",img)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
