#desenvola um algoritmo que solicite ao usuário um preco de um produto e um percentual de desconto a ser aplicado a ele.

preco = float(input('Qual é o preço do produto?: '))
p = float(input('Percentual de desconto (0-100)%: '))

desconto = preco * (p / 100)
final = preco - desconto

print('O preço do produto é {}.O percentual de desconto é {}%'.format(preco, p))  #forma moderna de inserir variavel na string
print('O valor de desconto é %.2f . O valor final do produto é %.2f' % (desconto, final)) #forma clássica de inserir variavel na string
