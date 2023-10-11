def division(val1,val2):
    try:
        return val1/val2
    except ZeroDivisionError:
        print(f"[Erro] Você não pode dividir um número por zero!")
        raise
    except BaseExecpition as error:
        print(f"[Erro] ocorreu um erro: {error}")
        
def input_int(message, canBeZero = True):
    while True: 
        value= int(input(message))
        
        if not canBeZero and value == 0:
            raise ValueError()
        return value
    except ValueError:
        print("[Erro] número informado inválido!")
    except BaseExecpition as error:
        print(f"[Erro] ocorreu um erro: {error}")
    finally:
        print("[finally]")

def main():
    try:
        n1= input_int("Digite o primeiro valor")
        n2= input_int("Digite o segundo valor", canBeZero = False)
    
    result = division(n1,n2)
    
        print(f"resultado: {result}")
    except ValueError:
        print("[Erro] número informado inválido!")
    except BaseExecpition as error:
        print(f"[Erro] ocorreu um erro: {error}")
    else: 
        print(" obrigado ")
    
main()

#try and except usados para tratamento de erros (raise pra passar a excessão para adiante)

