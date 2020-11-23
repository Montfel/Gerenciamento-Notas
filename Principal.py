import pandas as pd
from Classe import Professor, Aluno, Disciplina, Nota
from Funcao import buscarDisciplina, buscarProfessor, voltarMenu, criarDataFrame, adicionarDataFrame

try:
    open('N1.xlsx', 'r')
    File = True
except IOError:
    File = False
    print('Criando novo arquivo...')
    criarDataFrame()

listaProf = []
listaAluno = []
listaDisc = []
listaNota = []
notas = []
alunos = []

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
        print('\nFim do programa.')
        break

    elif escolha == '1':
        professor = Professor()
        # Teste
        if not File:
            print('1 →')
            # criarDataFrame(professor.nome, professor.matricula, professor.data_nascimento)
            adicionarDataFrame(professor.nome, professor.matricula, professor.data_nascimento)
        elif File:
            print('2 ←')
            adicionarDataFrame(professor.nome, professor.matricula, professor.data_nascimento)

        listaProf.append(professor)

    elif escolha == '2':
        aluno = Aluno()
        listaAluno.append(aluno)

    elif escolha == '3':
        disciplina = Disciplina()
        listaDisc.append(disciplina)

    elif escolha == '4':
        nota = Nota()
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
