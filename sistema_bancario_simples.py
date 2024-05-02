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
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += "Depósito: R${valor_depositado:.2f}\n"
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