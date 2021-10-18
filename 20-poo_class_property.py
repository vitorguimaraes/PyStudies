# Classe: é o projeto de um objeto
# Objeto: é a execução do código de uma classe
# Instância: é sinônimo de objeto
# Propriedades: são variáveis que armazenam atributos
# Métodos: são as funções que o objeto pode realizar

# __init__: método construtor. Quando um novo objeto é instanciado, 
# ele é invocado automaticamente, passando os atributos dos argumentos
# self: representa a instância da classe

# Definimos os atributos com um underscore
# Utilizar dunders impede que classes filhas herdem atributos privados, 
# por causa do name mangling 
# Não é necessário criar setters se você não precisa alterar o atributo

class Hero():
    def __init__(self, name: str, hp: int, attack: int, defense: int) -> None:
        self._name    = name
        self._hp      = hp  
        self._attack  = attack 
        self._defense = defense 

    @property 
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp 
    
    @hp.setter 
    def hp(self, new_hp: int) -> None:
        self._hp = new_hp

    @property 
    def attack(self):
        return self._attack

    @attack.setter 
    def attack(self, new_attack: int) -> None:
        self._attack = new_attack

    @property
    def defense(self):
        return self._defense
    
    @defense.setter 
    def defense(self, new_defense: int) -> None:
        self._defense = new_defense



Type hints
Type annotations

# Herança múltipla, Mixin
# Classe abstrata, método abstrato
# Atributo de classe, Método de classe
# Property (get e setter)
# Membros de classe
# Métodos de classe
# Métodos estáticos
# Duck typing (__getitem__, __repr__,
 # Python Data Model

Inicialização: __init__
Representação: __str__, __repr__
Container, sequencia: __contains__, __iter__, __len__, __getitem__
Numéricos: __add__, __sub__, __mul__, __mod__
 