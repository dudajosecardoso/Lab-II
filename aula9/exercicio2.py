def give_note():
    try:
        note = int(input("Dê sua nota de 0 a 10 para nosso produto: "))

        if note < 0:
            raise ValueError("Erro! Não é permitido inserir números negativos.")
        
        assert 0 <= note <= 10
        print("Obrigada pela avaliação!")

    except ValueError:
        print("Por favor utilize apenas números positivos.")
    except AssertionError:
        print("O número está acima do permitido!")

def main():
    give_note()
main()
