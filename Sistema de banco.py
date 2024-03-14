# v1.0 do Sistema Bancario

menu = """

[n] Novo Usuario
[c] Nova conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


def inicio():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    usuarioConta = dict()
    while (True):

        opcao = input(menu)
        if opcao == 'n':
            novoUser = novoUsuario()
            if novoUser in usuarios:
                print("CPF ja existe")
            else:
                usuarios.append(novoUser)
        elif opcao == 'c':
            print("QUANTIDADE", len(contas))
            conta = novaContaCorrente(len(contas))
            contas.append(conta[0])
            usuarioConta.update(conta = conta[1])
        elif opcao == 'd':
            depositar()
        elif opcao == 's':
            sacar()
        elif opcao == 'e':
            print(extrato)
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'q':
            print("--------- USUARIOS ---------")
            print(usuarios)
            print("------------------------------")

            print("--------- CONTAS ---------")
            print(contas)
            print("------------------------------")

            print("--------- usuarios CONTAS ---------")
            print(usuarioConta)
            print("------------------------------")
            break


def novoUsuario():

    pessoa = dict(nome="", nascimento="", cpf="", endereço="")
    pessoa["nome"] = input("nome:")
    pessoa["nascimento"] = input("nascimento:")
    pessoa["cpf"] = input("cpf:")
    pessoa["endereço"] = input("endereço:")

    print("--------- NOVO USUARIO ---------")
    print(pessoa)
    print("------------------------------")
    return pessoa["cpf"]

def novaContaCorrente(quant):
    conta = dict(agencia="0001", nmrConta=quant + 1, usuario="")
    conta['usuario'] = novoUsuario()
    print("--------- NOVA CONTA ---------")
    print(conta)
    print("------------------------------")
    return conta["usuario"], conta

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques,):
    # 3 saques diarios de 500 reais cada
    # verificar saldo
    print("SAQUE")
    if (saldo > 0):
        if (numero_saques < 3):
            valor = float(input("Digite o valor do saque: "))
            while valor > 500:
                print("Limite de 500 reais por saque! Tente novamente.")
                valor = float(input("Digite o valor do saque: "))
            if (valor < saldo):
                saldo -= valor
                extrato += f"R${valor:.2f} Saque\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente")
        else:
            print("Você atingiu o limite de saque diario")
    else:
        print("Nao tem saldo suficiente para saque")

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    # VALOR DEVE SER POSITIVO
    print("DEPOSITO")
    valor = float(input("Digite o valor de deposito: "))
    while valor <= 0:
        print("Valor deve ser positivo! Tente novamente.")
        valor = float(input("Digite o valor de deposito: "))
    saldo += valor
    extrato += f"R${valor:.2f} Deposito\n"

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("*******EXTRATO*******")
    if (extrato == ""):
        print("Não foram realizadas operações.")
    else:
        print(extrato + f"Saldo: R${saldo:.2f} reais")
    print("*********************")


inicio()
