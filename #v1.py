# v1.0 do Sistema Bancario

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        # VALOR DEVE SER POSITIVO
        print("DEPOSITO")
        valor = float(input("Digite o valor de deposito: "))
        while valor <= 0:
            print("Valor deve ser positivo! Tente novamente.")
            valor = float(input("Digite o valor de deposito: "))
        saldo += valor
        extrato = f"{valor} Deposito\n" + extrato

    elif opcao == "s":
        print("SAQUE")

    elif opcao == "e":
        print("EXTRATO")
        print(extrato + f"Saldo: {saldo} reais")

    elif opcao == "q":
        break

    else:
        print("Tente novamente")
