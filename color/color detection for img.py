import cv2
import numpy as np
def empty(a):
    pass
#task bar yaparken lazım

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 750, 350)
#önemsiz gibi duruyo ama taskbar penceresi boyutu
cv2.createTrackbar("Hue Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
#task barları yarattık
while True:
    img = cv2.imread("milinx.jpg")
    img=cv2.resize(img,(400,400))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #resmi rgb den hsv çevirdik
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    #trackbardan değer aldık
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    #aldığımız değerleri  yazıdrdık
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    #maske yaparken dizi olarak istiyo üç elemanlı o yüzden arraye çevirioyruz
    mask = cv2.inRange(imgHSV, lower, upper)
    #limit koyuyor mask limiti bu diye
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    #resme maskeyi basıyoruz
    #fonksiyon birleştirme fonksiyonu resme maskeyi ekliyor direk bu şekilde rengi tespit edebiliyoruz
    cv2.imshow("img", img)
    cv2.imshow("imgHSV", imgHSV)
    cv2.imshow("mask", mask)
    cv2.imshow("imgResult", imgResult)

    cv2.waitKey(1)
