contact_list = {"Marcelo": 97864537, 
				"Daniel": 99673450, 
				"André": 88432865, 
				"Laís": 99432764,
				"Márcia": 88653421,
				"Kelly": 99563856,
				"Ana": 97824423}

#Percorrendo dicionários
for key, value in contact_list.items():
	print("Friend {} has phone number {}".format(key, value))
print("\n")

#Acessando chaves específicas do dicionário:
print(contact_list["Laís"])	#dict[key]

#Removendo itens do dicionário:
del(contact_list["Daniel"]) #sintaxe: del(dict[key]) 
print(contact_list)

#Retornar chaves do dicionário:
print(contact_list.keys())

#Retornar valores do dicionário:
print(contact_list.values())

#Verificar se uma chave ou valor está contido no dicionário:
if "Marcelo" in contact_list.keys(): #verifica se a chave está contida no dicionário
	print("True")

if 88653421 in contact_list.values(): #verifica se o valor está contido no dicionário
	print("True")

#Retornar e excluir item do dicionário
print(contact_list.popitem())

#Unir dicionários
new_dict = {"João": 98451243,
			"Maria": 89543512}
contact_list = {"Marcelo": 97864537, 
				"Daniel": 99673450, 
				"André": 88432865, 
				"Laís": 99432764,
				"Márcia": 88653421,
				"Kelly": 99563856,
				"Ana": 97824423}
contact_list.update(new_dict)
print(contact_list)

#Não é incomum ver índices codificados 
#por exemplo, ponto [0], itens [1], vals [-1]):
#Sempre que você ver índices codificados em seu código, pare para considerar 
#se você poderia usar várias atribuições para tornar seu código mais legível.