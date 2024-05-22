import arquivos, os

arquivo = arquivos
sair = False

while sair == False:
    opcao = input("Escolha uma Opção:\n"
                  "1: Cadastrar item\n"
                  "2: Listar itens\n"
                  "3: Sair\n")
    
    match opcao:
        case "1":
            item = input("Digite o item a ser adicionado: ")
            arquivo.criaArquivo(item)
            os.system('clear')
        case "2":
            os.system('clear')
            arquivo.lerArquivo()
        case "3":
            sair = True
        case _:
            print("Opção inválida")
    # if opcao == "1":
    #     item = input("Digite o item a ser adicionado: ")
    #     arquivo.criaArquivo(item)
    #     os.system('clear')
    # elif opcao == "2":
    #     os.system('clear')
    #     arquivo.lerArquivo()
    # elif opcao == "3":
    #     sair = True
    # else:
    #     print("Opção inválida")


