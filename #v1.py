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
        print("DEPOSITO")


    elif opcao == "s":
        print("SAQUE")


    elif opcao == "e":
        print("EXTRATO")


    elif opcao == "q":
        break

    
    else:
        print("Tente novamente")
