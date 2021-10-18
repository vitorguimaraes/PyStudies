# Funções podem ser invocadas de qualquer parte do código
# Pode retornar um valor, por isso raramente devemos usar variáveis globais
# Funções geralmente retornam valores, enquanto métodos não retornam valores

# Quando definimos uma função, definimos parâmetros que são passados
# Quando invocamos a função definimos os argumentos passados pra função

def soma(x, y): # Aqui definimos os parâmetros
	return x+y

soma(2, 4) # Aqui passamos argumentos para a função


# Type hinting
def soma(x: int, y: int) -> int:
	return x + y

###############################################################################
# Parâmetros Default
# Deve-se passar primeiro os parâmetros que não são inicializados
def login(system, user = 'admin', password = '123'):
	f'User: {user}'
	f'Password: {password}'

###############################################################################
# Argumentos posicionais e nomeados
# Argumentos posicionais: cada valor deve ser passado na ordem da implementação da função 
# Argumentos nomeados: associação com o nome do parâmetro e o valor que é enviado

def personal_data(name, age, sex):
	print('Nome: {}\nIdade: {}\nSexo: {}'.format(name, age, sex))

personal_data('Vitor', 23, 'M')			            # Argumentos posicionais
personal_data(sex = 'M', name = 'Vitor', age = 23)  # Argumentos nomeados
# Argumentos posicionais são passados como uma tupla
# Argumentos nomeados são passados como um dicionário

###############################################################################
# Retorno de valores múltiplos
def potencia(x):
	quadrado = x**2
	cubo 	 = x**3 
	return quadrado, cubo

x, y = potencia(3)

###############################################################################
# Função Variádica
# São funções que podem receber quantidades arbitrárias de parâmetros
# *args: Lista de argumentos posicionais    (arguments)
# **kwargs: Conjunto de argumentos nomeados (keyword arguments)
def func(*args, **kwargs):
	print(args)
	print(kwargs)

# Ex:
def lista_de_argumentos(*args):
	print(args)

def lista_de_argumentos_nomeados(**kwargs):
	print(kwargs)

lista_de_argumentos('a', 1, True, 19.6, (1, 3, 'a'))

lista_de_argumentos_nomeados(Marcelo = 97864537, 
							 Daniel  = 99673450, 
							 Andre   = 88432865, 
							 Lais    = 99432764,
							 Marcia  = 88653421,
							 Kelly   = 99563856,
							 Ana     = 97824423)

func('a', 1, True, 19.6, (1, 3, 'a'), Marcelo = 97864537, 
									  Daniel  = 99673450, 
									  André   = 88432865, 
									  Laís    = 99432764,
									  Marcia  = 88653421,
									  Kelly   = 99563856,
									  Ana     = 97824423)


###############################################################################
# Desempacotamento de listas, tuplas e dicionários
# É possível passar listas, tuplas e dicionários
# desempacotados como argumentos de uma função
def func(a, b, c):
	print(a)
	print(b)
	print(c)

lista = [10, 20, 30]
func(*lista) # É enviado 10, 20, 30 para a função, e não a lista contendo os valores
# Exemplo de desempacotamento
x, y, z = lista  # x = 10, y = 20, z = 30

# Exemplo prático:
def pessoa(nome, sobrenome, idade):
	print(nome)
	print(sobrenome)
	print(idade)

lista = ['Vitor', 'Guimarães', 25]
tupla = 'João', 'Silva', 35
dicionario = {'nome': 'Vitor', 'sobrenome': 'Guimarães', 'idade': 25}

pessoa(*lista)
pessoa(*tupla)
pessoa(**dicionario)

# Função zip (retorna uma lista de tuplas)
# [ 1, 2, 3 ]
# zip ======> [(1, 4), (2, 5), (3, 6)]
# [ 4, 5, 6 ]

x = [1, 2, 3] # lista ou tupla
y = [4, 5, 6] # lista ou tupla
a = tuple(zip(x, y))

# Usando zip para passar argumentos para função
def foo(login, password, system):
	print(login)
	print(password)
	print(system)

keys   = 'login', 'password', 'system'
values = 'admin', 123, 'MainSystem' 

zipped = zip(keys, values) # [('login', 'admin'), ('password', 123), ('system', 'MainSystem')]
named_args = dict(zipped)  # {'login': 'admin', 'password': 123, 'system': 'MainSystem'}
foo(**named_args)		   # Desempacota o dicionário 

###############################################################################
# Instrução Nonlocal
# Permite acessar variáveis que não são globais nem locais
def my_func():
	var_local = 10

	def func_interna():
		nonlocal var_local
		var_local += 10
		print(var_local)
	func_interna()
my_func()

# Escopo global
# Para o python escopo global é o escopo do módulo. Tudo que estiver declarado no
# escopo global pode ser acessado de outros módulos e por qualquer código 
# implementado dentro desse módulo

variavel_global = 'global' # Essa variável pode ser acessada de qualquer parte do módulo

# A função globals() retorna as variáveis globais do módulo
# A função locals() retorna as variáveis locais do escopo

# Variáveis globais
# De dentro das funções nós conseguimos acessar e ler o valor das variáveis
# globais, mas não conseguimos alterar seus valores

# Ex:
global1 = 'global_variable' # variável global (escopo do módulo)
def goo():
	global num  #variável, função, classe...
	num = 'access global_variable from local scope' # A variável global 'num' será alterada
	print(num)
	global num2
	num2 = 'global_variable declared from local scope'
goo()
print(num2)
# A instrução global serve para acessar uma variável global de dentro de um escopo
# local ou para declarar uma variável global de dentro de um escopo local

# NUNCA coloque no escopo global o que pode ser enviado por parâmetro