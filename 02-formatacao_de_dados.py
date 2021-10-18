
# Não é necessário declarar o encoding no python3, as strings já são unicode

num_float = 3.123456789
variavel = "olá"

# % formatting
# Porque é ruim: Quanto maior sua string, menos legível fica seu código 
print("O valor do número float é: %.3f" %num_float)
print("A string é: %s" %variavel)


# str.format()
# Porque é ruim: Pode ficar muito verboso quando você lida com muitos 
# parâmetros e strings
print("O valor do número float é: {0:.3f}".format(num_float))
print("O valor da string é {}".format(variavel))


# f-strings
# Vantagens:
# - Aceita expressões 
# - Aceita chamadas de funções e métodos
# - É mais rápido que % formatting e str.format()
# Printar o valor de uma variável float
print(f'O valor do número float é {num_float:0.3f}')
print(f'A string é {variavel}')