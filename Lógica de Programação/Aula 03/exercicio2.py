#algoritmo com dois valores e qual operacao o usuario vai querer

print('CALCULADORA')
print('Adição: +')
print('Subtração: -')
print('Multiplicação: *')
print('Divisão: /')

op = input('Qual operação deseja fazer? ')
if op == '+' or op == '-' or op == '*' or op == '/':  #caso alguem digite uma op invalida o programa ja encerra
    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))

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

print('Encerrando o programa...')