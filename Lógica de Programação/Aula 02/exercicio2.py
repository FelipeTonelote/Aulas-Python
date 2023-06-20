#escreva um programa que calcule a conta de um carro alugado. Diária: 50,00 e 0,15 por km rodado.

km = int(input('Quantos quilometros percorreu?: '))
dias = int(input('Por quantos dias ele foi alugado?: '))

preco = 60 * dias + 0.15 * km

print('Km = {}. Quantidade de dias = {}.'.format(km, dias))
print('O valor a ser pago é R${}'.format(preco))
