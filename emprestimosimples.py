emprestimo = input('digite o valor do emprestimo: ')
renda = input('digite valor da sua renda: ')

if not emprestimo.isnumeric():
    print('não podemos fazer esse tipo de operação: ')
else:
    emprestimo = int(emprestimo)
    renda = int(renda)
    calculo1 = (emprestimo * renda/4)
    calculo2 = (calculo1 >= renda and calculo1 <= renda)

    msg = 'emprestimo aprovado' if  calculo2 else 'emprestimo recusado'
    print(msg)