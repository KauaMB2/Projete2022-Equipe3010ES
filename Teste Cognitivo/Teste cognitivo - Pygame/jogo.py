import pygame
from pygame.locals import *
from sys import exit
from random import randint
from cronometro import setInterval
from cronometro import clearInterval
indiceAcertos=0
pygame.init()#Inicia pygames
somAcerto=pygame.mixer.Sound('som/acerto.wav')#Cria objeto para som acerto
somErro=pygame.mixer.Sound('som/errado.wav')#Cria objeto para som erro
altura=650#Altura da tela
largura=950#Largura da tela
pontos=0#Variável de pontos
fonte1=pygame.font.SysFont('arial', 40, bold=True, italic=True)#Define fonte para texto
fonte2=pygame.font.SysFont('arial', 32, True, False)
relogio=pygame.time.Clock()#Define objeto referente ao tempo de atualizaçao do game
tela=pygame.display.set_mode((largura, altura))#Define tamanho da tela
pygame.display.set_caption('CEPEG')#Define nome do jogo
logo=pygame.image.load('img/logoCEPEG.png')#Cria objeto para a imagemLogo
tela.fill((0,0,180))#Cor de fundo da tela
pygame.draw.rect(tela,(100,100,255),(0,0,largura,80))#Desenha retangulo
#pygame.draw.rect(nomeTela,(R,G,B),(posX,posY,tamX,tamY)) -> Desenha retangulo na tela
tela.blit(logo,(10, 15))# Coloca a logo na tela
div1=pygame.image.load('img/div.png')#Carrega um objeto para imagem
div2=pygame.image.load('img/div.png')#Carrega um objeto para imagem
randomFormato=None
randomCor=None
randomDiv=None
jogo=False
inicio=True
final=False
acertos=0
erros=0
segundos=60
acertarImg=False
acertarCor=False
acertarDiv=False
varCronometro=None
def telaInicio():
    global inicio
    while(inicio==True):
        fonte2=pygame.font.SysFont('arial', 32, True, False)
        mensagem="Clique em qualquer tecla para iniciar, você tem 60 segundos. Boa sorte!!"
        texto_formatado=fonte2.render(mensagem, False, (255,255,255))
        retTexto=texto_formatado.get_rect()
        imgInicio=pygame.image.load('img/imgInicio.png')#Carrega um objeto para imagem
        imgInicio=pygame.transform.scale(imgInicio, [560, 380])#Define um tamanho para a imgInicio
        tela.blit(imgInicio,(160, 90))#Coloca imagem na tela
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                inicio=False
        retTexto.center=(largura//2, 95)
        tela.blit(texto_formatado, retTexto)
        pygame.display.update()
telaInicio()
pygame.draw.rect(tela,(0,0,180),(0,84,largura,400))#Exclui texto e imagens da tela inicial
tela.blit(div1,(0, 90))#Coloca imagem na tela
tela.blit(div2,(450, 90))#Coloca imagem na tela
def telaFinal():
    global final, div1, varCronometro, segundos, jogo, acertos, erros, pontos

    pygame.draw.rect(tela,(0,0,180),(0,95,largura,550))#Desenha retangulo
    div1=pygame.transform.scale(div1, [600, 500])#Define um tamanho para a div1
    tela.blit(div1,(185, 90))#Coloca imagem na tela
    mensagem="Acabou o tempo!"
    texto_formatado=fonte1.render(mensagem, False, (255,255,255))
    retTexto=texto_formatado.get_rect()
    retTexto.center=(largura//2, 95)
    tela.blit(texto_formatado, retTexto)
    mensagem="Pressione \"R\" para recomeçar"
    texto_formatado=fonte2.render(mensagem, False, (255,255,255))
    retTexto=texto_formatado.get_rect()
    retTexto.center=(largura//2, 130)
    tela.blit(texto_formatado, retTexto)

    stringAcertos=f"Acertos: {acertos}"
    texto_formatado=fonte2.render(stringAcertos, False, (0,0,0))
    tela.blit(texto_formatado, (300,205))
        
    stringErros=f"Erros: {erros}"
    texto_formatado=fonte2.render(stringErros, False, (0,0,0))
    tela.blit(texto_formatado, (300,245))

    stringPontos=f"Pontos: {pontos}"
    texto_formatado=fonte2.render(stringPontos, False, (0,0,0))
    tela.blit(texto_formatado, (300,285))

    stringResultados=None
    if(pontos<=9):
        stringResultados="Resultado: Atenção ruim!"
    elif((pontos>=10)and(pontos<=19)):
        stringResultados="Resultado: Atenção normal!"
    else:
        stringResultados="Resultado: Atenção boa!"
    texto_formatado=fonte2.render(stringResultados, False, (0,0,0))
    tela.blit(texto_formatado, (300,325))
    while(final==True):
        for event in pygame.event.get():
            if event.type==QUIT:
                clearInterval(varCronometro)
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_r:
                    pygame.draw.rect(tela,(0,0,180),(0,80,largura,400))#Desenha retangulo
                    div1=pygame.transform.scale(div1, [489, 509])#Define um tamanho para a div1
                    tela.blit(div1,(0, 90))#Coloca imagem na tela
                    tela.blit(div2,(450, 90))#Coloca imagem na tela
                    acertos=0
                    erros=0
                    pontos=0
                    final=False
                    segundos=60
                    jogo=False
        pygame.display.update()#Atualiza a tela
def geraImagem():
    global randomFormato, randomCor, randomDiv, acertarImg, acertarCor, acertarDiv
    acertarImg=False
    acertarCor=False
    acertarDiv=False
    randomFormato=randint(0, 3)#Sorteia um formato para a imagem
    randomCor=randint(0, 3)#Sorteia uma cor para a imagem
    randomDiv=randint(0, 1)#Sorteia uma div para a imagem
    fig=None
    print(f"Formato: {randomFormato}")
    print(f"Cor: {randomCor}")
    print(f"Div: {randomDiv}")
    print("===========================")
    if(randomFormato==0):
        fig=pygame.image.load("img/circulo/"+str(randomCor)+".png")#Cria objeto para a imagem
    elif(randomFormato==1):
        fig=pygame.image.load("img/pentagono/"+str(randomCor)+".png")#Cria objeto para a imagem
    elif(randomFormato==2):
        fig=pygame.image.load("img/quadrado/"+str(randomCor)+".png")#Cria objeto para a imagem
    elif(randomFormato==3):
        fig=pygame.image.load("img/triangulo/"+str(randomCor)+".png")#Cria objeto para a imagem
    fig=pygame.transform.scale(fig, [386, 372])#Define um tamanho para a figura
    if(randomDiv==0):
        tela.blit(fig,(55, 149))#Coloca imagem na telaDiv
    else:
        tela.blit(fig,(505, 149))#Coloca imagem na telaDiv
def deletarImg():
    tela.blit(div1,(0, 90))#Coloca imagem na tela
    tela.blit(div2,(450, 90))#Coloca imagem na tela
def acerto():
    global indiceAcertos, pontos, acertos
    indiceAcertos+=1
    if(indiceAcertos>=3):
        deletarImg()
        geraImagem()
        somAcerto.play()
        indiceAcertos=0
        pontos+=1
        acertos+=1
def erro():
    global erros, pontos, indiceAcertos
    indiceAcertos=0
    if(pontos!=0):
        pontos-=1
    erros+=1
    deletarImg()
    geraImagem()
    somErro.play()
def contador():
    global segundos
    segundos-=1
    print(segundos)
while True: #Loop principal do game
    relogio.tick(60)#Define em quantos frames o jogo irá rodar
    for event in pygame.event.get():#Averigua se um evento aconteceu
        if event.type==QUIT:#Se o botão de "sair" for precionado...
            clearInterval(varCronometro)
            pygame.quit()#Desliga o game
            exit()#Desliga o game
        if(event.type == pygame.KEYDOWN):
                if(jogo==True):
                    if ((event.key==pygame.K_LEFT)and(randomFormato==0)and(acertarImg==False)):
                        acertarImg=True
                        acerto()
                    elif ((event.key==pygame.K_UP)and(randomFormato==1)and(acertarImg==False)):
                        acertarImg=True
                        acerto()
                    elif ((event.key==pygame.K_RIGHT)and(randomFormato==2)and(acertarImg==False)):
                        acertarImg=True
                        acerto()
                    elif ((event.key==pygame.K_DOWN)and(randomFormato==3)and(acertarImg==False)):
                        acertarImg=True
                        acerto()
                    elif ((event.key==pygame.K_w)and(randomCor==0)and(acertarCor==False)):
                        acertarCor=True
                        acerto()
                    elif ((event.key==pygame.K_s)and(randomCor==1)and(acertarCor==False)):
                        acertarCor=True
                        acerto()
                    elif ((event.key==pygame.K_d)and(randomCor==2)and(acertarCor==False)):
                        acertarCor=True
                        acerto()
                    elif ((event.key==pygame.K_a)and(randomCor==3)and(acertarCor==False)):
                        acertarCor=True
                        acerto()
                    elif ((event.key==pygame.K_SPACE)and(randomDiv==0)and(acertarDiv==False)):
                        acertarDiv=True
                        acerto()
                    elif ((event.key==pygame.K_KP0)and(randomDiv==1)and(acertarDiv==False)):
                        acertarDiv=True
                        acerto()
                    else:
                        erro()
                else:
                    varCronometro=setInterval(contador, 1)
                    jogo=True
                    geraImagem()
    mensagemCronometro=f"Tempo: {segundos}s"#Define qual texto será exibido
    texto_formatado=fonte1.render(mensagemCronometro, True, (0,0,0))#Define a cor do texto e outros parâmetros
    pygame.draw.rect(tela,(100,100,255),(755,15,200,60))#Desenha retangulo
    tela.blit(texto_formatado, (755,15))#Coloca o texto na tela
    mensagemPontos=f"Pontos: {pontos}"#Define qual texto será exibido
    texto_formatado=fonte1.render(mensagemPontos, True, (0,0,0))#Define a cor do texto e outros parâmetros
    pygame.draw.rect(tela,(0,0,180),(15,585,200,60))#Desenha retangulo
    tela.blit(texto_formatado, (15,585))#Coloca o texto na tela
    if(segundos==0):
        clearInterval(varCronometro)
        final=True
        telaFinal()
    pygame.display.update()#Atualiza a tela