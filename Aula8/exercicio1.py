## Crie um programa que receba através de input dois números e retorne sua divisão

def division():
    while True:
        try:
            n1 = int(input("Digite o numerador: "))
            n2 = int(input("Digite o denominador: "))
            result = n1 / n2
        except (ValueError, TypeError):
            print("Tivemos um problema com os tipos de dados que você digitou, tente novamente!")
            print()
            continue
        except ZeroDivisionError:
            print("Não é possível dividir um número por zero! tente novamente!")
            print()
            continue
        except KeyboardInterrupt:
            print("O usuário preferiu não informar os dados!")
        else:
            print(f"o resultado é {result}")
        break
        
def main():
    division()
main()
