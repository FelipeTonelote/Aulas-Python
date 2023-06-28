#CALCULADORA SIMPLES COM OPCAO DE SAIR

print('CALCULADORA')
print('Adição: +')
print('Subtração: -')
print('Multiplicação: *')
print('Divisão: /')
print('Digite s para sair')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))

while (op != 's'):
    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x , y, res))
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
    else:
        print('Operação Inválida')

    op = input('Qual operação deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = float(input('Digite o primeiro valor: '))
        y = float(input('Digite o segundo valor: '))

print('Encerrando o programa...')