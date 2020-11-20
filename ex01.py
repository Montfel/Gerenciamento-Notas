nome_cliente = []
sexo = []
placa = []
qtd_km = []
qtd_dias = []
media = 0
while True:
    nome_cliente.append(input("Digite o nome do cliente: "))
    sexo.append(input('Digite o sexo: ').lower())
    placa.append(input('Digite a placa do carro: '))
    qtd_km.append(float(input('Digite a quantidade de km: ')))
    qtd_dias.append(int(input('Digite a quantidade de dias contratados: ')))
    sair = input('Deseja sair? Se sim, escreva SAIR: ').upper()
    if sair == 'SAIR':
        break
for i in range(len(nome_cliente)):
    print(f'Placa do carro: {placa[i]}')
    print(f'Valor a pagar: {qtd_km[i]*0.1 + qtd_dias[i]*70}')
    print()
print(f'Media de km contratados: {sum(qtd_km)/len(qtd_km):.2}')
print('O nome das clientes de sexo feminino que fecharam aluguéis acima de 7 dias contratados: ')
for i in range(len(nome_cliente)):
    if sexo[i] == 'f' and qtd_dias[i] > 7:
        print(nome_cliente[i])
print('Hello')