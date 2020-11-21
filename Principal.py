from Classe import Professor, Aluno, Disciplina, Nota
# from Funcao import relacaoAlunos

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
                for j in range(len(listaProf)):
                    if listaProf[j].matricula == listaDisc[i].matricula_professor:
                        for h in range(len(listaNota)):
                            if listaNota[h].codigo_disciplina == listaDisc[i].codigo:
                                for x in range(len(listaAluno)):
                                    if listaNota[h].matricula_aluno == listaAluno[x].matricula:
                                        Disciplina.relatorioNotas(listaDisc[i], listaProf[j], listaNota[h], listaAluno[x])

    else:
        print('\nOpção invalida! Digite novamente.')
