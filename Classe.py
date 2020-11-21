from datetime import date
class Professor:
    Nome = ''
    Matricula = ''
    Data_nascimento = date

    def __init__(self, nome, matricula, data_nascimento):
        self.Nome = nome
        self.Matricula = matricula
        self.Data_nascimento = data_nascimento

class Aluno:
    Nome = ''
    Matricula = ''
    Data_nascimento = date

    def __init__(self, nome, matricula, data_nascimento):
        self.Nome = nome
        self.Matricula = matricula
        self.Data_nascimento = data_nascimento

class Disciplina:
    Codigo = ''
    Nome = ''
    Matricula_professor = ''
    
    def __init__(self, codigo, nome, matricula_professor):
        self.Codigo = codigo
        self.Nome = nome
        self.Matricula_professor = matricula_professor

class Nota:
    Codigo_disciplina = ''
    Matricula_aluno = ''
    Nota1 = 0.0
    Nota2 = 0.0
    
    def __init__(self, codigo, nome, matricula_professor):
        self.Codigo = codigo
        self.Nome = nome
        self.Matricula_professor = matricula_professor