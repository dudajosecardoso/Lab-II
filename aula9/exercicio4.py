def find_element(my_list, number):
    try:
        result = my_list[number]
        print(result)
    except IndexError:
        print("Erro! O índice informado não existe na lista.")

def main():
    try:
        my_list = ["batata", "cebola", "tomate", "alface", "cenoura"]
        number = int(input("Insira o índice desejado: "))
        find_element(my_list, number)
    except ValueError:
        print("Erro! Por favor, insira um número inteiro como índice.")

main()
