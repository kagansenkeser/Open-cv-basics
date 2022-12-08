import cv2
img=cv2.imread("dortgen.png")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, imggray=cv2.threshold(imggray,150,250,cv2.THRESH_BINARY)
ortax=0
ortay=0
x=0
imggray,contours,hierarchy=cv2.findContours(imggray,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
#retr comp hem iç hem dış her hierachy i versin diye
#appros none dememiz ise tüm noktlaraı versin önemli önemsiz
for cnt in  contours:
#contours da hepsi var tüm noktalar cnt hierarşiye göre ayrılıyor burda en dış hat ve
#şeklin öevresi olduğu için 2 hat var
    if hierarchy[0][0][3]==-1:
        #bizim istedimizin sonu eksi 1 o yüzden eksi birli olanı alıyoruz 0 0 3 dememiz ise birinci
        #kısmın birinci ölbümünün 4. sü
        #ilk başta dış hattı veriyor
        #sonrasında ikinci hattı bu yüzden ilk turda çizdirmeekek için altakı aşamaya girdim
        x=x+1
        if x==2:
            cv2.drawContours(img,cnt,-1,(255,0,0),30)
            print("bu sanırım x",x)
            for a in range(890):
                #range 890 kafama göre değil cnt uzunluğu kadar
                
                ortax=cnt[ a][0]+ortax
                #değeri alıp buna atıyoruz her turda bu sayede toplamını buluyoruz
                #890 nokta olduğu için 890a bölüyoruz   x de ve y de orta nokta
            ortay=ortax[1]/890
            ortax=ortax[0]/890
            ortax=int(ortax)
            ortay=int(ortay)
            cv2.circle(img,(ortax,ortay),60,(0,0,255),15)
            cv2.line(img,(ortax+100,ortay),(ortax+40,ortay),(0,255,0),10)
            cv2.line(img,(ortax-100,ortay),(ortax-40,ortay),(0,255,0),10)

            cv2.line(img,(ortax,ortay+100),(ortax,ortay+40),(0,255,0),10)
            cv2.line(img,(ortax,ortay-100),(ortax,ortay-40),(0,255,0),10)


        else:
            pass





print(img.shape)

cv2.imshow("img",img[0:720,250:660])

cv2.waitKey(0)


#sonradan düzenlenicek eksikleri mevcut
