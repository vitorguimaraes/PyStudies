a = 10
b = 50

######################################
if a == 10:
	print("O valor de a é igual a 10")
######################################

if a == 10:
	print("O valor de a é igual a 10")

if b == 50:
	print("O valor de b é igual a 50")

if a == 10 and b == 50:
	print("O valor de a é igual a 10 e de b é 50")

else:
	print("nothing")
######################################
if a == 30:
	print("passing")

elif a == 25:
	print("passing")

elif a == 10:
	print("O valor de a é igual a 10\n\n")
######################################

#Usar if encadeados faz com que todas as expressões sejam verificadas
#Se você não precisa que todas as expressões sejam verificadas, use elif, pois
#o programa irá retornar após encontrar um elif verdadeiro, sem verificar as 
#demais expressões

idade = int(input("Informe sua idade:"))

if idade <= 0:
	print("A sua idade não pode ser 0 ou menor que 0")

elif idade > 150:
	print("A sua idade não pode ser superior a 150 anos")

elif idade < 18:
		print("Você precisa ter mais de 18 anos")