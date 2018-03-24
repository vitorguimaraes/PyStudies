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
#Para gerar uma lista com o range do python3, é necessário fazer um cast
#Ex:
#lista = list(range(10))

print(type(my_range))

#Range vs xRange

#Se executarmos 

# for i in range(0, 1000000000):
    # pass

#A função range() do Python2 irá imediatamente gerar uma lista contendo um 
#bilhão de inteiros e tentar alocar essa lista na memória. 

#Já com a função xrange(), ao executarmos:	

# for i in xrange(0, 1000000000):
#     pass

#Cada um dos inteiros (dos 1 bilhão) será gerado por vez, economizando memória 
#e tempo de startup

#No python3 a função range() original foi removida e eles renomearam a função
#xrange() para range()

#Executando os comandos abaixo no terminal percebemos que a função xrange() do 
#python2 é mais rápida do que o range() do python3

#python -m timeit "for i in xrange(10000000): pass"
#python3 -m timeit "for i in range(10000000): pass"


#O range() do python3 suporta slicing, enquanto o xrange do python2 não suporta:
print(range(10)[2:])