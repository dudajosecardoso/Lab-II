from menu import show_menu

def main():
    opc = 0 
    while opc != 3:
        show_menu()

        try:
            opc = int(input("Digite a opção desejada: "))

            if opc == 1:
                print("a")
            elif opc == 2:
                print("b")
            elif opc == 3:
                print("Você saiu!")
            else:
                print("Opção inválida. Digite um número de 1 a 3.")

        except ValueError:
            print("Você deve digitar um número.")

main()
