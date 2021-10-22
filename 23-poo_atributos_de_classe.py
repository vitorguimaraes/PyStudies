# Atributos de classe
# Os atributos de classe são compartilhados entre os objetos e são definidos
# fora do método __init__
# São acessíveis por objetos, mas só podem ser alterados se invocados
# pela classe

class MinhaClasse():
    atributo_de_classe = 50

    def __init__(self):
        self.atributo_de_instancia = -10

obj1 = MinhaClasse()
obj2 = MinhaClasse()

obj1.atributo_de_classe # Acessando atributo de classe pelo objeto 1
obj2.atributo_de_classe # Acessando atributo de classe pelo objeto 2

# Acessando e alterando atributos de classe:
MinhaClasse.atributo_de_classe = 100
