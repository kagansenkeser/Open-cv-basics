import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def empty(a):
    pass
#we need this for creating trackbar
#track bar fonksiyonu için ihtiyacımz var


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",1000,350)
cv2.createTrackbar("hue min","TrackBars",0,255,empty)
cv2.createTrackbar("hue max","TrackBars",255,255,empty)
cv2.createTrackbar("sat min","TrackBars",0,255,empty)
cv2.createTrackbar("sat max","TrackBars",255,255,empty)
cv2.createTrackbar("val min","TrackBars",0,255,empty)
cv2.createTrackbar("val max","TrackBars",255,255,empty)
#creating track bars
#track bar yapıyoruz 6 adet 3 min 3 max için
while True:
    succes, img =cap.read()
    imgHSV =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #resmi hsv ye çeviriyoruz
    #turning rgb to hsv
    h_min =cv2.getTrackbarPos("hue min","TrackBars")
    h_max =cv2.getTrackbarPos("hue max","TrackBars")
    s_min =cv2.getTrackbarPos("sat min","TrackBars")
    s_max =cv2.getTrackbarPos("sat max","TrackBars")
    v_min =cv2.getTrackbarPos("val min","TrackBars")
    v_max =cv2.getTrackbarPos("val max","TrackBars")
    #trackbardan değeri okyuoruz
    #getting value from trackbar
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
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
