#Inicio da função cachorro_peso()
def cachorro_peso():
    #Layout do Menu de valor com base no peso
    print('-' * 23, 'MENU 1 DE 3 - Peso do Cachorro', '-' * 23, "\n" +
          '|               PESO(Kg)               |              VALOR BASE             |\n'+
          '|               Até 3Kg                |               R$ 40,00              |\n'+
          '|             De 3 até 10Kg            |               R$ 50,00              |\n'+
          '|             De 10 até 30Kg           |               R$ 60,00              |\n'+
          '|             De 30 até 50Kg           |               R$ 70,00              |\n'+
          '-' * 78)

    base = 0 #retornará o valor base de acordo com o peso do cachorro

    #Inicio do loop
    while True:
        try:
            pesoC = int(input('Digite o peso do cachorro (Kg): '))
            if (pesoC >= 1) and (pesoC < 3): # >=1 para evitar que a pessoa coloque números negativos
                return base + 40
            elif (pesoC >= 3) and (pesoC < 10):
                return base + 50
            elif (pesoC >= 10) and (pesoC < 30):
                return base + 60
            elif (pesoC >= 30) and (pesoC < 50):
                return base + 70
            else:
                print('Não aceitamos cachorro nesse peso.')
                continue #retorna ao inicio do loop
        except ValueError:
            print('Você digitou um valor não númerico. Tente novamente.')
#Fim da função cachorro_peso()

#Inicio da função cachorro_pelo()
def cachorro_pelo():
    print('-' * 23, 'MENU 2 DE 3 - Tamanho do Pelo', '-' * 24, '\n'+
          '|                Curto (c)               |               1.0x                |\n'+
          '|                Médio (m)               |               1.5x                |\n'+
          '|                Longo (l)               |               2.0x                |\n'+
          '-' *78)
    #Inicio do loop
    while True:
        peloC = input('Digite o tamanho do pelo do cachorro: ')
        peloC = peloC.lower() #transforma qualquer string em minusculo
        peloC = peloC.strip() #tira o espaço caso o usuário digite sem querer
        if peloC == 'c':
            return 1.00
        elif peloC == 'm':
            return 1.5
        elif peloC == 'l':
            return 2.00
        else:
            print('Valor não encontrado. Escolha uma das opções disponíveis.')
            continue #retorna ao inicio do loop
#Fim da função cachorro_pelo()

#Inicio da função cachorro_extra()
def cachorro_extra():
    print('-' * 28, 'MENU 3 DE 3 - Extras', '-' * 28)
    acumulador = 0  #Receberá o total dos valores extras solicitados e retornará ao main

    #Inicio do loop
    while True:
        extraC = input('Deseja algum opcional? \n'+
                       '1 - Corte de unhas - R$ 10,00 \n'+
                       '2 - Escovar os dentes - R$ 12,00 \n'+
                       '3 - Limpar as orelhas - R$ 15,00 \n'+
                       '0 - Não quero mais nada \n'+
                       '>>')
        if extraC == '0':
            return acumulador #Após todos os extras solicitados retornará ao main com o total
        elif extraC == '1':
            acumulador += 10
        elif extraC == '2':
            acumulador += 12
        elif extraC == '3':
            acumulador += 15
        else:
            print('Valor não encontrado. Tente novamente...')
#Fim da função cachorro_extra()

#Inicio da Main
print('-' * 15, 'Bem-vindo ao PetShop de Felipe Beluci Tonelote', '-' * 15)

base = cachorro_peso()
multiplicador = cachorro_pelo()
extra =cachorro_extra()

total = base * multiplicador + extra #calculo do valor total do cliente

print('Valor com base no peso do cachorro: R$ {:.2f}. Tamanho do pelo: {}x. Adicional(is): R$ {:.2f}'.format(base, multiplicador, extra))
print('Valor total a ser pago: R$ {:.2f}'.format(total))