#Uma funcao que calcule o fatorial de um número recebido e retorne seu resultado
#Valide os dados por meio de outra funcao, só valores positivos serao aceitos
#Crie um help da funcao

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial(num):
    """
    Calcula a fatorial
    :param num: número coletado pelo input de x
    :return: retorna o valor da conta de fatorial
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

# PROGRAMA PRINCIPAL
x = valida_int('Digite um valor para calcular o fatorial: ', 0, 999999)
print('{}! = {}'.format(x, fatorial(x)))
help(fatorial)