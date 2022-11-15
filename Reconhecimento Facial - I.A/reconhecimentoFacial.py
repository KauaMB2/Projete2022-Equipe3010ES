import cv2 as cv
import os
DIR=os.path.dirname(__file__)#Encontra a localização do arquivo no PC
DIR=DIR+r'\fotosTeste\4.jpeg'
haar_cascade=cv.CascadeClassifier(r'cascades\haarcascade_frontalface_default.xml')

people=os.listdir("fotos")#Coloca o nome de todos as pastas dentro da pasta "fotos" em uma lista#features=np.load('features.npy')
#labels=np.load('labels.npy')
faceReconizer=cv.face.LBPHFaceRecognizer_create()
faceReconizer.read(r'classificadores\faceTrained.yml')

img=cv.imread(DIR)
cv.imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

facesRect=haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in facesRect:
    facesRoi=gray[y:y+h,x:x+h]
    label, confidence=faceReconizer.predict(facesRoi)
    print(f'Label={people[label]} with a confidence of {confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('Detected Face',img)
cv.waitKey(0)