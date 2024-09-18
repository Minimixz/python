class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.LIMITE_SAQUE = 500.0
        self.LIMITE_SAQUES_DIARIOS = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito deve ser positivo.')

    def sacar(self, valor):
        if self.saques_realizados >= self.LIMITE_SAQUES_DIARIOS:
            print('Limite de saques diários atingido.')
            return

        if valor > self.LIMITE_SAQUE:
            print(f'Valor máximo para saque é R$ {self.LIMITE_SAQUE:.2f}.')
            return

        if valor > self.saldo:
            print('Saldo insuficiente para realizar o saque.')
            return

        self.saldo -= valor
        self.extrato.append(f'Saque: R$ {valor:.2f}')
        self.saques_realizados += 1
        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')

    def visualizar_extrato(self):
        if not self.extrato:
            print('Não foram realizadas movimentações.')
            return

        print('Extrato:')
        for movimento in self.extrato:
            print(movimento)

        print(f'Saldo atual: R$ {self.saldo:.2f}')

# Exemplo de uso
def main():
    conta = ContaBancaria()

    while True:
        print("\nSelecione a operação:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Visualizar Extrato")
        print("0 - Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.visualizar_extrato()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
