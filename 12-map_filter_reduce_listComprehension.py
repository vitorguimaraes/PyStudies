# List Comprehension: resolve tudo que o map e filter resolvem :D :D :D
# map(): aplica uma função em cada um dos elementos de uma lista
# filter(): filtra elementos de uma lista com uma função
# reduce(): aplica uma função nos elementos da lista, reduzindo a um só elemento 


# *************************************************** #
# *********************** MAP *********************** #
# *************************************************** #

# Problema: Obter o quadrado dos números de uma lista 

# Solução comum
items = [1, 2, 3, 4, 5]
squared = []
for value in items:
    squared.append(value**2)

# Solução com map()
items = [1, 2, 3, 4, 5]
squared = list(map(lambda value: value**2, items))
# Pode-se ler "lambda value:" como "for value in items"

# Solução com List Comprehension
items = [1, 2, 3, 4, 5]
squared = [value**2 for value in items]

# Multiple if statement 
# Sintaxe: new_list = [expression (if else conditional) for member in iterable]
values = [1, -9, 10, 3, -5] 
new_values = list(map(lambda value: value if value > 0 else 0 if value%2==0 else 'x', values))


# *************************************************** #
# ********************* FILTER ********************** #
# *************************************************** #

# Problema: Gerar uma nova lista apenas com os números pares:
# Solução comum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
for num in numbers:
	if num%2 == 0:
		even_numbers.append(num)

# Solução com Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda value: value%2 == 0, numbers))

# Solução com List Comprehension
# Sintaxe: new_list = [expression for member in iterable (if(s) conditional)]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [num for num in numbers if num%2 == 0]

# ex: Número maiores que zero
values = [1, -9, 10, 3, -5] 
new_values = [value for value in values if value > 0]


# *************************************************** #
# ********************* REDUCE ********************** #
# *************************************************** #

# Problema: O produto dos valores de uma lista

# Solução comum
numbers = [1, 2, 3, 4]
product = 1
for value in numbers:
	product = product * value

# Solução com Reduce
from functools import reduce 
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Solução com List Comprehension
# Não é possível