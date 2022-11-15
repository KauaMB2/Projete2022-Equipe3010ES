from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import firebase
import mariaDB
import json
import os
import datetime
import pyrebase
import pymysql.cursors
import cadastrar_RFID
import cadastrar_Biometria
import cadastrar_Rosto
data=datetime.datetime.now()
varJson=None
dir_path=os.path.dirname(__file__)
listSetores=[]
with open(f"{dir_path}/json/config.json") as JSON:
    varJson=json.load(JSON)
def loginConfirmado():
    Label(janela,text="REINICIE A GUI",bg="#00d0ff",font='Segoe 60').place(width=1000,height=600,relx=0.5,rely=0.65,anchor="center")
    return
def testaConexaoFirebase():
    try:
        testeFirebase={
            "apiKey": INapiKey.get(),
            "authDomain": INauthDomain.get(),
            "databaseURL": INdatabaseURL.get(),
            "projectId": INprojectId.get(),
            "storageBucket": INstorageBucket.get(),
            "messagingSenderId": INmessagingSenderId.get(),
            "appId": INappId.get()
        }
        firebase=pyrebase.initialize_app(testeFirebase)
        firebase.database()
        auth=firebase.auth()
        #CRIA novo usuário para autenticação
        #auth.create_user_with_email_and_password('zkauambbr@gmail.com','123456')
        emailFirebase=INemail.get()
        senhaFirebase=INsenhaEmail.get()
        auth.sign_in_with_email_and_password(emailFirebase,senhaFirebase)
        varJson["firebaseConfig"]["apiKey"]=INapiKey.get()
        varJson["firebaseConfig"]["authDomain"]=INauthDomain.get()
        varJson["firebaseConfig"]["databaseURL"]=INdatabaseURL.get()
        varJson["firebaseConfig"]["projectId"]=INprojectId.get()
        varJson["firebaseConfig"]["storageBucket"]=INstorageBucket.get()
        varJson["firebaseConfig"]["messagingSenderId"]=INmessagingSenderId.get()
        varJson["firebaseConfig"]["appId"]=INappId.get()
        varJson["databaseConfig"]["firebase"]=1
        varJson["databaseConfig"]["mariaDB"]=0
        varJson["userFirebase"]["email"]=emailFirebase
        varJson["userFirebase"]["senha"]=senhaFirebase
        varJson["mqtt"]["client_id"]=""
        varJson["mqtt"]["username"]=""
        varJson["mqtt"]["password"]=""
        varJson["mqtt"]["broker"]=""
        varJson["mqtt"]["port"]=""
        varJson["mqtt"]["topic"]=""
        varJson["mariaDB"]["nomeDB"]=""
        varJson["mariaDB"]["senhaDB"]=""
        with open(f"{dir_path}/json/config.json","w") as JSON:
            json.dump(varJson,JSON,indent=4)
        INapiKey.delete(0,END)
        INauthDomain.delete(0,END)
        INdatabaseURL.delete(0,END)
        INprojectId.delete(0,END)
        INstorageBucket.delete(0,END)
        INmessagingSenderId.delete(0,END)
        INappId.delete(0,END)
        INemail.delete(0,END)
        INsenhaEmail.delete(0,END)
        loginConfirmado()
        return
    except:
        messagebox.showinfo(title="ERRO",message="Não foi possível fazer a conexão com o banco de dados!\nVerifique se os dados estão inseridos corretamente.")
        return
def testaConexaoMariaDB():
    try:
        senhaDB=INSenhaDB.get()
        nomeDB=INNomeDB.get()
        con=pymysql.connect(host='localhost', user='root', database=nomeDB, password=senhaDB, cursorclass=pymysql.cursors.DictCursor)
        con.close()
        varJson["databaseConfig"]["firebase"]=0
        varJson["databaseConfig"]["mariaDB"]=1
        varJson["mariaDB"]["nomeDB"]=nomeDB
        varJson["mariaDB"]["senhaDB"]=senhaDB
        varJson["firebaseConfig"]["apiKey"]=""
        varJson["firebaseConfig"]["authDomain"]=""
        varJson["firebaseConfig"]["databaseURL"]=""
        varJson["firebaseConfig"]["projectId"]=""
        varJson["firebaseConfig"]["storageBucket"]=""
        varJson["firebaseConfig"]["messagingSenderId"]=""
        varJson["firebaseConfig"]["appId"]=""
        varJson["userFirebase"]["email"]=""
        varJson["userFirebase"]["senha"]=""
        INSenhaDB.delete(0,END)
        INNomeDB.delete(0,END)
        with open(f"{dir_path}/json/config.json","w") as JSON:
            json.dump(varJson,JSON,indent=4)
        loginConfirmado()
        return
    except:
        messagebox.showinfo(title="ERRO",message="Não foi possível fazer a conexão com o banco de dados!\nVerifique se os dados estão inseridos corretamente.")
        return
