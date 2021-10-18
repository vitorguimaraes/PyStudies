################################# Herança #################################
# Cenário: Uma pessoa possui nome, e cpf 
# Um funcionário possui tudo que uma pessoa possui, além de: matrícula e cargo

class Person():
    def __init__(self, name: str, cpf: str) -> None:
        self._name = name 
        self._cpf  = cpf

    @property
    def name(self):
        return self._name 

    @property
    def cpf(self):
        return self._cpf


# O método super() chama o inicializador da classe mãe
# Nele passamos os atributos que a classe mãe recebe
class Worker(Person):
    def __init__(self, name: str, cpf: str, register: str, role: str) -> None:
        super().__init__(name, cpf)
        self._register = register 
        self._role     = role 

    @property
    def register(self):
        return self._register

    @register.setter
    def register(self, new_register: str) -> None:
        self._register = new_register