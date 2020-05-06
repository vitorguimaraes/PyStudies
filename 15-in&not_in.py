# Estes operadores verificam se o valor de um objeto está contido ou não em 
# uma lista, tupla ou dicionário
conjunto = [1, 2, 3, 4, 5]
x = 4
y = 0

result = "True" if x in conjunto else "False"
print(result)

result = "True" if y not in conjunto else "False"
print(result)

x = 1
y = 2
result = "True" if x and y in conjunto else "False"
print(result)