def escolherMariaDB():
    global INSenhaMQTT,INBroker,INPorta,INuser,INclienteID,INTopico,INSenhaDB,INNomeDB
    Frame(janela,borderwidth=0,relief="solid",bg="#00d0ff").place(relx=0.18,rely=0.7,anchor='center',width=400,height=450)
    Label(janela,text="Senha DB: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.55,rely=0.40)
    Label(janela,text="Nome DB: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.55,rely=0.45)
    INSenhaDB=Entry(janela)
    INSenhaDB.place(relx=0.65,rely=0.41)
    INNomeDB=Entry(janela)
    INNomeDB.place(relx=0.65,rely=0.46)
    btnConfirmarMariaDB=Button(janela,text="Confirmar MariaDB",bg="red",font='Segoe 15',command=testaConexaoMariaDB)
    btnConfirmarMariaDB.place(relx=0.55,rely=0.82)
    return
def escolherFirebase():
    global INapiKey,INauthDomain,INdatabaseURL,INprojectId,INstorageBucket,INmessagingSenderId,INappId,INemail,INsenhaEmail
    Frame(janela,borderwidth=0,relief="solid",bg="#00d0ff").place(relx=0.7,rely=0.7,anchor='center',width=400,height=450)
    Label(janela,text="apiKey: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.40)
    Label(janela,text="authDomain: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.45)
    Label(janela,text="databaseURL: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.50)
    Label(janela,text="projectId: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.55)
    Label(janela,text="storageBucket: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.60)
    Label(janela,text="messagingSenderId: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.65)
    Label(janela,text="appId: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.70)
    Label(janela,text="Email: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.75)
    Label(janela,text="Senha: ",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.04,rely=0.80)
    INapiKey=Entry(janela)
    INapiKey.place(relx=0.11,rely=0.41)
    INauthDomain=Entry(janela)
    INauthDomain.place(relx=0.15,rely=0.46)
    INdatabaseURL=Entry(janela)
    INdatabaseURL.place(relx=0.165,rely=0.51)
    INprojectId=Entry(janela)
    INprojectId.place(relx=0.125,rely=0.56)
    INstorageBucket=Entry(janela)
    INstorageBucket.place(relx=0.175,rely=0.61)
    INmessagingSenderId=Entry(janela)
    INmessagingSenderId.place(relx=0.22,rely=0.66)
    INappId=Entry(janela)
    INappId.place(relx=0.1,rely=0.71)
    INemail=Entry(janela)
    INemail.place(relx=0.1,rely=0.76)
    INsenhaEmail=Entry(janela)
    INsenhaEmail.place(relx=0.1,rely=0.81)
    btnConfirmarMariaDB=Button(janela,text="Confirmar Firebase",bg="red",font='Segoe 15',command=testaConexaoFirebase)
    btnConfirmarMariaDB.place(relx=0.04,rely=0.87)
    return
with open(f"{dir_path}/json/config.json") as JSON:
    varJson=json.load(JSON)
if varJson["databaseConfig"]["firebase"]!=0 or varJson["databaseConfig"]["mariaDB"]!=0:
    if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
        firebase.iniciar()
    if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
        mariaDB.iniciar()
    if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
        listSetores=firebase.SETORES()#Devolve uma lista com os setores do DB
        listSetores.remove("setores")
        listSetores.remove("funcionarios")
    if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
        listSetores=mariaDB.SETORES()#Devolve uma lista com os setores do DB
        listSetores.remove("setores")
        listSetores.remove("funcionarios")
    listSetoresCompleto=[]
    for i in range(0,len(listSetores),1):
        listSetoresCompleto.append(listSetores[i])
    listSetoresCompleto.append("setores")
    listSetoresCompleto.append("funcionarios")
    listCadastroFunc=[]
    listCadastroSetor=["Id","Nome","Horario"]
    def popular(infoT):
        global tv2,tvLabel
        try:
            tv2.destroy()
        except:
            pass
        if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
            tabela=firebase.TABELA(infoT)
        if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
            tabela=mariaDB.TABELA(infoT)
        sizeTABELA=len(tabela)
        colunasTabela=[]
        for k in range(0,sizeTABELA,1):
            colunasTabela.append(tabela[k]['COLUMN_NAME'])
        if (infoT=="funcionarios"):
            tv2=ttk.Treeview(tvLabel, columns=colunasTabela, show = 'headings')
            tv2.column('Id', minwidth = 1, width = 1)
            tv2.column('Nome', minwidth = 1, width = 1)
            tv2.column('Horario', minwidth = 1, width = 1)
            tv2.column('Setores',minwidth = 650, width = 650)
            tv2.heading('Id', text = 'ID')
            tv2.heading('Nome', text = 'NOME')
            tv2.heading('Horario', text = 'HORARIO')
            tv2.heading('Setores', text = 'SETORES')
            tv2.place(relx=0.48,rely=0.5,width=653,anchor='center')
            if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
                linhas=firebase.LINHAS(infoT)
            if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
                linhas=mariaDB.LINHAS(infoT)
            sizeLINHAS=len(linhas)
            for t in range(3,sizeTABELA,1):
                tv2.column(colunasTabela[t],minwidth=85,width=85)
                tv2.heading(colunasTabela[t],text=colunasTabela[t].upper())
            tv2.place(relx=0.48,rely=0.5,anchor='center')
            listInfo=[]
            for c in range(0,sizeLINHAS,1):
                info=[]
                for g in linhas[c].values():
                    info.append(g)
                listInfo.append(info)
            for i in listInfo:
                tv2.insert("","end",values=i)
            return
        if (infoT=="setores"):
            size=92
            tv2=ttk.Treeview(tvLabel, columns=colunasTabela, show = 'headings')
            tv2.column('Setor', minwidth = size, width = size)
            tv2.column('Horario', minwidth = size+30, width = size+30)
            tv2.column('Capacete', minwidth = size, width = size)
            tv2.column('protAuricular',minwidth = size, width = size)
            tv2.column('Luvas', minwidth = size, width = size)
            tv2.column('Colete', minwidth = size, width = size)
            tv2.column('Botas', minwidth = size, width = size)
            tv2.column('Mascara', minwidth = size, width = size)
            tv2.heading('Setor', text = 'SETOR')
            tv2.heading('Horario', text = 'HORARIO')
            tv2.heading('Capacete', text = 'CAPACETE')
            tv2.heading('protAuricular', text = 'PROTAURICULAR')
            tv2.heading('Luvas', text = 'LUVAS')
            tv2.heading('Colete', text = 'COLETE')#aqui
            tv2.heading('Botas', text = 'BOTAS')
            tv2.heading('Mascara', text = 'MASCARA')
            tv2.place(relx=0.5,rely=0.5,anchor='center')
            if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
                linhas=firebase.LINHAS(infoT)
            if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
                linhas=mariaDB.LINHAS(infoT)
            sizeLINHAS=len(linhas)
            listInfo=[]
            for c in range(0,sizeLINHAS,1):
                info=[]
                for g in linhas[c].values():
                    info.append(g)
                listInfo.append(info)
            for i in listInfo:
                tv2.insert("","end",values=i)
            return
        tv2=ttk.Treeview(tvLabel, columns=colunasTabela, show = 'headings')
        tv2.column('Id', minwidth = 30, width = 30)
        tv2.column('Nome', minwidth = 100, width = 100)
        tv2.column('Horario', minwidth = 150, width = 150)
        tv2.heading('Id', text = 'ID')
        tv2.heading('Nome', text = 'NOME')
        tv2.heading('Horario', text = 'HORARIO')
        if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
            linhas=firebase.LINHAS(infoT)
        if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
            linhas=mariaDB.LINHAS(infoT)
        sizeLINHAS=len(linhas)
        for t in range(3,sizeTABELA,1):
            tv2.column(colunasTabela[t],minwidth=85,width=85)
            tv2.heading(colunasTabela[t],text=colunasTabela[t].upper())
        tv2.place(relx=0.48,rely=0.5,anchor='center')
        listInfo=[]
        for c in range(0,sizeLINHAS,1):
            info=[]
            for g in linhas[c].values():
                info.append(g)
            listInfo.append(info)
        for i in listInfo:
            tv2.insert("","end",values=i)
        return
    def resetarCadastroSetor():
        global NovobtnSetor,listCadastroSetor,nomeSetor
        try:
            quadroProtAuricular.destroy()
        except:
            pass
        try:
            quadroBotas.destroy()
        except:
            pass
        try:
            quadroLuva.destroy()
        except:
            pass
        try:
            quadroColete.destroy()
        except:
            pass
        try:
            quadroCapacete.destroy()
        except:
            pass
        try:
            btnFinalizar.destroy()
        except:
            pass
        try:
            quadroMascara.destroy()
        except:
            pass
        NovobtnSetor=Button(Frame1, text="Adicionar setor", command=cadastrarSetor)
        NovobtnSetor.place(relx=0.30,y=195)
        btnReset.destroy()
        listCadastroSetor=["Id","Nome","Horario"]
        nomeSetor=""
        return
    def resetarCadastroFunc():
        global btnConfirmar1,btnConfirmar2,btnDigital,btnRFID,btnRosto
        try:
            quadroSetordoFunc.destroy()
        except:
            pass
        try:
            quadroNome.destroy()
        except:
            pass
        try:
            btnConfirmar2.destroy()
        except:
            pass
        try:
            btnDigital.destroy()
        except:
            pass
        try:
            btnRFID.destroy()
        except:
            pass
        try:
            btnRosto.destroy()
        except:
            pass
        listCadastroFunc.clear()
        btnConfirmar1.destroy()
        btnConfirmar1=Button(Frame2,text="Começar",bg="#00ff09",font='Segoe 25',command=cadastrarNome)
        btnConfirmar1.place(relx=0.48,y=100,anchor='center')
        return
    def simCapacete():
        listCadastroSetor.append('Capacete')
        texto['bg']="#00ff09"
        cadastrarProtAuricular()
        return
    def naoCapacete():
        texto['bg']="red"
        cadastrarProtAuricular()
        return
    def simProtAuricular():
        listCadastroSetor.append('protAuricular')
        texto['bg']="#00ff09"
        cadastrarLuva()
        return
    def naoProtAuricular():
        texto['bg']="red"
        cadastrarLuva()
        return
    def simLuva():
        listCadastroSetor.append('Luvas')
        texto['bg']="#00ff09"
        cadastrarColete()
        return
    def naoLuva():
        texto['bg']="red"
        cadastrarColete()
        return
    def simColete():
        listCadastroSetor.append('Colete')
        texto['bg']="#00ff09"
        cadastrarBotas()
        return
    def naoColete():
        texto['bg']="red"
        cadastrarBotas()
        return
    def simBotas():
        listCadastroSetor.append('Botas')
        texto['bg']="#00ff09"
        cadastrarMascara()
        return
    def naoBotas():
        texto['bg']="red"
        cadastrarMascara()
        return
    def simMascara():
        listCadastroSetor.append('Mascara')
        texto['bg']="#00ff09"
        finalizarCadastro()
        return
    def naoMascara():
        texto['bg']="red"
        finalizarCadastro()
        return
    def confirmarRESET():
        Label(Frame5,text="REINICIE A GUI",bg="#00d0ff",font='Segoe 60').place(width=600,height=300,relx=0.5,rely=0.5,anchor="center")
        varJson["firebaseConfig"]["apiKey"]=""
        varJson["firebaseConfig"]["authDomain"]=""
        varJson["firebaseConfig"]["databaseURL"]=""
        varJson["firebaseConfig"]["projectId"]=""
        varJson["firebaseConfig"]["storageBucket"]=""
        varJson["firebaseConfig"]["messagingSenderId"]=""
        varJson["firebaseConfig"]["appId"]=""
        varJson["databaseConfig"]["firebase"]=0
        varJson["databaseConfig"]["mariaDB"]=0
        varJson["userFirebase"]["email"]=""
        varJson["userFirebase"]["senha"]=""
        varJson["mqtt"]["client_id"]=""
        varJson["mqtt"]["username"]=""
        varJson["mqtt"]["password"]=""
        varJson["mqtt"]["broker"]=""
        varJson["mqtt"]["port"]=""
        varJson["mqtt"]["topic"]=""
        varJson["mariaDB"]["nomeDB"]=""
        varJson["mariaDB"]["senhaDB"]=""
        with open(f"{dir_path}/json/config.json","w") as JSON:
            json.dump(varJson,JSON,indent=4)
        return
    def RESET():
        global btnResetarJANELA
        btnResetarJANELA.destroy()
        Label(Frame5,text="RESET",bg="#00d0ff",font='Segoe 40').place(relx=0.49,rely=0.4,anchor="center")
        btnResetarJANELA=Button(Frame5,text="CONFIRMAR RESET",bg="red",font='Segoe 40',command=confirmarRESET)
        btnResetarJANELA.place(relx=0.49,rely=0.6,anchor="center")
        return
    def addListSetor():
        global cb2Tabelas
        cb2Tabelas.destroy()
        try:
            if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
                firebase.CREATE_TABLE(listCadastroSetor)
            if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
                mariaDB.CREATE_TABLE(listCadastroSetor)
            listSetores.append(nomeSetor)
            listSetoresCompleto.append(nomeSetor)
            cb2Tabelas=ttk.Combobox(Frame4, values = listSetoresCompleto)
            cb2Tabelas.place(relx=0.75,rely=0.60)
        except:
            messagebox.showinfo(title="ERRO",message="Não foi possível fazer o cadastro do setor\nTente novamente sem o uso de caracteres especiais")
        resetarCadastroSetor()
        return
    def finalizarCadastro():
        global btnFinalizar
        btnSim.destroy()
        btnNao.destroy()
        Label(quadroMascara,text="Sim",font="Segoe 10",bg="#00d0ff").place(relx=0.68,rely=0.10)
        Label(quadroMascara,text="Não",font="Segoe 10",bg="#00d0ff").place(relx=0.82,rely=0.10)
        btnFinalizar=Button(Frame1,text="FINALIZAR",bg="#00ff09",font=('Segoe 40'),command=addListSetor)
        btnFinalizar.place(relx=0.3,rely=0.62)
        return
    def cadastrarMascara():
        global btnSim,btnNao,quadroMascara,texto
        btnSim.destroy()
        btnNao.destroy()
        btnSim.destroy()
        btnNao.destroy()
        Label(quadroBotas, text="Sim",font="Segoe 10",bg="#00d0ff").place(relx=0.68,rely=0.10)
        Label(quadroBotas, text="Não",font="Segoe 10",bg="#00d0ff").place(relx=0.82,rely=0.10)
        quadroMascara=Frame(Frame1,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroMascara.place(relx=0.61,rely=0.42,width=280,height=50)
        texto=Label(quadroMascara, text="O funcionário vai utilizar \nMáscara de proteção?", font=('Segoe 12'), bg='#00d0ff')
        texto.place(relx=0,rely=0.10)
        btnSim=Button(quadroMascara, text="Sim", command=simMascara)
        btnSim.place(relx=0.68,rely=0.10)
        btnNao=Button(quadroMascara, text="Não",command=naoMascara)
        btnNao.place(relx=0.82,rely=0.10)
        return
    def cadastrarBotas():
        global btnSim,btnNao,quadroBotas,texto
        btnSim.destroy()
        btnNao.destroy()
        Label(quadroColete, text="Sim",font="Segoe 10",bg="#00d0ff").place(relx=0.68,rely=0.10)
        Label(quadroColete, text="Não",font="Segoe 10",bg="#00d0ff").place(relx=0.82,rely=0.10)
        quadroBotas=Frame(Frame1,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroBotas.place(relx=0.61,rely=0.32,width=280,height=50)
        texto=Label(quadroBotas, text="O funcionário vai utilizar \nbotas de proteção?", font=('Segoe 12'), bg='#00d0ff')
        texto.place(relx=0,rely=0.10)
        btnSim=Button(quadroBotas, text="Sim", command=simBotas)
        btnSim.place(relx=0.68,rely=0.10)
        btnNao=Button(quadroBotas, text="Não",command=naoBotas)
        btnNao.place(relx=0.82,rely=0.10)
        return
    def cadastrarColete():
        global btnSim,btnNao,quadroColete,texto
        btnSim.destroy()
        btnNao.destroy()
        Label(quadroLuva, text="Sim",font="Segoe 10",bg="#00d0ff").place(relx=0.68,rely=0.10)
        Label(quadroLuva, text="Não",font="Segoe 10",bg="#00d0ff").place(relx=0.82,rely=0.10)
        quadroColete=Frame(Frame1,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroColete.place(relx=0.35,rely=0.42,width=280,height=50)
        texto=Label(quadroColete, text="O funcionário vai utilizar \ncolete de proteção?", font=('Segoe 12'), bg='#00d0ff')
        texto.place(relx=0,rely=0.10)
        btnSim=Button(quadroColete, text="Sim", command=simColete)
        btnSim.place(relx=0.68,rely=0.10)
        btnNao=Button(quadroColete, text="Não",command=naoColete)
        btnNao.place(relx=0.82,rely=0.10)
        return
    def cadastrarLuva():
        global btnSim,btnNao,quadroLuva,texto
        btnSim.destroy()
        btnNao.destroy()
        Label(quadroProtAuricular, text="Sim",font="Segoe 10",bg="#00d0ff").place(relx=0.68,rely=0.10)
        Label(quadroProtAuricular, text="Não",font="Segoe 10",bg="#00d0ff").place(relx=0.82,rely=0.10)
        quadroLuva=Frame(Frame1,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroLuva.place(relx=0.35,rely=0.32,width=280,height=50)
        texto=Label(quadroLuva, text="O funcionário vai utilizar \nluvas de proteção?", font=('Segoe 12'), bg='#00d0ff')
        texto.place(relx=0,rely=0.10)
        btnSim=Button(quadroLuva, text="Sim", command=simLuva)
        btnSim.place(relx=0.68,rely=0.10)
        btnNao=Button(quadroLuva, text="Não",command=naoLuva)
        btnNao.place(relx=0.82,rely=0.10)
        return
    def cadastrarProtAuricular():
        global btnSim,btnNao,quadroProtAuricular,texto
        btnSim.destroy()
        btnNao.destroy()
        Label(quadroCapacete, text="Sim",font="Segoe 10",bg="#00d0ff").place(relx=0.68,rely=0.10)
        Label(quadroCapacete, text="Não",font="Segoe 10",bg="#00d0ff").place(relx=0.82,rely=0.10)
        quadroProtAuricular=Frame(Frame1,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroProtAuricular.place(relx=0.07,rely=0.42,width=280,height=50)
        texto=Label(quadroProtAuricular, text="O funcionário vai utilizar \nprotetor auricular?", font=('Segoe 12'), bg='#00d0ff')
        texto.place(relx=0,rely=0.10)
        btnSim=Button(quadroProtAuricular, text="Sim", command=simProtAuricular)
        btnSim.place(relx=0.68,rely=0.10)
        btnNao=Button(quadroProtAuricular, text="Não",command=naoProtAuricular)
        btnNao.place(relx=0.82,rely=0.10)
        return
    def cadastrarCapacete():
        global btnSim,btnNao,texto,quadroCapacete
        quadroCapacete=Frame(Frame1,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroCapacete.place(relx=0.07,rely=0.32,width=280,height=50)
        texto=Label(quadroCapacete,text="O funcionário irá utilizar \ncapacete de proteção?", font=('Segoe 12'), bg='#00d0ff')
        texto.place(relx=0,rely=0.10)
        btnSim=Button(quadroCapacete,text="Sim",command=simCapacete)
        btnSim.place(relx=0.68,rely=0.10)
        btnNao=Button(quadroCapacete,text="Não",command=naoCapacete)
        btnNao.place(relx=0.82,rely=0.10)
        return
    def cadastrarSetor():
        global btnReset,nomeSetor
        nomeSetor=InSetor.get()
        if(nomeSetor==""):
            messagebox.showinfo(title = "ERRO", message = "Digite o nome do setor")
            return
        btnSetor.destroy()
        Label(Frame1,text="Adicionar setor\n ",bg="#00d0ff",font="Segoe 10").place(relx=0.30, y=195)
        btnReset=Button(Frame1, text="Reiniciar cadastro",command=resetarCadastroSetor)
        btnReset.place(relx=0.40, y=195)
        listCadastroSetor.append(nomeSetor)
        InSetor.delete(0, END)
        cadastrarCapacete()
        return
    ###############################################################################
    def cadastrarDigital():
        global nomeFunc
        cadastrar_Biometria.cadastrar(nomeFunc)
        if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
            firebase.INSERT_FUNC(listCadastroFunc,nomeFunc)
        if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
            mariaDB.INSERT_FUNC(listCadastroFunc,nomeFunc)
        resetarCadastroFunc()
        return 
    def cadastrarRFID():
        global nomeFunc
        cadastrar_RFID.cadastrar(nomeFunc)
        resetarCadastroFunc()
        return 
    def cadastrarRosto():
        global nomeFunc
        cadastrar_Rosto.cadastrar(nomeFunc)
        cadastrar_Rosto.createTrain()
        try:
            if varJson["databaseConfig"]["firebase"]==1 and varJson["databaseConfig"]["mariaDB"]==0:
                firebase.INSERT_FUNC(listCadastroFunc,nomeFunc)
            if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==1:
                mariaDB.INSERT_FUNC(listCadastroFunc,nomeFunc)
        except:
            messagebox.showinfo(title="ERRO",message="Não foi possível fazer o cadastro do funcionário\nTente novamente sem o uso de caracteres especiais")
        resetarCadastroFunc()
        return
    def cadastro():
        global btnConfirmar2,btnDigital,btnRFID,btnRosto
        if(str(tvSetor.get_children())=="()"):
            messagebox.showinfo(title = "ERRO", message = "Nenhum setor cadastrado")
            return
        btnConfirmar2.destroy()
        btnAddsetor.destroy()
        Label(quadroSetordoFunc,text="Adicionar setor",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 10").place(relx=0.64,rely=0.40,anchor='center')
        Label(quadroSetordoFunc,text="Confirmar",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 10").place(relx=0.85,rely=0.80,anchor='center')
        btnDigital=Button(Frame2,text="Cadastrar digital",bg="#00ff09",font='Segoe 18',command=cadastrarDigital)
        btnDigital.place(relx=0.20,rely=0.60)
        btnRFID=Button(Frame2,text="Cadastrar RFID",bg="#00ff09",font='Segoe 18',command=cadastrarRFID)
        btnRFID.place(relx=0.40,rely=0.60)
        btnRosto=Button(Frame2,text="Cadastrar rosto",bg="#00ff09",font='Segoe 18',command=cadastrarRosto)
        btnRosto.place(relx=0.60,rely=0.60)
        return
    def addSetor():
        global cb1Tabelas
        varAddSetor=cb1Tabelas.get()
        if(varAddSetor==""):
            messagebox.showinfo(title = "ERRO", message = "Selecione algum dado")
            return
        for i in listCadastroFunc:
            if(varAddSetor==i):
                messagebox.showinfo(title = "ERRO", message = "Dado já inserido")
                return
        listCadastroFunc.append(varAddSetor)
        tvSetor.insert("","end",values=varAddSetor)
        return
    def cadastrarSetordoFunc():
        global InNome,btnConfirmar2,btnConfirmar1,quadroSetordoFunc,btnAddsetor,cb1Tabelas,tvSetor,nomeFunc,listSetores
        nomeFunc=InNome.get()
        if(nomeFunc==""):
            messagebox.showinfo(title = "ERRO", message = "Digite o nome do funcionário")
            return
        btnConfirmar2.destroy()
        Label(quadroNome,text="Confirmar",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 10").place(relx=0.6,rely=0.80,anchor='center')
        quadroSetordoFunc=Frame(Frame2,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroSetordoFunc.place(relx=0.55,rely=0.48,anchor='center',width=680,height=200)
        Labeltxt=Label(quadroSetordoFunc,text=f"Escolha o(s) setor(es) de {nomeFunc}", font='Segoe 18', bg='#00d0ff')
        Labeltxt.place(x=20,rely=0.15)
        cb1Tabelas=ttk.Combobox(quadroSetordoFunc,values=listSetores)
        cb1Tabelas.place(relx=0.45,rely=0.40, anchor='center')
        btnAddsetor=Button(quadroSetordoFunc,text="Adicionar setor",command=addSetor)
        btnAddsetor.place(relx=0.64,rely=0.40,anchor='center')
        btnConfirmar2=Button(quadroSetordoFunc,text="Confirmar",command=cadastro)
        btnConfirmar2.place(relx=0.85,rely=0.80,anchor='center')
        tvSetor=ttk.Treeview(quadroSetordoFunc, columns = ("setores"), show = 'headings')
        tvSetor.column('setores', minwidth=80,width=80)
        tvSetor.heading('setores', text = 'SETORES')
        tvSetor.place(relx=0.85,rely=0.40,height=120,anchor='center')
        InNome.delete(0,END)
        return
    def cadastrarNome():
        global btnConfirmar2,btnConfirmar1,InNome,quadroNome,nomeSetor
        btnConfirmar1.destroy()
        btnConfirmar1=Button(Frame2,text="Reiniciar",bg="#00ff09",font='Segoe 25',command=resetarCadastroFunc)
        btnConfirmar1.place(relx=0.48,y=100,anchor='center')
        quadroNome=Frame(Frame2,borderwidth=0,relief="solid",bg="#00d0ff")
        quadroNome.place(relx=0.48,rely=0.30,anchor='center',width=400,height=70)
        Labeltxt=Label(quadroNome,text="Digite o nome do funcionário", font='Segoe 18', bg='#00d0ff')
        Labeltxt.place(relx=0.48,rely=0.20,anchor='center')
        InNome=Entry(quadroNome)
        InNome.place(relx=0.34,rely=0.80, anchor='center')
        btnConfirmar2=Button(quadroNome,text="Confirmar",command=cadastrarSetordoFunc)
        btnConfirmar2.place(relx=0.6,rely=0.80,anchor='center')
        return
    def escolherTabela():
        global cb2Tabelas,tabelaSelecionada
        tabelaSelecionada=cb2Tabelas.get()
        verificaSETOR=False
        for i in listSetoresCompleto:
            if tabelaSelecionada == i:
                verificaSETOR=True
        if verificaSETOR==False:
            messagebox.showinfo(title="ERRO",message="A tabela selecionada não existe")
            return
        cb2Tabelas.set("")
        popular(tabelaSelecionada)
        return
    def formarFramesetores():
        global btnSetor,InSetor
        Labeltxt=Label(Frame1,text="Bem vindo à área de cadastro de setores!", font='Segoe 35', bg='#00d0ff')
        Labeltxt.place(relx=0.48,y=40, anchor='center')
        Labeltxt=Label(Frame1,text="Aqui você consegue cadastrar os setores de serviço da sua empresa\nque serão utilizados na verificação do CEPEG", font=('Segoe 16'), bg='#00d0ff')
        Labeltxt.place(relx=0.48,y=100, anchor='center')
        Label(Frame1,text="Setor da empresa: ",bg="#00d0ff",font='Segoe 15').place(x=20,y=190)
        InSetor=Entry(Frame1)
        InSetor.place(relx=0.18,y=195)
        btnSetor=Button(Frame1, text="Adicionar setor",command=cadastrarSetor)
        btnSetor.place(relx=0.30,y=195)
        return
    def formarFramefuncionarios():
        global btnConfirmar1
        Labeltxt=Label(Frame2,text="Cadastre cada funcionário de acordo com o seu setor na empresa", font='Segoe 25', bg='#00d0ff')
        Labeltxt.place(relx=0.47,y=40, anchor='center')
        btnConfirmar1=Button(Frame2,text="Começar",bg="#00ff09",font='Segoe 25',command=cadastrarNome)
        btnConfirmar1.place(relx=0.48,y=100,anchor='center')
        return
    def formarFrametabela():
        global tv,cb2Tabelas,tvLabel,Entrypesquisa,listSetoresCompleto
        tvLabel=Label(Frame4,bg='green')
        tvLabel.place(relx=0.48,y=220,anchor="center",width=1000,height=400)
        cb2Tabelas=ttk.Combobox(Frame4, values = listSetoresCompleto)
        cb2Tabelas.place(relx=0.75,rely=0.60)
        btn_esportes = Button(Frame4, text = "Selecionar tabela", command = escolherTabela)
        btn_esportes.place(relx=0.75,rely=0.65)
        """Label(Frame4,text="Pesquisar item:",bg="#00d0ff").place(x=30,rely=0.57)
        Entrypesquisa=Entry(Frame4)
        Entrypesquisa.place(x=30,rely=0.60)
        bpesquisa=Button(Frame4,text="Pesquisar",command=pesquisar)
        bpesquisa.place(x=160,rely=0.60)
        Label(Frame4,text="Deletar item:",bg="#00d0ff").place(x=260,rely=0.57)
        bdeletar=Button(Frame4,text="Deletar",command=deletar)
        bdeletar.place(x=260,rely=0.60)"""
        return
    def formarFrameresetar():
        global btnResetarJANELA
        Label(Frame5,text="Clique no botão de RESET\npara resetar a GUI",font='Segoe 25',bg='#00d0ff').place(relx=0.49,rely=0.1,anchor="center")
        btnResetarJANELA=Button(Frame5,text="RESETAR",bg="red",font='Segoe 40',command=RESET)
        btnResetarJANELA.place(relx=0.49,rely=0.4,anchor="center")
        return
    janela=Tk()
    janela.title("CEPEG")
    janela.geometry("1100x650")
    nb=ttk.Notebook(janela)#Formação das Labels
    nb.place(x = 0, y = 0, width = 1100, height = 800)
    Frame1=Frame(nb)
    Frame2=Frame(nb)
    Frame3=Frame(nb)
    Frame4=Frame(nb)
    Frame5=Frame(nb)
    Frame1['bg']='#00d0ff'
    Frame2['bg']='#00d0ff'
    Frame3['bg']='#00d0ff'
    Frame4['bg']='#00d0ff'
    Frame5['bg']='#00d0ff'
    nb.add(Frame1,text="Setores")
    nb.add(Frame2,text="Funcionários")
    nb.add(Frame4,text="Tabela")
    nb.add(Frame5,text="RESETAR")
    formarFramesetores()
    formarFramefuncionarios()
    formarFrametabela()
    formarFrameresetar()
    janela.mainloop()
if varJson["databaseConfig"]["firebase"]==0 and varJson["databaseConfig"]["mariaDB"]==0:
    janela=Tk()
    janela.title("Configurações")
    janela.geometry("1100x650")
    janela['bg']='#00d0ff'
    Label(janela,text="Bem vindo às configurações do CEPEG!",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 28").place(relx=0.49,rely=0.05,anchor='center')
    Label(janela,text="Aqui você pode escolher o banco de dados que deseja trabalhar e o protocolo de .",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 15").place(relx=0.49,rely=0.10,anchor='center')
    Label(janela,text="Escolha entre as opções abaixo:",borderwidth=0,relief="solid",bg="#00d0ff",font="Segoe 13").place(relx=0.49,rely=0.14,anchor='center')
    btnMariaDB=Button(janela,text="Firebase",bg="#00ff09",font='Segoe 20',command=escolherFirebase)
    btnMariaDB.place(relx=0.15,y=160)
    btnFirebase=Button(janela,text="MySQL(MariaDB)",bg="#00ff09",font='Segoe 20',command=escolherMariaDB)
    btnFirebase.place(relx=0.65,y=160)
    janela.mainloop()