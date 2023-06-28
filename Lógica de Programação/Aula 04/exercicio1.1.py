#OUTRA FORMA DE FAZER A CALCULADORA

#CALCULADORA SIMPLES COM OPCAO DE SAIR

print('CALCULADORA')
print('Adição: +')
print('Subtração: -')
print('Multiplicação: *')
print('Divisão: /')
print('Digite s para sair')

while True:
    op = input('Qual operação deseja fazer? ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = float(input('Digite o primeiro valor: '))
        y = float(input('Digite o segundo valor: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x , y, res))
        continue #opcional, apenas para agilizar no desempenho
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif (op == 's'):
        break
    else:
        print('Operação Inválida')


print('Encerrando o programa...')



