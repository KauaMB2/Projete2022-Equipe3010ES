import pymysql.cursors
import datetime
import json
import os
data=datetime.datetime.now()
#Abrindo conexão com MariaDB
listEPIs=["Setor","Horario","Capacete","protAuricular","Luvas","Colete","Botas","Mascara"]
dir_path=os.path.dirname(__file__)
with open(f"{dir_path}\json\config.json") as JSON:
    varJson=json.load(JSON)
senha=varJson["mariaDB"]["senhaDB"]
nomeDB=varJson["mariaDB"]["nomeDB"]
def CONECT():
    global con
    con=pymysql.connect(host='localhost', user='root', database=nomeDB, password=senha, cursorclass=pymysql.cursors.DictCursor)
def iniciar():
    CONECT()
    with con.cursor() as c:
        sql="CREATE TABLE IF NOT EXISTS funcionarios(Id INT(255),Nome VARCHAR(255),Horario VARCHAR(255),Setores VARCHAR(255));"
        c.execute(sql)
        sql="CREATE TABLE IF NOT EXISTS setores(Setor VARCHAR(255),Horario VARCHAR(20),Capacete VARCHAR(20),protAuricular VARCHAR(20),Luvas VARCHAR(20),Colete VARCHAR(20),Botas VARCHAR(20),Mascara VARCHAR(20));"
        c.execute(sql)
        con.close()
        return
def CREATE_TABLE(tabela):
    print("fgbfbfb\n\n\n\n\n"+str(tabela))
    CONECT()
    with con.cursor() as c:
        sql="USE cepegdb"
        c.execute(sql)
        sql=f"CREATE TABLE {tabela[3]}("
        for x in range(0,len(tabela),1):
            if(x!=3):
                sql=sql+f"{tabela[x]} VARCHAR(20)"
                if(x!=(len(tabela)-1)):
                    sql=sql+","
        sql=sql+");"
        c.execute(sql)
        con.commit()
    con.close()
    CONECT()
    with con.cursor() as c:
        tabela.remove("Id")
        tabela.remove("Nome")
        ps1=tabela[1]
        tabela[0]=ps1
        tabela[1]=f"\'{data.day}/{data.month}/{data.year} - {data.hour}h {data.minute}m\'"
        sizeTABELA=len(tabela)
        sizeEPIs=len(listEPIs)
        sql="INSERT INTO setores(Setor,Horario,Capacete,protAuricular,Luvas,Colete,Botas,Mascara)VALUES("
        VALUES=[f"\'{tabela[0]}\'",tabela[1],"\'Não Cadastrado\'","\'Não Cadastrado\'","\'Não Cadastrado\'","\'Não Cadastrado\'","\'Não Cadastrado\'","\'Não Cadastrado\'"]
        for y in range(2,sizeTABELA,1):
            for w in range(2,sizeEPIs,1):
                if str(tabela[y])==str(listEPIs[w]):
                    VALUES[w]="\'Cadastrado\'"
        for s in range(0,len(VALUES),1):
            sql=sql+VALUES[s]
            if(s!=(len(VALUES)-1)):
                sql=sql+","
        sql=f"{sql});"
        print(sql)
        c.execute(sql)
        con.commit()
    con.close()
    return
def INSERT_FUNC(setores,nomeFunc):
    CONECT()
    with con.cursor() as c:
        varId=None
        maxId=None
        sql="SELECT MAX(Id) FROM funcionarios"
        c.execute(sql)
        maxId=c.fetchone()
        if(maxId["MAX(Id)"]==None):
            varId=0
        else:
            varId=maxId["MAX(Id)"]+1
        sql="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'funcionarios\'"
        c.execute(sql)
        COLUMNS_NAME=c.fetchall()
        sizeCN=len(COLUMNS_NAME)
        sizeSETORES=len(setores)
        sql=f"INSERT INTO funcionarios("
        for y in range(0,sizeCN,1):
            sql=sql+f"{COLUMNS_NAME[y]['COLUMN_NAME']}"
            if(y!=(sizeCN-1)):
                sql=sql+","
        sql=sql+f")VALUES({varId},\'{nomeFunc}\',\'{data.day}/{data.month}/{data.year} - {data.hour}h {data.minute}m\',\'"
        for w in range(0,sizeSETORES,1):
            sql=sql+f"{setores[w]}"
            if(w!=(sizeSETORES-1)):
                sql=sql+"-"
        sql=sql+"\');"
        c.execute(sql)
        con.commit()
    con.close()
    return
def SETORES():
    CONECT()
    global listSetores
    with con.cursor() as c:
        sql="SHOW TABLES FROM cepegdb"
        c.execute(sql)
        tabelas=c.fetchall()
        sizeTABELAS=len(tabelas)
        listTabelas=[]
        for x in range(0,sizeTABELAS,1):
            listTabelas.append(tabelas[x]['Tables_in_cepegdb'])
    con.close()
    print(listTabelas)
    return listTabelas
def LINHAS(infoT):
    CONECT()
    with con.cursor() as c:
        sql=f"SELECT * FROM {infoT}"
        if (infoT!="setores"):
            sql=sql+" order by ID"
        c.execute(sql)
        linhas=c.fetchall()
    con.close()
    print("\n\n\n\n\n============\n"+str(linhas))
    return linhas
def TABELA(infoT):
    CONECT()
    with con.cursor() as c:
        sql=f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'{infoT}\'"
        c.execute(sql)
        COLUMNS_NAME=c.fetchall()
        print("\n\n\n\n"+str(COLUMNS_NAME))
    con.close()
    return COLUMNS_NAME
