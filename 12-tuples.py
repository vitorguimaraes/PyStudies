# Tuplas são estruturas imutáveis, portanto não é possível 
#remover, adicionar ou alterar a tupla de maneira alguma
# Tuplas geralmente são estruturas heterogêneas, contendo elementos de tipos distintos
tupla = ("amora", 28, True)

# Acessando índices da tupla:
print(tupla[0])
print(tupla[1])
print(tupla[2])
print("\n")
print(tupla[-1]) # Último elemento da tupla
print(tupla[-2]) # Penúltimo elemento da tupla
print(tupla[-3]) # Antipenúltimo elemento da tupla
print("\n")

# Tupla de tuplas
tupla = ((1, "frutas", False), (True, 2, "casas"), ("python", 7, None))
print(tupla[0][2]) #Acessando o terceiro elemento da primeira tupla

# Comprimento da tupla
print(len(tupla))
print("\n")
######################################################################

# Iterando tuplas:
tupla = ("macaco", 1, True, 26, None)
for item in tupla:
	print(item)
print("\n")
######################################################################

# Fatiando tuplas
# índices:  0, 1, 2, 3, 4, 5 em ordem normal 
# índices: -6,-5,-4,-3,-2,-1 em ordem inversa
tupla = ("macaco", 1, True, 26, None)

# tupla[x:y:z], em que:
# x: start
# y: stop
# z: step
# Se não definirmos o start, ele é 0
# Se não definirmos o stop, ele é len(tupla)
# Se não definirmos o step, ele é 1

print(tupla[:2])   # ('macaco', 1)
print(tupla[2:])   # (True, 26, None)
print(tupla[::2])  # ('macaco', True, None)
print(tupla[2::2]) # (True, None)
print(tupla[::-1]) # (None, 26, True, 1, 'macaco')s (inverte a tupla)
######################################################################

# Quantidade de ocorrências de um elemento em uma tupla
print(tupla.count("macaco"))

# Retornar o índice de um item da tupla
print(tupla.index(True))

# Função zip
# [ 1, 2, 3 ]
# -zip--------------- ====> [(1, 4), (2, 5), (3, 6)]
# [ 4, 5, 6 ]

x = [1, 2, 3] # lista ou tupla
y = [4, 5, 6] # lista ou tupla
a = tuple(zip(x, y))