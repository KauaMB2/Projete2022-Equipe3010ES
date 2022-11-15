import cv2
import numpy as np
import tkinter as tk
from tkinter import *
import os
dir_path=os.path.dirname(__file__)
def TirarFotos():
    nome_funcionario = inputName.get()

    if nome_funcionario == "":
        labelRetorno = Label(janela, text="Digite o nome do funcionário!")
        labelRetorno.pack(side=TOP)
        labelRetorno["fg"] = "red"
        return

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    haarcascade_face = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
    haarcascade_olho = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")

    amostra = 1

    numeroAmostras = 300

    largura, altura = 220, 220
    while True:
        _, video = camera.read()

        detectar_face = haarcascade_face.detectMultiScale(video, scaleFactor=1.5, minSize=(100, 100))
        imagemCinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        if not os.path.exists(f'fotos/{nome_funcionario}'):
            os.makedirs(f'fotos/{nome_funcionario}')
        for(x, y, w, z) in detectar_face:
            cv2.rectangle(video, (x, w), (x + w, y + z), (255, 0, 0), 2)

            regiao = video[y:y + z, x:x + w]
            regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)

            olhosDetectados = haarcascade_olho.detectMultiScale(regiaoCinzaOlho)

            for(ox, oy, ol, oa) in olhosDetectados:
                cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

                if(np.average(imagemCinza)) > 100:

                    imagemFace = cv2.resize(imagemCinza[y:y + z, x:x + w], (largura, altura))   
                    dirr=f"fotos/{nome_funcionario}/{amostra}.jpg"
                    print(dirr)
                    cv2.imwrite(dirr, imagemFace)

                    print("foto " + str(amostra) + " capturada com sucesso!")
                    amostra += 1

        cv2.imshow("Video", video)

        if cv2.waitKey(1) == ord("q"):
            break

        if(amostra >= numeroAmostras + 1):
            break

    print("Imagens da face capturadas com sucesso!")

    camera.release()

    cv2.destroyAllWindows()

janela = tk.Tk()
janela.geometry("600x600+100+100")

labelTitle = Label(janela, text="Cadastro Facial", font=("calibri 25"))
labelTitle.pack(side=TOP)

labelName = Label(janela, text="Digite o nome do funcionário: ", font=("calibri 12"))
labelName.pack(side=TOP)

inputName = Entry(janela, width=40)
inputName.pack(side=TOP)

buttonRegister = Button(janela, text="Tirar Fotos", width=20, command=TirarFotos)
buttonRegister.pack(side=TOP)
buttonRegister["bg"] = "green"
buttonRegister["fg"] = "white"

janela.mainloop()