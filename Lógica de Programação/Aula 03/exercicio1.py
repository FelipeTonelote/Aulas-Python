#faça um algoritmo que receba 3 valores de lados do triangulo e verifica se é um triangulo equilatero, isosceles ou escaleno.

A = int(input('Digite o 1° lado do triângulo: '))
B = int(input('Digite o 2° lado do triângulo: '))
C = int(input('Digite o 3° lado do triângulo: '))

if (A > 0) and (B > 0) and (C > 0) :
    if A + B > C and B + C > A and A + C > B:
    # Se chegou até aqui, quer dizer que o triangulo é válido!
        if A != B and A != C and B != C :
            print('Triângulo Escaleno')
        else:
            if A == B and A == C and B == C:
                print('Triângulo Equilatero')
            else:
                print('Triângulo Isósceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')