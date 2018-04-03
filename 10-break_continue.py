#Com a instrução break, o fluxo de execução é interrompido e sai do loop

for i in range(10):
	if i == 5:
		break
	print(i)

#Com a instrução continue, o fluxo de execução é interrompido e volta para o 
#início do loop. No exemplo abaixo, quando i for par o print não será 
#executado, e o programa volta para a primeira linha do while
#Quando i for ímpar, o fluxo de execução passa pelo print

i = 0
while i<10:
	i += 1
	if(i%2 == 0):#Se i for par
		continue
	print(i) 	 #Não executa quando i é par