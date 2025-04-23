menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3


def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:  R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else: 
        print("Por favor, insira uma quantia válida para depositos!")
    return saldo, extrato

def saque(valor, numero_de_saques, saldo, extrato):
    if numero_de_saques > LIMITE_SAQUES:
        print("Você ultrapassou o nossos limites de saques! Por favor, tente novamente amanhã.")
    
    elif valor > limite:
        print(f"O valor do saque ultrapassa nosso limite de: R$ {limite:.2f}")
    
    elif valor > saldo:
        print("Saldo insulficiente!")

    elif valor <= 0:
        print("Valor inválido para saque.")
    
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_de_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_de_saques

def extrato_resumo(extrato, saldo):
    print("\n============== EXTRATO ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ { saldo:.2f}")

while True:

    option = input(menu)

    if option == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)
      

    elif option == "s":
            valor = float(input("Informe o valor desejado para saque: "))
            saldo, extrato, numero_de_saques = saque(valor, numero_de_saques, saldo, extrato)

    elif option == "e":
        extrato_resumo(extrato, saldo)
    
    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
