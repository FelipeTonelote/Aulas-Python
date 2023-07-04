#exibindo a tela de boas-vindas
print('Bem-vindo a Loja do Felipe Tonelote')
#declaração das variáveis
valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Digite a quantidade do produto: '))
desconto_produto = 0

#teste das quantidades
if (qtd_produto < 200):
    desconto_produto = 0.0 # 0% = 0.0
elif (qtd_produto >= 200) and (qtd_produto < 1000):
    desconto_produto = 0.05 # 5% = 0.05
elif (qtd_produto >= 1000) and (qtd_produto < 2000):
    desconto_produto = 0.1 # 10% = 0.1
else:
    desconto_produto = 0.15 # 15% = 0.15

#calculo do desconto
valor_sem_desconto = valor_produto * qtd_produto
valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto_produto)

#mostragem na tela o resultado final
print('O valor SEM desconto é: R$ {:.2f}'.format(valor_sem_desconto))
print('O valor COM desconto é: R$ {:.2f}'.format(valor_com_desconto))