#Strings podem ser declaradas usando aspas simples ou duplas
string1 = 'String com aspas siples'
string2 = "String com aspas duplas"
print(string1)
print(string2)
print("\n")
#Strings de várias linhas podem ser declaradas com três aspas simples ou duplas
string1 = '''String com aspas simples
de várias linhas'''

string2 = """String com aspas duplas
de várias linhas"""
print(string1)
print(string2)

###############################################################################
#Fatiando Strings
string = "Para o Python, toda String é uma lista imutável"
#índices:  0, 1, 2, 3, 4, 5 em ordem normal 
#índices: -6,-5,-4,-3,-2,-1 em ordem inversa

#string[x:y:z], em que:
#x: start
#y: stop
#z: step
#Se não definirmos o start, ele é 0
#Se não definirmos o stop, ele é len(lista)
#Se não definirmos o step, ele é 1

print(string[:4])   #Para
print(string[4:])   #o Python, toda String é uma lista imutável
print(string[::5])  #PohtSgmsme
print(string[1::3]) #a Ph,o rg aiamál
print(string[::-1]) #levátumi atsil amu é gnirtS adot ,nohtyP o araP (inverte a string)

###############################################################################
#Caracteres na tabela ASCII
#Caractere para ascii
print(ord("A"))

#ASCII para caractere
print(chr(97)) 
print("\n")

###############################################################################
#Dividindo strings
string = "Lista de caracteres"
string = string.split(" ")
print(string)
print("\n")

#Substituindo strings
string = "Lista de caracteres"
print(string.replace("de", "com"))

###############################################################################
#Iterando Strings
string = "Lista de caracteres em Python"
for key, value in enumerate(string):
	print(key, value)