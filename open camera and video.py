import cv2
#adding library
#kütüphane eklemek
cap =cv2.VideoCapture(0)
#taking value from camera
#kameradan değer almak

while True:
    success,img=cap.read()
    #video aslında çokça fotoğrafın birleşmesidir bu yüzden loop içinde
    #video is actually combination of lots of video
    cv2.imshow("image",img)
    #resmi ekrana yazdırıyor  print ama opencv
    #print img on screen      print but on opencv
    cv2.waitKey(1)
    #resmi ekranda tutuyor ki görebilelim
    #holding image on screen so we can see the image 
