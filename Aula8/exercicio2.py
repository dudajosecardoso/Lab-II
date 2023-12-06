class InvalidMonthException(BaseException):
    pass

def get_month_name(month):
    try: 
        months = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
        
        return months[month - 1]
    except IndexError:
        print("O mês não existe")
    except BaseException as error:
        print("ocorreu um erro")
        
def main():
    while True:
        try: 
            month = int(input("Digite o mês: "))
            
            if month > 12 or month < 1:
                raise InvalidMonthException()
            
            month_name = get_month_name(month)
            
        except ValueError:
            print("Você deve digitar somente números inteiros. Tente novamente! ")
            print()
            continue
        except BaseException as error: 
            print("Ocorreu um erro, Tente Novamente! ", error)
            print()
            continue
        else:
            print(f"nome do mês: {month_name}")
        break
        
main()
