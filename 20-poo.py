###############################################################################
# Membros de classe
# Os membros de classe são compartilhados entre os objetos

class MinhaClasse():
    membro_classe = 50

    def __init__(self):
        self.membro_inst = -10

    def func(self):
        print(self.membro_classe)
        print(self.membro_inst)


obj1 = MinhaClasse()
obj2 = MinhaClasse()

obj1.membro_inst = 0
obj2.membro_inst = 1

print("obj1 membro_classe: {}".format(obj1.membro_classe))
print("obj1 membro_inst: {}".format(obj1.membro_inst))

print("obj2 membro_classe: {}".format(obj2.membro_classe))
print("obj2 membro_inst: {}".format(obj2.membro_inst))
print("-------------------------------------------------")
# Equivalente a:
obj1.func()
obj2.func()

# Acessando e modificando membros de classe:
MinhaClasse.membro_classe = 1000
print("\n")

###############################################################################

# Métodos de Classe
class Bichos():
    qtd_bichos = 0

    def __init__(self):  # Método construtor
        self.add_bicho()

    def __del__(self):  # Método destrutor
        self.del_bicho()
        if self.qtd_bichos == 0:
            print("Todos os bichos foram mortos!")

    @classmethod
    def add_bicho(cls):  # O parâmetro cls indica que é um parâmetro de classe
        cls.qtd_bichos += 1

    @classmethod
    def del_bicho(cls):
        cls.qtd_bichos -= 1


b1 = Bichos()
b2 = Bichos()
b3 = Bichos()

print(Bichos.qtd_bichos)
print("\n")

###############################################################################
# Métodos Estáticos
# Podem ser invocados por meio de um objeto ou da instância da classe

class MetodosEstaticos():

    @staticmethod
    def func1():
        print("Método estático 1")

    @staticmethod
    def func2(a, b, c):
        info = """
        Nome da função: {nome} 
        Quantidade de Args: {quantidade}
        Args: {args}
        """
        info = info.format(
            nome=MetodosEstaticos.func2.__name__,
            quantidade=MetodosEstaticos.func2.__code__.co_argcount,
            args=MetodosEstaticos.func2.__code__.co_varnames
        )
        print(info)


obj = MetodosEstaticos()
obj.func1()
MetodosEstaticos.func1()

obj.func2(1, 2, 3)
MetodosEstaticos.func2(1, 2, 3)