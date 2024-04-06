#Usando string multilinha
menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair

"""

#criando variaveis conforme pede o desafio de sistema bancario primeira versão 
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

#criando condições
while True:
    opcao = input (menu)


    if opcao == "d":
        valor = float(input("Qual o valor do depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" #interpolação de string

        else:
            print("Operação falhou! O valor informado é invalido")   

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. ")
            
        elif excedeu_limite:
            print("Operação falhou! Limite excedido. ")

        elif excedeu_saque:
            print("operação falhou! Numero de saques excedido. ")      

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é invalido. ")

    elif opcao == "e":
        print("\n=========================EXTRATO=========================")
        print("Não foram realizado movimentações. " if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("==================================================")                  

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a opção desejada. ")
        

                        