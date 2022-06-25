import cv2
#importing library
#kütüphane elkeme
img = cv2.imread("hutao.png")# hutao.png is my path your path can like be C:\Users\kagan\Desktop
#reading file location
#dosya konumunu okuma
cv2.imshow('image', img)
#showing the image
#resmi gösterme
cv2.waitKey(0)
#to wait image on the screen
#resmi ekranda bekletmek için
