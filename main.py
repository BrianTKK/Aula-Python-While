opcao = -1



while opcao != 0:
    opcao = int(input("Informe a opcao: "))
    match opcao:
        case 1:
            print("opcao 1")
        case 2:
            print("opcao 2")
        case _:
            if opcao != 0:
                print("opcao invalida")