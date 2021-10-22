# Métodos Estáticos
# É atribuído à classe, não aos objetos
# Não pode acessar ou alterar o estado da classe, pois não recebe cls ou self
# Funciona como uma função comum, mas faz parte da classe

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi