from datetime import date


class Professor:
    nome = ''
    matricula = ''
    data_nascimento = date

    def __init__(self, nome, matricula, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento


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
