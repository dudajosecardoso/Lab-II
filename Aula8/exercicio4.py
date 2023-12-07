import math

def combinations(n, m):
    if n < m or n < 0 or m < 0:
        return 0
    else:
        return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))

def main():
    while True:
        try:
            n = int(input("Digite o número total de alunos (N): "))
            m = int(input("Digite o número de alunos em um dos grupos (M): "))
    
            result = combinations(n, m)
    
        except ValueError:
            print("Por favor, digite números inteiros.")
            continue
        else:
           print(f"O número de combinações possíveis é: {result}")
        break

main()
