import cv2 as cv
import os
import numpy as np
features=[]
labels=[]
def createTrain():
    people=os.listdir("fotos")#Coloca o nome de todos as pastas dentro da pasta "fotos" em uma lista
    DIR=os.path.dirname(__file__) #Encontra a localização do arquivo no PC
    DIR=DIR+r'\fotos'
    haar_cascade=cv.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        for img in os.listdir(path):#O método listdir() retorna uma lista contendo os nomes das entradas no diretório fornecido por path
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            facesRect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in facesRect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)#Adiciona a imagem dentro de uma lista 
                labels.append(label)#Armazena algum valor numérico que representará as pastas das imagens percorridas dentro dos arquivos
                print(f'label = {label}')
                print(f'faces_roi = {faces_roi}')
    return
createTrain()
print(f'features = {features}')
print(f'labels = {labels}')
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

features=np.array(features,dtype='object')
labels=np.array(labels)
faceReconizer=cv.face.LBPHFaceRecognizer_create()

#Treinando o reconhecedor facial usando a lista 'features'(Recursos) e a lista 'labels'(Rótulos)
faceReconizer.train(features,labels)
faceReconizer.save('classificadores\faceTrained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
