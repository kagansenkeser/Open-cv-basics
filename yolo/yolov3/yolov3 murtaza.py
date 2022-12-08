import cv2
import numpy as np
import time
cap=cv2.VideoCapture(0)
wht=320
confThreshold=0.5
classesFile="coco.names"
classNames=[]
with open(classesFile,"rt") as f:
    classNames =f.read().rstrip("\n").split("\n")
#clasların adını alıyoruz bu şekilde



pTime = 0
#previous time
cTime = 0
#current time

#model değiştircem

modelconfig="yolov3.cfg"
modelweights="yolov3.weights"

#modelconfig="yolov3-tiny.cfg"
#modelweights="yolov3-tiny.weights"

#tiny güzel ama doruluk gidiyor
#eğer güçlüyse işlemcin normal yolo daha iyi

net=cv2.dnn.readNetFromDarknet(modelconfig,modelweights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
#bu kısmı açıklamıyor



def findobjects(outputs,img):
    ht,wt,ct=img.shape
    bbox       =[]
    classIds   =[]
    confs      =[]

    for output in outputs:
        for det in output:
            #ilk 5 klas dışında kalanların en yükseğini buluyoruz ki hangisi oldunu anlayalım
            scores=det[5:]
            classId=np.argmax(scores)
            confidence=scores[classId]
            if confidence>confThreshold:
                #oranı 100 de 50 den yüksekse kaydediyoruz
                w,h=int(det[2]*wt),int(det[3]*ht)
                #pixel deger olarka alıyoruz bu sayede
                x,y=int(det[0]*wt-w/2),int(det[1]*ht-h/2)
                bbox.append([x,y,w,h])
                classIds.append((classId))
                confs.append(float(confidence))

    print(len(bbox))
    indices=cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nms_threshold=0.3)
    #çok kutulamayı kesiyor aynı yere fazla kutu koyma durumu

    for i in indices:
        i=i[0]
        box=bbox[i]
        x,y,w,h=box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,f"{classNames[classIds[i]]}"
                        f" {int(confs[i]*100)}%",
        (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)


while True:
    succes,img=cap.read()
    #net normal resim almıyo sadece blob alıyo
    blob=cv2.dnn.blobFromImage(img,1/255,(wht,wht),[0,0,0],1,crop=False)
    net.setInput(blob)

    layerNames=net.getLayerNames()
    #layerlerin ad listesi
    #print( net.getUnconnectedOutLayers())
    #bunu kullandımızda bize sayı olarak veriyor ama bize adı lazım
    outputnames=[layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]

    outputs=net.forward(outputnames)
    #direk aldık değerleri şimdi
  #  print(outputs[0].shape)
    #300 kutu  #85 in sebebi   1xkonum  2ykonum 3genişlik 4uzunluk 5obje var mı kalan 80 her klasın oranı

  #  print(outputs[1].shape)
    #1200 kutu
#    print(outputs[2].shape)
    #4800 kutu
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    findobjects(outputs,img)
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 255), 5)
    cv2.imshow("img",img)
    cv2.waitKey(1)
