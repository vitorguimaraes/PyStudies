# Falta: Herança, Polimorfismo, Encapsulamento e Abstração


# Classe: é o projeto de um objeto
# Objeto: é a execução do código de uma classe
# Instância: é sinônimo de objeto
# Propriedades: são variáveis que armazenam atributos
# Métodos: são as funções que o objeto pode realizar

class Retangulo():
    def __init__(self):
        self.altura = 0 
        self.largura = 0

    def area(self):
        return self.altura * self.largura

# Instanciando um objeto da classe
r1 = Retangulo()

# Acessando e modificando atributos:
r1.altura = 10
r1.largura = 15 

# Invocando métodos:
r1.area()

###############################################################################
# Método Construtor Personalizado

class Circulo():
    def __init__(self, raio):
        self.r = raio

    def area(self):
        return 3.14 * self.r * self.r


circulo = Circulo(3)
print(circulo.area())

###############################################################################
# Setters e Getters

class Quadrado():
    def __init__(self, lado):
        self.lado = 0
        self.set_lado(lado)

    def set_lado(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            # O programa encerra
            raise ValueError("O valor de lado deve ser inteiro!")
        self.lado = num

    def get_area(self):
        return self.lado * self.lado


# Visibilidade de membros (propriedades e métodos)
publico = 0
_restrito = 0  #Esse atributo não pode ser acessado diretamente


class Quadrado():
    def __init__(self, lado):  
        self._lado = 0
        self.set_lado(lado)

    def set_lado(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            # O programa encerra
            raise ValueError("O valor de lado deve ser inteiro!")
        self._lado = num

    def get_area(self):
        return self._lado * self._lado


# Para evitar a colisão de nomes entre a superclasse e a subclasse o membro
# deve ser precedido por dois underlines (dunders)
__colisao = 0

###############################################################################
# Property

class A():
    def __init__(self):
        self._var = 0

    def _get_var(self):
        return self._var

    def _set_var(self, num):
        self._var = num

    var = property(fget=_get_var, fset=_set_var)


a = A()
a.var = 10
print(a.var)
print("\n")
###############################################################################
# Decorators
# O decorador de método adiciona funcionalidades ao método sem alterar sua implementação

class B():
    def __init__(self):
        self._var = 0

    # Ao definir property usando decorator o nome da função deve 
    # ser o mesmo da propriedade
    @property
    def var(self):  
        return self._var

    @var.setter
    def var(self, num):
        self._var = num


b = B()
b.var = 15
print(b.var)

###############################################################################
# Exemplo:


class Rectangle():
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def largura(self):
        return self._largura

    @largura.setter
    def largura(self, largura):
        if(not(isinstance(largura, int) and (largura > 0))):
            raise ValueError("O valor inserido é inválido")
        self._largura = largura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if(not(isinstance(altura, int) and (altura > 0))):
            raise ValueError("O valor inserido é inválido")
        self._altura = altura

    @property
    def area(self):
        return self._largura * self._altura


my_rectangle = Rectangle(10, 20)
my_rectangle.largura = 5
my_rectangle.altura = 7

print(my_rectangle.largura)
print(my_rectangle.altura)
print(my_rectangle.area)

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

###############################################################################
###############################################################################
###############################################################################

# Herança

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.disconnect = True 
        print("Disconnected.")
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by) # chama o init da super classe
        self.capacity = capacity 
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
        
        elif self.connected:
            print("Printing {pages} pages.")
            self.remaining_pages -= pages 