from datetime import date


class Professor:
    nome = ''
    matricula = ''
    data_nascimento = date

    def __init__(self):
        self.cadastrar()
    
    def cadastrar(self):
        while True:
            try:
                self.matricula = input('\nInforme a matrícula do professor: ')
                assert self.matricula.isnumeric()

                # medico_existe, none, medicos = verificarDado('medicos.txt', self.crm)

                # if medico_existe:
                #     print('\nEste médico já existe.')
                #     raise OverflowError

                self.nome = input('\nInforme o nome do professor: ').strip().capitalize()
                assert len(self.nome) >= 1

                data = input('\nInforme a data de nascimento do professor (DD/MM/AAAA): ')
                self.data_nascimento = date(int(data[6:]), int(data[3:5]), int(data[:2]))
                print(self.nome)
                print(self.matricula)
                print(self.data_nascimento)
                # assert self.cpf.isnumeric() and len(self.cpf) == 11

                # medicos.append([self.crm, self.nome, self.cpf, self.sexo, self.status])
                # subirDadosParaArquivo('medicos.txt', medicos)
                print('\nMédico cadastrado.')
                break

            except (OverflowError, AssertionError):
                voltar = voltarMenu()
                if voltar.casefold() == 's':
                    return None
        


class Aluno:
    nome = ''
    matricula = ''
    data_nascimento = date

    def __init__(self, nome, matricula, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento


class Disciplina:
    codigo = ''
    nome = ''
    matricula_professor = ''
    
    def __init__(self, codigo, nome, matricula_professor):
        self.codigo = codigo
        self.nome = nome
        self.matricula_professor = matricula_professor


class Nota:
    codigo_disciplina = ''
    matricula_aluno = ''
    nota1 = 0.0
    nota2 = 0.0
    
    def __init__(self, codigo, nome, matricula_professor):
        self.codigo = codigo
        self.nome = nome
        self.matricula_professor = matricula_professor
