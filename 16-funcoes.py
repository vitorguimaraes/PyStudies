#Funções podem ser invocadas de qualquer parte do código
#Pode retornar um valor, por isso raramente devemos usar variáveis globais
#Funções geralmente retornam valores, enquanto métodos não retornam valores

#Quando definimos uma função, definimos parâmetros que são passados
#Quando invocamos a função definimos os argumentos passados pra função

def soma(x, y): #Aqui definimos os parâmetros
	return x+y
print(soma(2, 4)) #Aqui passamos argumentos para a função

###############################################################################
#Parâmetros Default
#Deve-se passar primeiro os parâmetros que não são inicializados
def login(system, user = "admin", password = "123"):
	print("User: {}".format(user))
	print("Password: {}".format(password))

login(None)
print("\n")

###############################################################################
#Argumentos posicionais e nomeados
#Argumentos posicionais: cada valor deve ser passado na ordem da implementação da função 
#Argumentos nomeados: associação com o nome do parâmetro e o valor que é enviado

def personal_data(name, age, sex):
	print("Nome: {}\nIdade: {}\nSexo: {}".format(name, age, sex))

personal_data("Vitor", 23, "M")						#Argumentos posicionais
personal_data(sex = "M", name = "Vitor", age = 23)  #Argumentos nomeados
#Argumentos posicionais são passados como uma tupla
#Argumentos nomeados são passados como um dicionário