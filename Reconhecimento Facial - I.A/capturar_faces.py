import cv2
import numpy as np

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

haarcascade_face = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
haarcascade_olho = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")

largura, altura = 220, 220

print("Capturando as faces...")

while True:
    _, video = camera.read()

    detectar_face = haarcascade_face.detectMultiScale(video, scaleFactor=1.5, minSize=(100, 100))
    imagemCinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)

    for(x, y, w, z) in detectar_face:
        cv2.rectangle(video, (x, w), (x + w, y + z), (255, 0, 0), 2)

        regiao = video[y:y + z, x:x + w]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)

        olhosDetectados = haarcascade_olho.detectMultiScale(regiaoCinzaOlho)

        for(ox, oy, ol, oa) in olhosDetectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

            if cv2.waitKey(1) == ord("s"):

                if(np.average(imagemCinza)) > 100:

                    imagemFace = cv2.resize(imagemCinza[y:y + z, x:x + w], (largura, altura))   


    cv2.imshow("Video", video)

    if cv2.waitKey(1) == ord("q"):
        break

print("Imagens da face capturadas com sucesso!")

camera.release()

cv2.destroyAllWindows