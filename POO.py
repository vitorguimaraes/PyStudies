# Classe: é o projeto de um objeto
# Objeto: é a execução do código de uma classe
# Instância: é sinônimo de objeto
# Propriedades: são variáveis que armazenam atributos
# Métodos: são as funções que o objeto pode realizar


# Herança, polimorfismo, encapsulamento, abstração
# Classe abstrata, método abstrato
# Atributo de classe, Método de classe
# Property (get e setter)
# __ e _

################################# Herança #################################
# Cenário: O Netflix possui filmes e séries. Ambos possuem nome, ano de lançamento e likes
# Filmes possuem   
class Programas():
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano 
        self.likes = 0

    @property
    def likes(self):
        return self.likes

    @
        self._likes += 1