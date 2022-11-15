import cv2 as cv 
import os

haar_cascade=cv.CascadeClassifier(r'cascades\haarcascade_frontalface_default.xml')
people=os.listdir("fotos")#Coloca o nome de todos as pastas dentro da pasta "fotos" em uma lista#features=np.load('features.npy')
faceReconizer=cv.face.LBPHFaceRecognizer_create()
faceReconizer.read(r'classificadores\faceTrained.yml')

camera = cv.VideoCapture(0, cv.CAP_DSHOW)

while camera.isOpened():
    status, frame=camera.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('person',gray)
    facesRect=haar_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in facesRect:
        facesRoi=gray[y:y+h,x:x+h]
        label, confidence=faceReconizer.predict(facesRoi)
        print(f'Label={people[label]} with a confidence of {confidence}')
        cv.putText(frame,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    key=cv.waitKey(1)#ESC = 27
    if key==27:#Se apertou o ESC
        break
    cv.imshow("Camera", frame)
cv.destroyAllWindows()