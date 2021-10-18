x = 10
string = "sim" if x == 10 else "não"

number = int(input("Insira um número: "))

result = "Par" if number % 2 == 0 else "Ímpar"
print(result)

def par_impar(number):
    return "par" if number % 2 == 0 else "Ímpar"