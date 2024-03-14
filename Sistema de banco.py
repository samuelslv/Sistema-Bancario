# v1.0 do Sistema Bancario
import textwrap


def menu():
    menu = """
[n] Novo Usuario
[c] Nova conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Contas
[q] Sair
=> Digite a opção: """
    return input(menu)


def inicio():
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while (True):
        opcao = menu()

        if opcao == 'n':
            novoUsuario(usuarios)
        elif opcao == 'c':
            quantoContas = len(contas) + 1
            conta = novaContaCorrente(quantoContas, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'd':
            valor = float(input("Digite o valor de deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                   limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'l':
            listarContas(contas)
        elif opcao == 'listar':
            print(contas)
            print("------------------------------")
            print(usuarios)
        elif opcao == 'q':
            print("--------- USUARIOS ---------")
            print(usuarios)
            print("------------------------------")

            print("--------- CONTAS ---------")
            print(contas)
            print("------------------------------")

            break


def validarCPF(cpf, usuarios):
    usuariosFiltrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuariosFiltrados[0] if usuariosFiltrados else None


def novoUsuario(usuarios):
    pessoa = dict(nome="", nascimento="", cpf="", endereço="")
    cpf = input("cpf:")

    usuario = validarCPF(cpf, usuarios)

    if usuario:
        print("CPF ja esta cadastrado")
        return

    pessoa["nome"] = input("nome:")
    pessoa["nascimento"] = input("nascimento:")
    pessoa["cpf"] = cpf
    pessoa["endereço"] = input("endereço:")

    usuarios.append(pessoa)
    print("***** USUARIO CADASTRADO COM SUCESSO *****")


def novaContaCorrente(quant, usuarios):
    conta = dict(agencia="0001", nmrConta=quant, usuario="")
    cpf = input("cpf:")
    usuario = validarCPF(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso")
        conta["usuario"] = usuario
        print(conta)
        return conta
    print("Usuario nao encontrado")


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # 3 saques diarios de 500 reais cada
    # verificar saldo
    print("SAQUE")

    saldoInsuficiente = valor > saldo
    passouLimiteDiario = numero_saques >= limite_saques
    passouLimiteSaque = valor > limite

    if (saldoInsuficiente):
        print("Saldo insuficiente")
    elif (passouLimiteDiario):
        print("Você atingiu o limite de saque diario")
    elif (passouLimiteSaque):
        print("Valor de saque maior que o limite")
    elif (valor < 0):
        print("Valor negativo não permitido.")
    else:
        saldo -= valor
        extrato += f"R${valor:.2f} Saque\n"
        numero_saques += 1

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    # VALOR DEVE SER POSITIVO
    print("DEPOSITO")
    while valor <= 0:
        print("Valor deve ser positivo! Tente novamente.")
        valor = float(input("Digite o valor de deposito: "))
    saldo += valor
    extrato += f"R${valor:.2f} Deposito\n"
    print("Deposito realizado com sucesso")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("*******EXTRATO*******")
    if (extrato == ""):
        print("Não foram realizadas operações.")
    else:
        print(extrato + f"Saldo: R${saldo:.2f}")
    print("*********************")


def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['nmrConta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))


inicio()
