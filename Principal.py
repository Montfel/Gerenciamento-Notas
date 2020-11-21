from Classe import Professor, Aluno, Disciplina, Nota
# from Funcao import relacaoAlunos

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
        listaProf.append(professor)

    elif escolha == '2':
        aluno = Aluno()
        listaAluno.append(aluno)
    
    elif escolha == '3':
        disciplina = Disciplina()
        listaDisc.append(disciplina)
    
    elif escolha == '4':
        nota = Nota()
        Nota.calcularMedia(nota)
        listaNota.append(nota)

    elif escolha == '5':
        buscaDisc = input('\nInforme o código da Disciplina: ')

        # Melhorar!
        for i in range(len(listaDisc)):
            if listaDisc[i].codigo == buscaDisc:
                disciplina = listaDisc[i]

        for i in range(len(listaProf)):
            if listaProf[i].matricula == disciplina.matricula_professor:
                professor = listaProf[i]

        for i in range(len(listaNota)):
            if listaNota[i].codigo_disciplina == disciplina.codigo:
                notas.append(listaNota[i])
            # if listaAluno[i].matricula == listaNota[i].matricula_aluno:
            #     alunos.append(listaAluno[i])

        Disciplina.relatorioNotas(disciplina, professor, notas)

    else:
        print('\nOpção invalida! Digite novamente.')
