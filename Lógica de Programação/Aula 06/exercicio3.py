#Programa para ler o nome, ano de nascimento e sexo de diferentes pessoas.
#Armazene os dados em um dicionário com listas.
#Ao encerrar o cadastro, apresente algumas informacoes.


cadastro = {'nome': [], 'sexo': [], 'ano': []}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() == 'N':
        break
    if terminar.upper() != 'S':
        print('Digite S para SIM ou N para NÃO.')
        continue

    nome = input('Qual o seu nome? ')
    sexo = input('Qual seu sexo [M/F]? ')
    ano = input('Qual seu ano de nascimento? ')
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

# Total de cadastros
total_cadastros = len(cadastro['nome'])
print('Total de cadastros efetuados:', total_cadastros)

# Média das idades
ano_atual = 2023  # Atualize com o ano atual
idades = [
    ano_atual - int(ano)
    for ano in cadastro['ano']]
media_idades = sum(idades) / total_cadastros
print('Média das idades:', media_idades)

# Lista de mulheres com menos de 30 anos
mulheres_menos_30 = [
    cadastro['nome'][i]
    for i in range(total_cadastros)
    if cadastro['sexo'][i] == 'F' and idades[i] < 30
]
print('Mulheres com menos de 30 anos:', mulheres_menos_30)

# Lista de homens com idade acima da média
homens_acima_media = [
    cadastro['nome'][i]
    for i in range(total_cadastros)
    if cadastro['sexo'][i] == 'M' and idades[i] > media_idades
]
print('Homens com idade acima da média:', homens_acima_media)
