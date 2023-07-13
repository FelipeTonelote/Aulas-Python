# ------Inicio das Variaveis Globais-----
lista_colaboradores = []
id_global = 0
# ------Fim das Variaveis Globais-----

# ------Inicio de cadastrar_colaborador(id)-----


def cadastrar_colaborador(id):
    print('*' * 64, '\n' +
          '-' * 18, 'MENU CADASTRAR COLABORADOR', '-' * 18)
    print('ID do Colaborador: {}'.format(id))
    nome = input('Digite o NOME do colaborador: ')
    setor = input('Digite o SETOR do colaborador: ')
    pagamento = int(input('Digite o PAGAMENTO(R$) do colaborador: '))
    dicionario_colaborador = {'id': id,
                              'nome': nome,
                              'setor': setor,
                              'pagamento': pagamento}
    lista_colaboradores.append(dicionario_colaborador.copy())
    print('*' * 64)
# ------Fim de cadastrar_colaborador(id)-----

# ------Inicio de consultar_colaborador()-----


def consultar_colaborador():
    print('*' * 64, '\n' +
          '-' * 18, 'MENU CADASTRAR COLABORADOR', '-' * 18)
    while True:
        opcao_consultar = input('\nEscolha a opção desejada:\n' +
                                '1 - Consultar TODOS os Colaboradores\n' +
                                '2 - Consultar Colaborador por ID\n' +
                                '3 - Consultar Colaborador(es) por setor\n' +
                                '4 - Retornar\n' +
                                '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção de consultar TODOS os colaboradores')
            for colaborador in lista_colaboradores:  # colaborador vai varrer toda a lista de colaboradores
                print('-' * 15)
                for key, value in colaborador.items():  # varrer todos os conjuntos de chave e valor do dicionario colaborador
                    print('{}: {}'.format(key, value))
                print('-' * 15)
        elif opcao_consultar == '2':
            print('Você escolheu a opção de consultar o colaborador por ID')
            valor_desejado = int(
                input('Digite o ID do colaborador desejado: '))
            for colaborador in lista_colaboradores:
                # o valor do campo ID desse dicionario é igual o id desejado?
                if colaborador['id'] == valor_desejado:
                    print('-' * 15)
                    for key, value in colaborador.items():  # varrer todos os conjuntos de chave e valor do dicionario colaborador
                        print('{}: {}'.format(key, value))
                    print('-' * 15)
        elif opcao_consultar == '3':
            print('Você escolheu a opção de consultar os colaborador(es) por setor')
            valor_desejado = input('Digite o setor do colaborador desejado: ')
            for colaborador in lista_colaboradores:
                # o valor do campo setor desse dicionario é igual o setor desejado?
                if colaborador['setor'] == valor_desejado:
                    print('-' * 15)
                    for key, value in colaborador.items():  # varrer todos os conjuntos de chave e valor do dicionario colaborador
                        print('{}: {}'.format(key, value))
                    print('-' * 15)
        elif opcao_consultar == '4':
            return  # sai da funcao consultar_colaborador() e volta para MAIN
        else:
            print('Opção Inválida. Tente novamente.')
            continue  # volta para o inicio do laço
# ------Fim de consultar_colaborador()-----

# ------Inicio de remover_colaborador()-----


def remover_colaborador():
    print('*' * 64, '\n' +
          '-' * 19, 'MENU REMOVER COLABORADOR', '-' * 19)
    valor_desejado = int(
        input('Digite o ID do colaborador que deseja remover: '))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == valor_desejado:
            lista_colaboradores.remove(colaborador)
            print('Colaborador Removido!')

# ------Fim de remover_colaborador()-----


# ------Inicio da MAIN -----
print('Bem-vindo ao Controle de Colaboradores de Felipe Beluci Tonelote\n' +
      '*' * 64)
while True:
    print('-' * 24, 'MENU PRINCIPAL', '-' * 24)
    opcao_principal = input('Escolha a opção desejada:\n' +
                            '1 - Cadastrar Colaborador\n' +
                            '2 - Consultar Colaborador\n' +
                            '3 - Remover Colaborador\n' +
                            '4 - Sair\n' +
                            '>>')
    if opcao_principal == '1':
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao_principal == '2':
        consultar_colaborador()
    elif opcao_principal == '3':
        remover_colaborador()
    elif opcao_principal == '4':
        break
    else:
        print('Opção Inválida. Tente novamente.')
        continue  # volta para o inicio do laço
# ------Fim da MAIN -----
