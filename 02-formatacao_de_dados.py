# Não é necessário declarar o encoding no python3, as strings já são unicode

num_int = 5
num_float = 3.123456789
val_string = "olá"

# Printar o valor de uma variável int
print(num_int)

print("O valor do número int é:", num_int)
print("O valor do número int é: " + str(num_int))
print("O valor do número int é: %d" %num_int)
print("O valor do número int é: {}".format(num_int))
f'O valor do número int é: {num_int}' # f-strings

# Printar o valor de uma variável float
print("O valor do número float é:", num_float)
print("O valor do número float é: " + str(num_float))
print("O valor do número float é: %.3f" %num_float)
print("O valor do número float é: {0:.3f}".format(num_float))

# Printar o valor de uma variável string
print("A string é:", val_string)
print("A string é: " + val_string)
print("A string é: %s" %val_string)
print("A string é: {}".format(val_string))