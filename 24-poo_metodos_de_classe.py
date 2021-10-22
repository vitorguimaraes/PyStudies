# Métodos de Classe
# É atribuído à classe, não aos objetos
# Pode acessar e alterar o estado da classe
# Cria um novo objeto

class Pizza():
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

pizza1 = Pizza.margherita()
pizza2 = Pizza.prosciutto()