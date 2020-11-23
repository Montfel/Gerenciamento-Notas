import pandas as pd
import datetime


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


def addColunaDataFrame():
    Notas = pd.read_excel('Notas.xlsx')
    Notas.insert(loc=0, column='Nome')
    Notas.insert(loc=1, column='Matrícula')
    Notas.insert(loc=2, column='Data de Nascimento')


def adicionarDataFrame(nome, matricula, data):
    dataframe = pd.read_excel('Notas.xlsx')
    # date = datetime.datetime(2008, 1, 31)
    date = data
    # linha = ['Gabriel', '111.111.111-11', date, '11.111.111-1', 'Aracaju']
    linha = [nome, matricula, date]
    dataframe.loc[len(dataframe)] = linha
    print(dataframe)


def alterarDataFrame():
    dataframe = pd.read_excel('Notas.xlsx')
    dataframe.drop(index=[0], inplace=True)
    data = datetime.datetime(2008, 1, 31)
    linha = [11111111121, "Mariana", data, "Inativo"]
    dataframe.loc[len(dataframe)] = linha
    print(dataframe)
    return dataframe


def saveExcel():
    dataframe = alterarDataFrame()
    excel_reader = pd.ExcelFile('Notas.xlsx')
    to_update = {"Plan1": dataframe}
    # Criar objeto para escrita
    excel_writer = pd.ExcelWriter('Notas.xlsx')

    # Loop para o caso de querer trabalhar com mais de uma planilha
    for sheet in excel_reader.sheet_names:
        sheet_df = excel_reader.parse(sheet)
        append_df = to_update.get(sheet)
        # Concatenar com o que já existia
        if append_df is not None:
            sheet_df = dataframe
        # Gravar no arquivo
        sheet_df.to_excel(excel_writer, sheet, index=False)
    # Salvar e fechar arquivo
    excel_writer.save()
