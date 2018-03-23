# -*-coding: utf-8-*-

#sintaxe do range:
#range([start], stop[, step])

my_range = range(0, 100, 5)
for x in my_range:
	print x

#O range inicia exatamente no START, e vai até o penúltimo valor de STOP
#Caso seja passado um STEP, a iteração é feita a cada STEP

#No python 2, a função range retorna uma lista
#No python 3, a função range retorna um objeto da classe range 

print type(my_range)
