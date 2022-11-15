import json
import pyrebase
import datetime
import os
data=datetime.datetime.now()

dir_path=os.path.dirname(__file__)
with open(f"{dir_path}/json/config.json") as JSON:
    varJson=json.load(JSON)
db=None
def iniciar():
    global db
    firebaseConfig=varJson["firebaseConfig"]
    firebase=pyrebase.initialize_app(firebaseConfig)
    db=firebase.database()
    auth=firebase.auth()
    #CRIA novo usuário para autenticação
    #auth.create_user_with_email_and_password('zkauambbr@gmail.com','123456')
    email=varJson["userFirebase"]["email"]
    senha=varJson["userFirebase"]["senha"]
    if email!='' and senha!='':
        user = auth.sign_in_with_email_and_password(email,senha)
    return
def SETORES():
    global db
    request = db.child("/sistema/nomeSetores").get().val()
    return request
def TABELA(infoT):
    global db
    if(infoT=="funcionarios"):
        request=[{'COLUMN_NAME': 'Id'}, 
        {'COLUMN_NAME': 'Nome'}, 
        {'COLUMN_NAME': 'Horario'}, 
        {'COLUMN_NAME': 'Setores'}]
        return request
    if(infoT=="setores"):
        request=[{'COLUMN_NAME': 'Setor'}, 
        {'COLUMN_NAME': 'Horario'}, 
        {'COLUMN_NAME': 'Capacete'}, 
        {'COLUMN_NAME': 'protAuricular'}, 
        {'COLUMN_NAME': 'Luvas'}, 
        {'COLUMN_NAME': 'Colete'}, 
        {'COLUMN_NAME': 'Botas'},  
        {'COLUMN_NAME': 'Mascara'}]
        return request
    request=db.child(f"/sistema/nomeColunas/{infoT}").get().val()
    COLUMNS_NAME=[]
    for x in range(0,len(request),1):
        y={'COLUMN_NAME': request[x]}
        COLUMNS_NAME.append(y)
    return COLUMNS_NAME
def LINHAS(infoT):
    global db
    if(infoT=="funcionarios"):
        listFuncionarios=db.child("/funcionarios").get().val()
        #COLOCAR ID no request
        listaFinal=[]
        for x in range(0,len(listFuncionarios),1):
            varDict={'Id': x,'Nome': listFuncionarios[x]['Nome'], 'Horario': listFuncionarios[x]['Horario'], 'Setores':listFuncionarios[x]['Setores']}
            listaFinal.append(varDict)
        return listaFinal
    if(infoT=="setores"):
        nomeSetores=db.child("/sistema/nomeSetores").get().val()
        nomeSetores.remove("funcionarios")
        nomeSetores.remove("setores")
        setores=db.child("/setores").get().val()
        #print(setores[nomeSetores[0]])#TESTE para chamar nomeSetores[0]"automa" - DÁ PRA USAR O LOOP for
        listSetores=[]
        for w in range(0,len(nomeSetores),1):
            varJson1={'Setor': nomeSetores[w], 'Horario': setores[nomeSetores[w]]['Horario']}
            setoresDict=json.loads(json.dumps(setores))
            DictFinal=varJson1
            for y,x in setoresDict[nomeSetores[w]].items():
                if(y!='Horario'):
                    DictFinal.update({y:x})
            listSetores.append(DictFinal)
        return listSetores
    listRegistro=db.child("/registro").child(f'{infoT}').get().val()
    listaFinal=[]
    if(str(listRegistro)!="None"):
        for x in range(0,len(listRegistro),1):
            varDict1={'Id': x,'Nome': listRegistro[x]['Nome'], 'Horario': listRegistro[x]['Horario']}
            del listRegistro[x]['Nome']
            del listRegistro[x]['Horario']
            varDict1.update(listRegistro[0])
            listaFinal.append(varDict1)
    return listaFinal
def CREATE_TABLE(tabela):
    global db
    totalSetores=len(db.child("sistema").child("nomeSetores").get().val())
    db.child(f"/sistema").child("nomeSetores").update({int(totalSetores): tabela[3]})
    dados=[]
    for x in range(0,len(tabela),1):
        if(x!=3):
            dados.append(tabela[x])
    db.child("sistema").child("nomeColunas").update({tabela[3]: dados})
    varDict={
        'Horario': f"{data.day}/{data.month}/{data.year} - {data.hour}h {data.minute}m",
        'Capacete': 'NaoEquipado',
        'protAuricular': 'NaoEquipado',
        'Luvas': 'NaoEquipado',
        'Colete': 'NaoEquipado',
        'Botas': 'NaoEquipado',
        'Mascara': 'Equipado'
    }
    for x in range(4,len(tabela),1):
        if(tabela[x]=="Capacete"):
            varDict["Capacete"]="Equipado"
        if(tabela[x]=="protAuricular"):
            varDict["protAuricular"]="Equipado"
        if(tabela[x]=="Luvas"):
            varDict["Luvas"]="Equipado"
        if(tabela[x]=="Colete"):
            varDict["Colete"]="Equipado"
        if(tabela[x]=="Capacete"):
            varDict["Capacete"]="Equipado"
        if(tabela[x]=="Botas"):
            varDict["Botas"]="Equipado"
        if(tabela[x]=="Mascara"):
            varDict["Mascara"]="Equipado"
    db.child("setores").child(f"{tabela[3]}").update(varDict)
    return
def INSERT_FUNC(setores,nomeFunc):
    global db
    totalFunc=len(db.child("funcionarios").get().val())
    varDict={
        'Horario': f"{data.day}/{data.month}/{data.year} - {data.hour}h {data.minute}m",
        'Nome': nomeFunc,
        'Setores': setores
    }
    db.child("funcionarios").child(f"{totalFunc}").update(varDict)
    return