#codigo que mostra apenas os dois ultimos caracteres da metade da frase digitada

frase = input('Digite uma frase: ')
tamanho = len(frase)

frase2 = frase[:int(tamanho/2)]
print(frase2[-2:])