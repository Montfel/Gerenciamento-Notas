import pandas as pd
from datetime import date
from openpyxl import Workbook
import Classe

def buscarDisciplina(busca, listaDisc):
    for i in range(len(listaDisc)):
        if listaDisc[i].codigo == busca:
            return listaDisc[i]

    return False


def buscarProfessor(disciplina, listaProf):
    for i in range(len(listaProf)):
        if listaProf[i].matricula == disciplina.matricula_professor:
            return listaProf[i]

    return False


#
# for i in range(len(listaNota)):
#     if listaNota[i].codigo_disciplina == disciplina.codigo:
#         notas.append(listaNota[i])
#     # if listaAluno[i].matricula == listaNota[i].matricula_aluno:
#     #     alunos.append(listaAluno[i])


def voltarMenu():
    while True:
        try:
            voltar = input('\nInformação inválida! Deseja voltar para o Menu? [S/N] ').strip()[0]
            assert voltar.casefold() == 's' or voltar.casefold() == 'n'
            return voltar

        except (AssertionError, IndexError):
            print('\nOpção inválida! Informe "SIM" ou "NÃO".')


def criarDataFrame():
    df = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento']) #Dataframe Professor
    df2 = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])#Dataframe Aluno
    df3 = pd.DataFrame(columns=['Codigo', 'Nome', 'Matricula do professor'])#Dataframe Disciplinas
    df4 = pd.DataFrame(columns=['Codigo da Disciplina', 'Matrícula do aluno', 'Nota 1', 'Nota 2'])#Dataframe Notas
    df.to_excel('N1.xlsx', 'Plan1',index=False)
    df2.to_excel('N2.xlsx', 'Plan1',index=False)
    df3.to_excel('N3.xlsx', 'Plan1',index=False)
    df4.to_excel('N4.xlsx', 'Plan1',index=False)



def salvarDataframe(df,df2,df3,df4,lista_de_professores,lista_de_alunos,lista_de_disciplinas,lista_de_notas):
    
    i = 0
    dados = pd.read_excel('N1.xlsx')
    for professor in lista_de_professores:
        linha = [professor.nome,professor.matricula,professor.data_nascimento]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('N1.xlsx')
    dados.to_excel(excel_writer,'Plan1',index=False)
    excel_writer.save()

    i = 0
    dados = pd.read_excel('N2.xlsx')
    for aluno in lista_de_alunos:
        linha = [aluno.nome,aluno.matricula,aluno.data_nascimento]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('N2.xlsx')
    dados.to_excel(excel_writer,'Plan1',index=False)
    excel_writer.save()

    i = 0
    dados = pd.read_excel('N3.xlsx')
    for disciplina in lista_de_disciplinas:
        linha = [disciplina.codigo,aluno.nome,aluno.matricula_professor]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('N3.xlsx')
    dados.to_excel(excel_writer,'Plan1',index=False)
    excel_writer.save()

    i = 0
    dados = pd.read_excel('N4.xlsx')
    for nota in lista_de_notas:
        linha = [nota.codigo_disciplina,nota.matricula_aluno,nota.nota1,nota.nota2]
        dados.loc[i] = linha
        i += 1
    excel_writer = pd.ExcelWriter('N4.xlsx')
    dados.to_excel(excel_writer,'Plan1',index=False)
    excel_writer.save()

def getDataFramefromExcel(df,df1,df2,df4,lista_de_professores,lista_de_alunos,lista_de_disciplinas,lista_de_notas):
    #Professor
    dados = pd.read_excel('N1.xlsx')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        matricula = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        professor = Classe.Professor(nome,matricula,data_nascimento)
        lista_de_professores.append(professor)
    #Aluno
    dados = pd.read_excel('N2.xlsx')
    for i in range(len(dados)):
        nome = dados.loc[i][0]
        matricula = dados.loc[i][1]
        data_nascimento = dados.loc[i][2]
        aluno = Classe.Aluno(nome,matricula,data_nascimento)
        lista_de_alunos.append(aluno)
    #Disciplina
    dados = pd.read_excel('N3.xlsx')
    for i in range(len(dados)):
        codigo = dados.loc[i][0]
        nome = dados.loc[i][1]
        matricula_aluno = dados.loc[i][2]
        disciplina = Classe.Disciplina(codigo,nome,matricula)
        lista_de_disciplinas.append(disciplina)
    #Notas
    dados = pd.read_excel('N4.xlsx')
    for i in range(len(dados)):
        codigo_do_aluno = dados.loc[i][0]
        matricula_aluno = dados.loc[i][1]
        nota1 = dados.loc[i][2]
        nota2 = dados.loc[i][3]
        notas = Classe.Disciplina(codigo_do_aluno,matricula_aluno,nota1,nota2)
        lista_de_notas.append(notas)