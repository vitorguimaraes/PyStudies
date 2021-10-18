# Listas são estruturas mutáveis
# Listas geralmente são estruturas homogêneas, contendo elementos do mesmo tipo
lista = [1, 2, 3, 4, 5]

# Criar uma cópia de uma lista
copy = lista.copy() # Ou copy = lista[:]

# Extender conteúdo de uma lista
t = [6, 7, 8, 9]
lista.extend(t) # ou lista += t
# agora a lista é [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Acessando índices da lista:
print(lista[0])
print(lista[1])
print(lista[2])
print("\n")
print(lista[-1]) # Último elemento da lista
print(lista[-2]) # Penúltimo elemento da lista
print(lista[-3]) # Antipenúltimo elemento da lista

print("\n")

# Lista de listas
lista = [["a", "b", "c"], [1, 2, 3], ["uva", "maçã", "banana"]]
print(lista[0][2]) # Acessando o terceiro elemento da primeira lista

# Comprimento da lista
print(len(lista))

#####################################################################
lista = ["a", "b", "c", "d", "e"]

# Adicionando itens no final da lista:
lista.append("z")#sintaxe: (element)
print(lista)

# Adicionando itens em qualquer índice da lista:
lista.insert(3, "ola") #sintaxe: (index, element)

# Alterando elementos da lista:
lista[2] = "x" #sintaxe: list[index] = element

# Removendo itens da lista:
del(lista[-1]) # sintaxe: del(list[index]) - nesse caso remove o último elemento da lista
print(lista)
del(lista[1:3]) # deleta do índice 1 ao índice 3

lista.remove(x) # Remove um elemento específico, onde x é o elemento

# Removendo todos os itens da lista
lista.clear()

# Remover e retornar item deletado:
lista.pop(0) # sintaxe: list.pop(index) - Se não informar o indice o padrão é o ultimo elemento

# Iterando listas:
lista = list(range(10))
for item in lista:
	print(item)
print("\n")

# Alterando objetos da lista
# Se você não precisa do índice:
for item in lista:
	lista[item] += 5
print(lista)

# Se você precisa do índice:
for index, item in enumerate(lista): #enumerate() enumera os objetos da lista
	lista[index] += 5
print(lista)

######################################################################
# Fatiando listas

# índices:  0, 1, 2, 3, 4, 5 em ordem normal 
# índices: -6,-5,-4,-3,-2,-1 em ordem inversa
lista = ["PYTHON"]

# lista[x:y:z], em que:
# x: start
# y: stop
# z: step
# Se não definirmos o start, ele é 0
# Se não definirmos o stop, ele é len(lista)
# Se não definirmos o step, ele é 1

print(lista[:2])   #PYT
print(lista[2:])   #THON
print(lista[::2])  #PTO
print(lista[2::2]) #TO
print(lista[::-1]) #NOHTYP (inverte a lista)

######################################################################
# Ordenamento de listas
lista = ["uva", "maçã", "banana", "laranja", "mamão"]

# Inverter lista
lista.reverse()
print(lista)

# Ordenar de forma ascendente:
lista.sort()
print(lista)

# Ordenar de forma descendente:
lista.sort(reverse = True)
print(lista)

######################################################################
# Quantidade de ocorrências de um elemento em uma lista
print(lista.count("banana"))

# Retornar o índice de um item da lista
print(lista.index("maçã"))

# Função zip
# [ 1, 2, 3 ]
# -zip=====> [(1, 4), (2, 5), (3, 6)]
# [ 4, 5, 6 ]

x = [1, 2, 3] # lista ou tupla
y = [4, 5, 6] # lista ou tupla
a = tuple(zip(x, y))