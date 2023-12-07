def is_leap_year(year):
    if (year % 4 ==0 and not year % 100 == 0) or year % 400 == 0:
       return True
    else:
        return False
    
def main():
    try:
        year = int(input("Digite um ano:"))
        
        result = is_leap_year(year)
        
        print("é bissexto?",result)
    except ValueError:
        print('[Error] Valor digitado inválido')
        
    except BaseException as error:
        print('[Error] Aconteceu um erro', error)
    
    
main()
