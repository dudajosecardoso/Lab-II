class NegativeNumberError(Exception):
    pass

def calculate_square_root():
    number = int(input("Insira um número: "))
    
    if number < 0:
        raise NegativeNumberError("Erro! A raiz quadrada de números negativos é inválida.")
    else:
        square_root = number ** 0.5
        print(f"A raiz quadrada de {number} é {square_root:.2f}")

def main():
    try:
        calculate_square_root()
    except NegativeNumberError as error:
        print(error)
    except Exception as error:
        print(f"Ocorreu um erro: {error}")


main()
