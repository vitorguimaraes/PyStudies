
# Não é necessário declarar o encoding no python3, pois as strings já são unicode

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
print(f'A string é {variavel}')
print(f'O valor do número float é {num_float:0.3f}')

# formatting
library = [
  ('Author', 'Topic', 'Pages'), 
  ('Twain', 'Rafting', 601), 
  ('Feyman', 'Physics', 95), 
  ('Hamilton', 'Mythology', 144)
]

for author, topic, pages in library: 
  print(f"{author:10} {topic:10} {pages:>{10}}")
#Author     Topic           Pages
#Twain      Rafting           601
#Feyman     Physics            95
#Hamilton   Mythology         144

