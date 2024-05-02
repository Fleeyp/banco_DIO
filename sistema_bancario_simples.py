menu = """

[1] depositar
[2] sacar
[3] extrato
[0] sair

=> """

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\nDepósito\n")
        valor_depositado = float(input("Digite o valor que deseja depositar: "))
        while valor_depositado:
            if valor_depositado > 0:
                saldo += valor_depositado
                print("Deseja realizar outro depósito? y/n")
                if input() == "n":
                    break
                elif input() == "y":
                    print("Digite o valor que deseja depositar")
                else:
                    print("\nOpção inválida!\nRetornando para o menu...")
                    break
            else:
                print("\nValor inválido, digite um valor positivo\nRetornando para o menu...")
                break

    elif opcao == "2":
        print("Saque")

    elif opcao == "3":
        print("Extrato")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")