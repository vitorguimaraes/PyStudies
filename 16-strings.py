# Strings podem ser declaradas usando aspas simples ou duplas
string1 = 'String com aspas simples'
string2 = "String com aspas duplas"

# Usa-se aspas simples para: 
# identificadores, expressões regulares ou SQL 

# Usa-se aspas duplas para: 
# Textos 

# Strings de várias linhas podem ser declaradas com três aspas
string = '''String com 
			aspas simples
			de várias linhas'''


###############################################################################
# Fatiando Strings
string = "Para o Python, toda String é uma lista imutável"
# índices:  0, 1, 2, 3, 4, 5 em ordem normal 
# índices: -6,-5,-4,-3,-2,-1 em ordem inversa

# string[x:y:z], em que:
# x: start
# y: stop
# z: step
# Se não definirmos o start, ele é 0
# Se não definirmos o stop, ele é len(lista)
# Se não definirmos o step, ele é 1

string[:4]   # Para
string[4:]   # No Python toda String é uma lista imutável
string[::5]  # PohtSgmsme
string[1::3] # a Ph,o rg aiamál
string[::-1] # levátumi atsil amu é gnirtS adot ,nohtyP o araP (inverte a string)

###############################################################################
# Converter caractere para ascii
ord("A")

# Converter ASCII para caractere
chr(97)

###############################################################################
# Dividindo strings
string = "Lista de caracteres"
string = string.split(" ")

# Substituindo strings
string = "Lista de caracteres"
string.replace("de", "com")

###############################################################################
# Iterando Strings
string = "Lista de caracteres em Python"
for key, value in enumerate(string):
	print(key, value)