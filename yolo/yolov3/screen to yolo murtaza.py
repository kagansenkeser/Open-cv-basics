from mss import mss
import cv2
from PIL import Image
import numpy as np
from time import time

mon = {'top': 180, 'left':950, 'width':800, 'height':460}
sct = mss()


wht=320
confThreshold=0.2
classesFile="coco.names"
classNames=[]
with open(classesFile,"rt") as f:
    classNames =f.read().rstrip("\n").split("\n")




#model değiştircem

#modelconfig="yolov3.cfg"
#modelweights="yolov3.weights"

modelconfig="yolov3-tiny.cfg"
modelweights="yolov3-tiny.weights"

net=cv2.dnn.readNetFromDarknet(modelconfig,modelweights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

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

    #bununla   konumlarnı direk al        print((bbox[1]))
    indices=cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nms_threshold=0.3)

    for i in indices:
        i=i[0]
        box=bbox[i]
        x,y,w,h=box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,f"{classNames[classIds[i]]}"
                        f" {int(confs[i]*100)}%",
        (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)


while True:
    begin_time = time()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    blob=cv2.dnn.blobFromImage(img_bgr,1/255,(wht,wht),[0,0,0],1,crop=False)
    net.setInput(blob)
    layerNames=net.getLayerNames()
    outputnames=[layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    outputs=net.forward(outputnames)
    findobjects(outputs,img_bgr)

    fps=int((1/(time() - begin_time)))



    cv2.putText(img_bgr,str(fps),(0,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    cv2.imshow('test', np.array(img_bgr))










    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
