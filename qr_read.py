import cv2
from pyzbar.pyzbar import decode
import numpy as np

cap = cv2.VideoCapture(1)
while True:
    succes, img = cap.read()
    code = decode(img)  # BU SATIR SİLİNEBİLİR
    for barcode in decode(img):
        mydata = barcode.data.decode("utf-8")
        print(mydata)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(0,255,0),5)
        pts2=barcode.rect
        cv2.putText(img,mydata,(pts2[0],pts2[1]-15),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,(0,165,255),2)
    cv2.imshow("resim", img)
    cv2.waitKey(1)

