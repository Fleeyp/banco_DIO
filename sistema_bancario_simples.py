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
            extrato += f"Depósito: R${valor_depositado:.2f}\n"
            print("Depósito realizado com sucesso!\nRetornando para o menu...")
        else:
            print("\nValor inválido, digite um valor positivo!\nRetornando para o menu...")
            break

    elif opcao == "2":
        print("Saque")

        valor_saque = float(input("Informe o valor do saque: "))

        saque_excedido = valor_saque > saldo
        limite_excedido = valor_saque > limite
        num_saques_excedido = num_saques > LIMITE_SAQUES

        if saque_excedido:
            print("Saldo insuficiente!")
        elif limite_excedido:
            print("Limite de saque excedido! Solicite um valor inferior ou igual a",limite,"!")
        elif num_saques_excedido:
            print("Limite de saques diário excedido!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:.2f}\n"
            num_saques += 1
            print("Saque realizado com sucesso!\nRetornando para o menu...")
        
        else:
            print("O valor informado é inválido")

    elif opcao == "3":
        print("Extrato")
        print("\n================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}\n")
        print("=========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")