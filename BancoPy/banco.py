from typing import List
from time import  sleep

from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print("=================================")
    print("===========PYTHON BANK===========")
    print("=================================")

    print("Selecione um opção no menu:")
    print("1 - Criar conta")
    print("2 - Efetuar Saque")
    print("3 - Efetuar Depósito")
    print("4 - Efetuar Transferência")
    print("5 - Listar contas ")
    print("6 - Sair do sistema")

    opcao: int =  int(input())

    if opcao == 1:
        criar_conta()
    elif opcao ==2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Volte Sempre')
        sleep(2)
        exit(0)
    else:
        print("Opção inválida")
        sleep(2)
        menu()

def criar_conta() -> None:
    print("Informe os dados do cliente: ")
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de Nascimento: ')

    cliente: Cliente = Cliente(nome,email,cpf,data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta Criada com sucesso!')
    print('Dados da Conta:')
    print(conta)
    sleep(2)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o Número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o Valor do Saque: "))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
    else:
        print('Ainda não há contas cadastradas!')
    sleep(2)
    menu()

def efetuar_deposito() -> None:
    if len(contas):
        numero: int = int(input("Informe o número da sua Conta: "))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
    else:
        print('Ainda não há contas cadastradas!')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da conta sua conta'))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input('Informe o número da conta de destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input("Informe o valor da transferência: "))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'Conta destino com número {numero_d} não encontrada!')
        else:
            print(f'Conta com número {numero_o} não encontrada!')


    else:
        print("Ainda não existem contas cadastradas!")
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas:')
        for conta in contas:
            print(conta)
            print('-------------------------')
            sleep(1)

        print(f'Total de contas: {len(contas)}')

    else:
        print('Não existem contas cadastradas!')
    sleep(2)
    menu()

def buscar_conta_por_numero(numero: int) -> None:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

if __name__ == '__main__':
    main()

