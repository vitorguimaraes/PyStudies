# sintaxe do range:
# range([start], stop[, step])

my_range = range(0, 100, 5)
for x in my_range:
	print x

# O range inicia exatamente no START, e vai até o penúltimo valor de STOP
# Caso seja passado um STEP, a iteração é feita a cada STEP

# Criando um range inverso
my_range = list(range(10, 0, -1))

# A função range retorna um objeto da classe range 
# Para gerar uma lista com o range do python3, é necessário fazer um cast
#Ex:
#lista = list(range(10))

print(type(my_range))

