# Analogia: Sets são como nomes de um sorteio em uma caixa. Você sabe todos os
# itens que estão lá, você pode adicionar e remover elementos, mas não pode
# alterar os elementos que estão nele.

# Sets são uma coleção desordenada e não indexadas
# Não é possível alterar um item, mas é possível adicionar e 
# remover novos itens

s = {"apple", "banana", "cherry"}

# Não é possível acessar um item do set pelo índice. É necessário usar um for
for item in s:
    print(s)


# Adicionar um item ao set
s.add("orange")
# Adicionar vários itens ao set
s.update(["mango", "grapes"])


# Remover itens do set
s.remove("banana")
s.discard("banana")
# A função remove() gera um erro caso o elemento não exista
# A função discard() retorna None caso o elemento não exista

# Remover e retornar item deletado
# Remove o último item, mas como o set é desordenado 
# você não sabe qual item vai ser removido
s.pop()

# Remover todos os elementos do set
s.clear()
del s 
# clear remove os elementos do set mas mantém a variável do tipo set na memória 
# del remove os elementos do set, inclusive a própria variável

# Comprimento do set
print(len(s))

# Extender conteúdo de um set
set1 = {1, 2, 3}
set2 = {4, 5, 6}

set3 = set1.union(set2) # Extende o set em uma nova variável
set1.update(set2)       # Extende o set sem precisar de uma nova variável