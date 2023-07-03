#Algoritmo para cadastrar jogos
#Crie um menu de opções contendo: cadastrar, listar tudo e sair
#Uma funcao para cada item
#Armazenar todos os dados em um arquivo .txt salvos em disco

#Abrir arquivo: open()
#r : leitura
#w : escrita, apaga o conteúdo se ja existir
#a : escrita, mas preserva o conteúdo se ja existir
#b : modo binário
#+ : atualizacao (leitura e escrita)
#t : abrir arquivo .txt
# ...

#Fechar arquivo: arquivo.close()


def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def existe_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt') #leitura e abrir arquivo txt
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

#PROGRAMA PRINCIPAL

arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ',1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada... \n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de listar selecionada... \n')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...')
        break

