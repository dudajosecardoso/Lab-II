def classify_triangle(triangle_side_1, triangle_side_2, triangle_side_3):
    if triangle_side_1 <= 0 or triangle_side_2 <= 0 or triangle_side_3 <= 0:
        raise ValueError("Os lados do triângulo devem ter valores positivos.")

    sides = [triangle_side_1, triangle_side_2, triangle_side_3]
    sides.sort()

    if sides[0] + sides[1] <= sides[2]:
        raise ValueError("Os lados informados não formam um triângulo válido.")

    if triangle_side_1 == triangle_side_2 == triangle_side_3:
        print("É um triângulo equilátero.")
    elif triangle_side_1 == triangle_side_2 or triangle_side_1 == triangle_side_3 or triangle_side_2 == triangle_side_3:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")

def main():
    try:
        triangle_side_1 = float(input("Insira o tamanho do primeiro lado do triângulo: "))
        triangle_side_2 = float(input("Insira o tamanho do segundo lado do triângulo: "))
        triangle_side_3 = float(input("Insira o tamanho do terceiro lado do triângulo: "))
        
        classify_triangle(triangle_side_1, triangle_side_2, triangle_side_3)

    except ValueError as error:
        print(f"O triângulo informado é inválido: {error}")

    except Exception as error:
        print(f"Ocorreu um erro: {error}")


main()
