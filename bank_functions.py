import textwrap


def menu():
    menu = """
    ================= MENU =====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova contas
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

    
def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:  R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else: 
        print("Por favor, insira uma quantia válida para depositos!")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= limite_saques


    if excedeu_saldo:
        print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
    
    elif excedeu_limite:
        print(f"O valor do saque ultrapassa nosso limite de: R$ {limite:.2f}")
    
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_de_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
          print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuário, com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo")
    data_nacimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço:")

    usuarios.append({"nome": nome, "data_nascimento": data_nacimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def extrato_resumo(saldo, /, *, extrato):
    print("\n============== EXTRATO ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ { saldo:.2f}")
    print("=================================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        option = menu()

        if option == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(valor, saldo, extrato)
        
        elif option == "s":
                valor = float(input("Informe o valor desejado para saque: "))

                saldo, extrato = saque(
                    saldo=saldo, 
                    valor=valor, 
                    extrato=extrato, 
                    limite=limite, 
                    numero_de_saques=numero_de_saques,
                    limite_saques=LIMITE_SAQUES
                    )

        elif option == "e":
            extrato_resumo(saldo, extrato=extrato)

        elif option == "nu":
            criar_usuario(usuarios)

        elif open == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif option == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


