#calcule o preco a pagar pelo fornecimento de energia

kwh = float(input('Quantos kWh foram consumidos: '))
tipo = input('Tipo de instalação (R = Residencial / C = Comercial / I = Industrial):')

if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6
else:
    print('Instalação Inválida')

print('Total a pagar: {}'.format(kwh * preco))