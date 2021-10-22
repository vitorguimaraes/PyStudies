users = {"Marcelo": 97864537, 
				"Daniel": 99673450, 
				"André": 88432865, 
				"Laís": 99432764,
				"Márcia": 88653421,
				"Kelly": 99563856,
				"Ana": 97824423}

# Percorrendo dicionários
for key, value in users.items():
	print("Friend {} has phone number {}".format(key, value))

# Acessando chaves específicas do dicionário:
users["Laís"]	# sintaxe: dict[key]

# Removendo itens do dicionário:
del(users["Daniel"]) # sintaxe: del(dict[key]) 

# Retornar chaves do dicionário:
users.keys()

# Retornar valores do dicionário:
users.values()

# Verificar se uma chave ou valor está contido no dicionário:
if "Marcelo" in users.keys(): # verifica se a chave está contida no dicionário
	print("True")

if 88653421 in users.values(): # verifica se o valor está contido no dicionário
	print("True")

# Retornar e excluir item do dicionário
users.popitem()

# Unir dicionários
new_dict = {"João": 98451243,
			"Maria": 89543512}

users = {"Marcelo": 97864537, 
				"Daniel": 99673450, 
				"André": 88432865, 
				"Laís": 99432764,
				"Márcia": 88653421,
				"Kelly": 99563856,
				"Ana": 97824423}

users.update(new_dict)


# Não é incomum ver índices codificados 
# por exemplo, ponto [0], itens [1], vals [-1]
# Sempre que você ver índices codificados em seu código, pare para considerar 
# se você poderia usar várias atribuições para tornar seu código mais legível.


# ************************************ #
# ***** Dictionary Comprehension ***** #
# ****************************** ***** #

# Problema: Você tem uma lista de usuários em que cada item contém
# um usuário com id, nome e senha. Você precisa acessar as informações
# de um determinado usuário tomando seu nome por referência 

users = [
	(0, "Bob", "password"), 
	(1, "Rolf", "rolf123"),
	(2, "Jose", "longpassword"),
	(3, "username", "1234"),
]

# Solução comum:
for user in users:
	if user[1] == "Bob":
		# do something

users_mapping = {user[1]: user for user in users}
user_info = users_mapping["Bob"] 
user_info[0] # Acessa o id
user_info[1] # Acessa o nome
user_info[2] # Acessa a senha

# *obs: Com essa solução é possível apenas ler os dados, mas não é possível
# sobescrever, por a consulta é feita a partir de uma cópia da lista principal