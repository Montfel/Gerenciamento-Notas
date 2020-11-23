import pandas as pd
from datetime import date

lista_de_professores = []
class Professor:

    def __init__(self,nome,matricula,data_de_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.data_de_nascimento = data_de_nascimento
    
    def __str__(self):
        return f'Nome: {self.nome}\nMatricula: {self.matricula}\nData de nascimento: {self.data_de_nascimento}'
dados = pd.read_excel('dataframe_prof.xlsx')
print(dados)


##Pegar do dataframe e tratar em memória
for i in range(len(dados)):
    nome = dados.loc[i][0]
    matricula = dados.loc[i][1]
    data_de_nascimento = dados.loc[i][2]
    professor = Professor(nome,matricula,data_de_nascimento)
    lista_de_professores.append(professor)

#Passar da memória pro dataframe
i = 0
for professores in lista_de_professores:
    linha = [professores.nome,professores.matricula,professores.data_de_nascimento]
    dados.loc[i] = linha
    i += 1
excel_reader = pd.ExcelFile('dataframe_prof.xlsx')
excel_writer = pd.ExcelWriter('dataframe_prof.xlsx')
dados.to_excel(excel_writer,'Plan1',index=False)
excel_writer.save()