manifestacaoList = []

while True:
    print("\nMenu: \n 1) - Listar das Manifestações \n 2) - Criar uma nova Manifestação \n 3) - Exibir quantidade de manifestações \n 4) - Pesquisar uma manifestação por código \n 5) - Excluir uma Manifestação pelo Código \n 6) - Sair do Sistema")
    escolha = int(input("\n Digite sua escolha: "))

    if escolha == 1:
        cont = 0  # Contador para exibir lista em ordem númerica
        if len(manifestacaoList) != 0:
            print("\nLista de manifestações: \n")
            for manifestacao in manifestacaoList:
                cont = cont + 1
                print(cont.__str__() + ") - " + manifestacao)
        else:
            print("\nNão existe nenhuma manifestação!")

    elif escolha == 2:
        manifestacao = str(input("\nDigite sua manisfetação: "))
        manifestacaoList.append(manifestacao)

        print("\nNova manifestação criada com sucesso!")

    elif escolha == 3:
        print("\nA quantidade de manifestações é " + len(manifestacaoList).__str__())

    elif escolha == 4:
        codigo = int(input("\nDigite o código da manisfestação: "))

        if codigo <= len(manifestacaoList):
            print('''\nA manifestação pesquisada foi "''' + manifestacaoList[codigo - 1] + '''"''')

        else:
            print("\nCódigo inválido!")

    elif escolha == 5:
        cont = 0  # Contador para exibir lista em ordem númerica
        if len(manifestacaoList) != 0:
            print("\nLista de manifestações: \n")
            for manifestacao in manifestacaoList:
                cont = cont + 1
                print(cont.__str__() + ") - " + manifestacao)

            excluir = int(input("\nDigite o número da manisfestação que deseja excluir: "))
            del(manifestacaoList[excluir - 1])

        else:
            print("\nNão existe nenhuma manifestação!")

    elif escolha == 6:
        break

    else:
        print("\nOpção inválida, tente novamente!")
