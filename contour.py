import cv2
import numpy as np

cap = cv2.VideoCapture(0)

webcam = False


def getcontours(img, cannytrash=[70, 70]):
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray, (25, 25), 1)
    imgcanny = cv2.Canny(imgblur, cannytrash[0], cannytrash[1])
    kernel = np.ones((5, 5))
    imgdial = cv2.dilate(imgcanny, kernel, iterations=3)
    imgthresh = cv2.erode(imgdial, kernel, iterations=2)
    cv2.imshow("imgthresh", imgthresh)

    # bize resmin dış hatları lazım o yüzden contour alıyoruz
    contours, hiearchy = cv2.findContours(imgthresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 1000:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.002 * peri, True)
            bbox = cv2.boundingRect(approx)
            cv2.drawContours(img, c, -1, (0, 255, 0), 15)

            l=max(contours,key=cv2.contourArea)
            x,y,w,h=cv2.boundingRect(l)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)

            solust=(x,y)
            solalt=(x,y+h)
            sagalt=(x+w,y+h)
            sagust=(x+w,y)
            cv2.circle(img,solalt,50,(255,0,0),4)
            cv2.circle(img,solust,50,(0,0,255),4)
            cv2.circle(img,sagalt,50,(255,0,255),4)
            cv2.circle(img,sagust,50,(0,255,0),4)

            #cv2.putText(img, str(solalt[1]-solust[1]), (int((x+w)/2-20),int((y+h)/2)), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0),5)
            #cv2.putText(img, str(sagalt[0]-solalt[0]), (int((x+w/2)),int((y+h))), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0),5)
            yukseklik=(solalt[1]-solust[1])
            genislik=(sagalt[0]-solalt[0])


            cv2.putText(img, "yukseklik :", (10,50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0),2)
            cv2.putText(img, str(yukseklik/2), (190,50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0),2)




            cv2.putText(img, "genislik   :", (10,80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0),2)
            cv2.putText(img, str(genislik/2), (190,80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0),2)



while True:
    succes, img = cap.read()
    getcontours(img)
    cv2.imshow("resim", img)
    cv2.waitKey(1)




