nome = input('seu nome por gentileza: ')
idade = int(input('sua idade por favor: '))
renda = float(input('valor do seu salario: '))
empréstimo = float(input('valor do emprestimo: '))

som = renda * 30 / 100
if idade > 17 or som >= empréstimo:
    var = idade >= 18 and som > empréstimo
    print(f'{nome} foi aprovado')
else:
    print(f'{nome} foi negado')
