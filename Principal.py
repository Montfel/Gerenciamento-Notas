from Classe import Professor, Aluno, Disciplina, Nota

listaProf = []
listaAluno = []
listaDisc = []
listaNota = []

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
        Professor.impressao(professor)
        listaProf.append(professor)

    elif escolha == '2':
        aluno = Aluno()
    
    elif escolha == '3':
        disciplina = Disciplina()
    
    elif escolha == '4':
        nota = Nota()

    elif escolha == '5':
        # Teste
        buscaProf = input('\nQual matricula do Prof. : ')

        for i in range(len(listaProf)):
            if listaProf[i].matricula == buscaProf:
                Professor.impressao(listaProf[i])

    else:
        print('\nOpção invalida! Digite novamente.')
