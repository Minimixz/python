# Sistema Bancário Simples

# Inicializando o saldo e o extrato
saldo = 0
extrato = []

def depositar(saldo, valor):
    """Função para depositar um valor."""
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print("Valor de depósito deve ser positivo.")
    return saldo

def sacar(saldo, valor):
    """Função para sacar um valor."""
    if 0 < valor <= saldo:
        saldo -= valor
        extrato.append(f'Saque: R$ {valor:.2f}')
        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    elif valor > saldo:
        print("Saldo insuficiente para saque.")
    else:
        print("Valor de saque deve ser positivo.")
    return saldo

def exibir_extrato():
    """Função para exibir o extrato."""
    print("\n--- Extrato Bancário ---")
    for registro in extrato:
        print(registro)
    print(f'Saldo atual: R$ {saldo:.2f}')
    print("------------------------\n")

# Loop principal do sistema bancário
def main():
    global saldo  # Usar a variável global saldo

    while True:
        print("Selecione uma opção:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo = depositar(saldo, valor)
        elif opcao == '2':
            valor = float(input("Informe o valor do saque: R$ "))
            saldo = sacar(saldo, valor)
        elif opcao == '3':
            exibir_extrato()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o sistema
if __name__ == "__main__":
    main()
