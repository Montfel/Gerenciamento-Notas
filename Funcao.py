import pandas as pd
from datetime import date
from openpyxl import Workbook


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
    df = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])
    df2 = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])
    df3 = pd.DataFrame(columns=['Codigo', 'Nome', 'Matricula do professor'])
    df4 = pd.DataFrame(columns=['Codigo da Disciplina', 'Matrícula do aluno', 'Nota 1', 'Nota 2'])
    df.to_excel('N1.xlsx', 'Plan1')
    df2.to_excel('N2.xlsx', 'Plan2')
    df3.to_excel('N3.xlsx', 'Plan3')
    df4.to_excel('N4.xlsx', 'Plan4')
    # print(df.head())


def adicionarDataFrame(parametro1, parametro2, parametro3, parametro4):
    df = pd.read_excel(f'N{parametro4}.xlsx')
    df.drop(columns=["Unnamed: 0"], inplace=True)
    # print(df)

    linha = [parametro1, parametro2, parametro3]
    df.loc[len(df)] = linha

    df.to_excel(f'N{parametro4}.xlsx', f'Plan{parametro4}')

    print(df)
