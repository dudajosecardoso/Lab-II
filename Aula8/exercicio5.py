# Utilizando dicionários, crie um programa que simule um caixa eletrônico. O usuário poderá optar pelas seguintes funcionalidades:
import os
import time


def deposit(stock_bank, transactions):
    try:
        how_much = int(input("\033[32mQuanto deseja depositar:\033[0m"))
        if how_much > 0:
            new_transaction = {"Saldo": how_much}
            transactions.append(new_transaction)
            stock_bank["Saldo"] = stock_bank.get("Saldo", 0) + how_much
            print(f"\033[32mDepósito de R${how_much} realizado com sucesso\033[0m")
        else:
            print("\033[31mVocê não pode adicionar valores abaixo de 0\033[0m")
    except ValueError:
        print("Digite um valor correto")
    time.sleep(2)


def withdraw(stock_bank, transactions):
    try:
        how_much = int(input("\033[32mQuanto deseja sacar:\033[0m"))
        if how_much > 0 and how_much <= stock_bank.get("Saldo", 0) and how_much <= 1000:
            new_transaction = {"Saldo": -how_much}
            transactions.append(new_transaction)
            stock_bank["Saldo"] = stock_bank.get("Saldo", 0) - how_much
            print(f"\033[32mSaque de R${how_much} realizado com sucesso\033[0m")
        elif how_much <= 0:
            print("\033[31mVocê não pode sacar valores abaixo de 0\033[0m")
        elif how_much > 1000:
            print(
                "\033[31mO valor do saque excede o limite de transação de R$1000\033[0m"
            )
        else:
            print("\033[31mSaldo insuficiente para o saque\033[0m")
    except ValueError:
        print("Digite um valor correto")
    time.sleep(2)


def money_verify(stock_bank, transactions):
    saldo = stock_bank.get("Saldo", 0)
    print(f"\033[32mSaldo atual: R${saldo}\033[0m")
    time.sleep(2)


def historic_movimentation(transactions):
    print("\033[32mHistórico de movimentações:")
    for transaction in transactions:
        if transaction["Saldo"] > 0:
            print(f"Depósito de R${transaction['Saldo']}")
        else:
            print(f"\033[31mSaque de R${-transaction['Saldo']}\033[0m")
    time.sleep(2)


def menu():
    print("\033[34;1m-=-=-=-=-= BEM VINDO A LOJA VIRTUAL -=-=-=-=-=\033[0m")
    print("1) - Depositar dinheiro")
    print("2) - Sacar dinheiro")
    print("3) - Verificar saldo bancário")
    print("4) - Histórico de movimentações")
    print("10) - Sair")
    print(f"\033[34m{'-='*22}\033[0m")


def main():
    stock_bank = {}
    transactions = []
    while True:
        os.system("cls")
        menu()
        option = int(input("Digite sua opção:"))
        if option == 1:
            deposit(stock_bank, transactions)
        elif option == 2:
            withdraw(stock_bank, transactions)
        elif option == 3:
            money_verify(stock_bank, transactions)
        elif option == 4:
            historic_movimentation(transactions)
        elif option == 5:
            print("\033[31mSaindo do sistema. Obrigado!\033[0m")
            break
        else:
            print("\033[31mOpção inválida. Tente novamente.\033[0m")
        time.sleep(2)


main()
