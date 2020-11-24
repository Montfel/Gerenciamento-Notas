import pandas as pd
from Classe import Professor, Aluno, Disciplina, Nota
from Funcao import buscarDisciplina, buscarProfessor, voltarMenu, criarDataFrame, \
    salvarDataframe, getDataFramefromExcel
# adicionarDataFrameNotas adicionarDataFrame
try:
    open('N1.xlsx', 'r')

except IOError:
    print('Criando novo arquivo...')
    criarDataFrame()

listaProf = []
listaAluno = []
listaDisc = []
listaNota = []
notas = []
alunos = []

getDataFramefromExcel(listaProf, listaAluno, listaDisc, listaNota)

while True:
    print('\nMenu da Escola\n\n'
          '1 - Cadastro de Professores\n'
          '2 - Cadastro de Alunos\n'
          '3 - Cadastro de Disciplinas\n'
          '4 - Cadastro de Notas\n'
          '5 - Relatório de Notas\n'
          '0 - Sair\n')

    escolha = input('Escolha uma das opções acima: ')

    if escolha == '0':
        salvarDataframe(listaProf, listaAluno, listaDisc, listaNota)
        print('\nFim do programa.')
        break

    elif escolha == '1':
        professor = Professor()
        # adicionarDataFrame(professor.nome, professor.matricula, professor.data_nascimento, 1)
        listaProf.append(professor)

    elif escolha == '2':
        aluno = Aluno()
        # adicionarDataFrame(aluno.nome, aluno.matricula, aluno.data_nascimento, 2)
        listaAluno.append(aluno)

    elif escolha == '3':
        disciplina = Disciplina()
        # adicionarDataFrame(disciplina.codigo, disciplina.nome, disciplina.matricula_professor, 3)
        listaDisc.append(disciplina)

    elif escolha == '4':
        nota = Nota()
        # adicionarDataFrameNotas(nota.codigo_disciplina, nota.matricula_aluno, nota.nota1, nota.nota2)
        listaNota.append(nota)

    elif escolha == '5':
        while True:
            try:
                buscaDisc = input('\nInforme o código da Disciplina: ')

                disc = buscarDisciplina(buscaDisc, listaDisc)
                assert disc is not False

                prof = buscarProfessor(disc, listaProf)

                for i in range(len(listaNota)):
                    if listaNota[i].codigo_disciplina == disc.codigo:
                        notas.append(listaNota[i])
                    # if listaAluno[i].matricula == listaNota[i].matricula_aluno:
                    #     alunos.append(listaAluno[i])

                Disciplina.relatorioNotas(disc, prof, notas)
                break

            except AssertionError:
                voltar = voltarMenu()
                if voltar.casefold() == 's':
                    break

    else:
        print('\nOpção invalida! Digite novamente.')
