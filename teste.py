import pandas as pd
df = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento']) #Dataframe Professor
df2 = pd.DataFrame(columns=['Nome', 'Matricula', 'Data de Nascimento'])#Dataframe Aluno
df3 = pd.DataFrame(columns=['Codigo', 'Nome', 'Matricula do professor'])#Dataframe Disciplinas
df4 = pd.DataFrame(columns=['Codigo da Disciplina', 'Matrícula do aluno', 'Nota 1', 'Nota 2'])#Dataframe Notas
df.to_excel('N1.xlsx', 'Plan1',index=False)
df2.to_excel('N2.xlsx', 'Plan1',index=False)
df3.to_excel('N3.xlsx', 'Plan1',index=False)
df4.to_excel('N4.xlsx', 'Plan1',index=False)