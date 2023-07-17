import cv2
import time
cap=cv2.VideoCapture
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
while True:
    img=cap.read(0)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    succes, img = cap.read()
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 5)
    cv2.imshow("resim", img)
    cv2.waitKey(1)
