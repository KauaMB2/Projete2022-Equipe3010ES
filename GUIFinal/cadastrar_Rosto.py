import serial
import cv2 as cv
import numpy as np
import os

dir_path=os.path.dirname(__file__)
people=os.listdir("fotos")#Coloca o nome de todos as pastas dentro da pasta "fotos" em uma lista
DIR=os.path.dirname(__file__) #Encontra a localização do arquivo no PC
features=[]
labels=[]
DIR=DIR+r'\fotos'
haar_cascade=cv.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
print(DIR)
def createTrain():
    global features,labels
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
    return

def cadastrar(nome_funcionario):
    camera = cv.VideoCapture(0, cv.CAP_DSHOW)
    haarcascade_face = cv.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
    haarcascade_olho = cv.CascadeClassifier("cascades/haarcascade_eye.xml")
    amostra = 1
    numeroAmostras = 300
    largura, altura = 220, 220
    while True:
        _, video = camera.read()
        detectar_face = haarcascade_face.detectMultiScale(video, scaleFactor=1.5, minSize=(100, 100))
        imagemCinza = cv.cvtColor(video, cv.COLOR_BGR2GRAY)
        if not os.path.exists(f'fotos/{nome_funcionario}'):
            os.makedirs(f'fotos/{nome_funcionario}')
        for(x, y, w, z) in detectar_face:
            cv.rectangle(video, (x, w), (x + w, y + z), (255, 0, 0), 2)

            regiao = video[y:y + z, x:x + w]
            regiaoCinzaOlho = cv.cvtColor(regiao, cv.COLOR_BGR2GRAY)

            olhosDetectados = haarcascade_olho.detectMultiScale(regiaoCinzaOlho)

            for(ox, oy, ol, oa) in olhosDetectados:
                cv.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

                if(np.average(imagemCinza)) > 100:

                    imagemFace = cv.resize(imagemCinza[y:y + z, x:x + w], (largura, altura))   
                    dirr=f"fotos/{nome_funcionario}/{amostra}.jpg"
                    print(dirr)
                    cv.imwrite(dirr, imagemFace)

                    print("foto " + str(amostra) + " capturada com sucesso!")
                    amostra += 1

        cv.imshow("Video", video)

        if cv.waitKey(1) == ord("q"):
            break

        if(amostra >= numeroAmostras + 1):
            break

    print("Imagens da face capturadas com sucesso!")

    camera.release()

    cv.destroyAllWindows()
