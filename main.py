import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythonDB"]
mycol = mydb["customers"]
arq_csv = open('C:/Users/thiag/PycharmProjects/pyMongo/boletins-de-servicos.csv', encoding='utf-8')

arq_reader = csv.reader(arq_csv, delimiter=';')

dictArq = {"BOLETIM": "", "TIPO": "", "PUBLICADO_EM": "", "ASSUNTO": ""}
arq_txt = open('C:/Users/thiag/PycharmProjects/pyMongo/boletins-de-servicos.txt', 'w+')



while(True):
    print("Digite [1] para ler o arquivo CSV \nDigite [2] para inserir dados manual \nDigite [3] para baixar os arquivos \nDigite [0] para sair")
    escolha = str(input("Digite o Menu que deseja entrar: "))

    # Adicionar o CSV no mongo
    if escolha == '1':
        for linha in arq_reader:
            dictArq = {"BOLETIM": linha[0], "TIPO": linha[1], "PUBLICADO_EM": linha[2], "ASSUNTO": linha[3]}
            x = mycol.insert_one(dictArq)


    #Adicionar manualmente no mongo
    if escolha == '2':
        while(True):
            boletim = str(input("Digite o BOLETIM: "))
            tipo = str(input("Digite o TIPO: "))
            publicado_em = str(input("Digite a DATA DE PUBLICAÇÃO: "))
            assunto = str(input("Digite o ASSUNTO: "))

            dictArq = {"BOLETIM": boletim, "TIPO": tipo, "PUBLICADO_EM": publicado_em, "ASSUNTO": assunto}
            x = mycol.insert_one(dictArq)

            sair = str(input("Digiter [s] para sair ou [n] para continuar: ")).lower()
            if sair == 's':
                break

    #Download dos dados para um arquivo TXT
    if escolha == '3':
        for result in mycol.find({}, {"_id": 1, "BOLETIM": 1, "TIPO": 1, "PUBLICADO_EM": 1, "ASSUNTO": 1}):
            result = str(result)
            arq_txt.write(result)
            arq_txt.write("\n\n")
        arq_txt.close()
        print("Arquivo Criado com Secesso")

    if escolha == '0':
        break
