import cv2
import mediapipe as mp
import time

cap =cv2.VideoCapture(0)
mpHands =mp.solutions.hands
hands = mpHands.Hands()
mpDraw= mp.solutions.drawing_utils

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                if id ==4:
                #her noktanın kendine has kodu var bu bize 4 nolu noktanın kodunu veriyor
                #each point has differnt code 4 is giving us thummb's head
                    cv2.circle(img,(cx,cy),25,(255,255,255),cv2.FILLED)

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    cv2.imshow("image",img)
    cv2.waitKey(1)
