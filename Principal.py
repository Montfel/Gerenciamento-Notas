from Classe import Professor, Aluno, Disciplina, Nota
from Funcao import buscarDisciplina, buscarProfessor, voltarMenu, criarDataFrame, \
    salvarDataframe, getDataFramefromExcel

try:
    open('N1.xlsx', 'r')

except IOError:
    print('Criando novos arquivos...')
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
                buscaDisc = int(input('\nInforme o código da Disciplina: '))

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
