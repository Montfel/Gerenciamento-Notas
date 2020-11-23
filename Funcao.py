import pandas as pd
from datetime import date


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
    df.to_excel('N1.xlsx')
    # print(df.head())


def adicionarDataFrame(nome, matricula, data):
    df = pd.read_excel('N1.xlsx')
    df.drop(columns=["Unnamed: 0"], inplace=True)
    # print(df)

    linha = [nome, matricula, data]
    df.loc[len(df)] = linha

    df.to_excel('N1.xlsx')

    print(df)
