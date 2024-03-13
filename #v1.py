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
        extrato += f"R${valor:.2f} Deposito\n"

    elif opcao == "s":
        #3 saques diarios de 500 reais cada
        #verificar saldo
        print("SAQUE")
        if(saldo>0):
            if(numero_saques < 3):
                valor = float(input("Digite o valor do saque: "))
                while valor > 500:
                    print("Limite de 500 reais por saque! Tente novamente.")
                    valor = float(input("Digite o valor do saque: "))
                if(valor<saldo):
                    saldo -= valor
                    extrato += f"R${valor:.2f} Saque\n"
                    numero_saques +=1
                else:
                    print("Saldo insuficiente")
            else:
                print("Você atingiu o limite de saque diario")
        else:
            print("Nao tem saldo suficiente para saque")

    elif opcao == "e":
        print("*******EXTRATO*******")
        if(extrato == ""):
            print("Não foram realizadas operações.")
        else:
            print(extrato + f"Saldo: R${saldo:.2f} reais")
        print("*********************")
    
    elif opcao == "q":
        break

    else:
        print("Tente novamente")
