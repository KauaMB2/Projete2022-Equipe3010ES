import json
import serial
def cadastrar(nome_funcionario):
    return
    # ser = serial.Serial("COM4")
    # valor = "C"
    # cadastroIniciado = False
    # id_recebido = False
    # while True:
    #     ser.write(valor.encode())

    #     if ser.readline().decode("utf-8") == "cadastrar\r\n":
    #         cadastroIniciado = True

    #     if cadastroIniciado == True:
    #         print("Cadastro iniciado")
    #         # nome_funcionario = input("Digite o nome do funcionário: ")

    #         with open("json/funcionarios_id_biometria.json", encoding="utf-8") as json_ids:
    #             json_ids_funcionarios = json.load(json_ids)

    #         lista_ids_cadastradas = list(json_ids_funcionarios.keys())

    #         for id in lista_ids_cadastradas:
    #             id = int(id)

    #         id = id + 1
    #         id = str(id)

    #         json_ids_funcionarios[id] = nome_funcionario

    #         enviar_id_funcionario = json.dumps(json_ids_funcionarios, indent=4)

    #         with open("json/funcionarios_id_biometria.json", "w") as json_ids:
    #             json_ids.write(enviar_id_funcionario)

    #         while True:
    #             ser.write(id.encode())

    #             if ser.readline().decode("utf-8") == "id_ok\r\n":
    #                 print("id_recebido")
    #                 id_recebido = True

    #                 while True:
    #                     if(ser.readline().decode("utf-8") == "cadastrado\r\n"):
    #                         print("Digital cadastrada!")                        
    #                         break
    #                 break

    #     if id_recebido == True:
    #         break
