from datetime import date
from Funcao import voltarMenu


class Professor:
    nome = ''
    matricula = ''
    data_nascimento = date

    def __init__(self):
        while True:
            try:
                self.matricula = input('\nInforme a matrícula do professor: ')
                assert self.matricula.isnumeric()

                self.nome = input('\nInforme o nome do professor: ').strip().capitalize()
                assert len(self.nome) >= 1

                data = input('\nInforme a data de nascimento do professor (DD/MM/AAAA): ')
                self.data_nascimento = date(int(data[6:]), int(data[3:5]), int(data[:2]))

                print('\nProfessor cadastrado.')
                break

            except (AssertionError, ValueError):
                voltar = voltarMenu()
                if voltar.casefold() == 's':
                    break

    def impressao(self):
        print(f'Nome: {self.nome}'
              f' - Matricula: {self.matricula}'
              f' - Data de nascimento: {self.data_nascimento}')

    def getNome(self):
        print(self.nome)


class Aluno:
    nome = ''
    matricula = ''
    data_nascimento = date

    def __init__(self):
        while True:
            try:
                self.matricula = input('\nInforme a matrícula do aluno: ')
                assert self.matricula.isnumeric()

                self.nome = input('\nInforme o nome do aluno: ').strip().capitalize()
                assert len(self.nome) >= 1

                data = input('\nInforme a data de nascimento do aluno (DD/MM/AAAA): ')
                self.data_nascimento = date(int(data[6:]), int(data[3:5]), int(data[:2]))

                print('\nAluno cadastrado.')
                break

            except (AssertionError, ValueError):
                voltar = voltarMenu()
                if voltar.casefold() == 's':
                    break

    def impressao(self):
        print(f'Nome: {self.nome}'
              f' - Matricula: {self.matricula}'
              f' - Data de nascimento: {self.data_nascimento}')


class Disciplina:
    codigo = ''
    nome = ''
    matricula_professor = ''
    
    def __init__(self):
        while True:
            try:
                self.codigo = input('\nInforme o código da disciplina: ')
                assert self.codigo.isnumeric()

                self.nome = input('\nInforme o nome da disciplina: ').strip().capitalize()
                assert len(self.nome) >= 1

                self.matricula_professor = input('\nInforme a matrícula do professor: ')
                assert self.matricula_professor.isnumeric()

                print('\nDisciplina cadastrada.')
                break

            except AssertionError:
                voltar = voltarMenu()
                if voltar.casefold() == 's':
                    break

    def relatorioNotas(self, professor):
        print(f'\nNome: {self.nome}'
              f'\nMatrícula do professor: {self.matricula_professor}'
              f'\nNome do Professor: {Professor.getNome(professor)}')


class Nota:
    codigo_disciplina = ''
    matricula_aluno = ''
    nota1 = 0.0
    nota2 = 0.0
    
    def __init__(self):
        while True:
            try:
                self.codigo_disciplina = input('\nInforme o código da disciplina: ')
                assert self.codigo_disciplina.isnumeric()
                
                self.matricula_aluno = input('\nInforme a matrícula do aluno: ')
                assert self.matricula_aluno.isnumeric()

                self.nota1 = float(input('\nInforme a primeira nota: '))
                assert 0 <= self.nota1 <= 10

                self.nota2 = float(input('\nInforme a segunda nota: '))
                assert 0 <= self.nota2 <= 10

                print('\nNotas cadastradas.')
                break

            except AssertionError:
                voltar = voltarMenu()
                if voltar.casefold() == 's':
                    break

    def calcularMedia(self):
        print((self.nota1 * self.nota2) / 2)
        return (self.nota1 * self.nota2) / 2
    
    def impressao(self):
        print(f'Codigo da disciplina: {self.codigo_disciplina}'
              f' - Matrícula do aluno: {self.matricula_aluno}'
              f' - Nota 1: {self.nota1}'
              f' - Nota 2: {self.nota2}')


