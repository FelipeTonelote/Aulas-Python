print('Bem-vindo a sorveteria de Felipe Beluci Tonelote')

# Visual do Cardápio
print('-' * 37 + 'Cardápio' + '-' * 37)
print('| N° de bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)|')
print('|      1      |         R$ 6,00        |       R$ 7,00      |       R$ 8,00      |')
print('|      2      |         R$ 10,00       |       R$ 12,00     |       R$ 14,00     |')
print('|      3      |         R$ 14,00       |       R$ 17,00     |       R$ 20,00     |')
print('----------------------------------------------------------------------------------')

acumulador = 0
while True:
     # entrando com o sabor desejado e invalidando caso a pessoa digite outra coisa
     sabor = input('Qual sabor deseja? (tr/pr/es) ')
     sabor = sabor.upper()  #para não ter problema caso a pessoa digite maiusculo ou minúsculo
     if sabor != 'TR' and sabor != 'PR' and sabor != 'ES':
          print('Sabor inválido. Tente novamente')
          continue

     # entrando com a quantidade desejada e invalidando caso a pessoa digite outra coisa
     qtd_bolas = int(input('Quantas bolas de sorvete gostaria? (1,2,3) '))
     if qtd_bolas != 1 and qtd_bolas != 2 and qtd_bolas != 3:
          print('Quantidade inválida. Tente novamente')
          continue

     #conferindo o que o cliente pediu e acumular para o preço final
     if sabor == 'TR' and qtd_bolas == 1:
          print('Você escolheu o sabor TRADICIONAL com 1 bola de sorvete')
          acumulador += 6

     elif sabor == 'TR' and qtd_bolas == 2:
          print('Você escolheu o sabor TRADICIONAL com 2 bolas de sorvete')
          acumulador += 10

     elif sabor == 'TR' and qtd_bolas == 3:
          print('Você escolheu o sabor TRADICIONAL com 3 bolas de sorvete')
          acumulador += 14

     elif sabor == 'PR' and qtd_bolas == 1:
          print('Você escolheu o sabor PREMIUM com 1 bolas de sorvete')
          acumulador += 7

     elif sabor == 'PR' and qtd_bolas == 2:
          print('Você escolheu o sabor PREMIUM com 2 bolas de sorvete')
          acumulador += 12

     elif sabor == 'PR' and qtd_bolas == 3:
          print('Você escolheu o sabor PREMIUM com 3 bolas de sorvete')
          acumulador += 17

     elif sabor == 'ES' and qtd_bolas == 1:
          print('Você escolheu o sabor ESPECIAL com 1 bolas de sorvete')
          acumulador += 8

     elif sabor == 'ES' and qtd_bolas == 2:
          print('Você escolheu o sabor ESPECIAL com 2 bolas de sorvete')
          acumulador += 14

     else:
          print('Você escolheu o sabor ESPECIAL com 3 bolas de sorvete')
          acumulador += 20

     # mensagem informando se o cliente deseja mais alguma coisa.
     pedir_mais = input('Deseja pedir mais algum sorverte (Sim = S / Não = Outra tecla): ')
     pedir_mais = pedir_mais.upper()
     # Valindo se caso sim: o programa retorna. Ou caso não: o programa encerra
     if pedir_mais == 'S':
          continue
     else:
          print('Valor a ser pago: R${:.2f}'.format(acumulador))
          break

