# Importação de símbolos
from math import sqrt

# Renomeação de símbolos
# import pygame as pg

# Importando todos os símbolos de um módulo que não estão definidos como privado
# Não é recomendado fazer este tipo de importação, pois é custoso ficar acessando 
# o disco para fazer a busca de símbolos
from socket import *

# Printar todas as funções de um módulo
import math
module = enumerate(dir(math))
for key, value in module: 
	f'{key} - {value}'

# No python o módulo principal possui o nome __main__
f'Name: {__name__}'

# Localização de módulos
# Todos os paths que o Python verifica estão na variável path do módulo sys
# Primeiro o Python verifica se o módulo importado é __builtin__
# Se não for, então ele procura o módulo em uma lista de path
# O primeiro path é o diretório em que o programa está sendo executado
# O segundo path é o diretório da variável PYTHONPATH
# O terceiro path é o diretório da biblioteca padrão, onde o python está instalado
# Em último caso, se houver um arquivo de diretórios definidos em um arquivo *.pth,
# o Python buscará os módulos nos paths definidos nesse arquivo
from pprint import pprint
from sys import path 
pprint(path)

###############################################################################
# Etapas da importação de módulos:
# Localização, compilação (.pyc) e execução
# Quando um módulo é importado o Python já o executa e guarda na memória
# Os módulos não são reexecutados 

###############################################################################
# Símbolos Privados
# São usados apenas pelo módulo que a contém. Se o módulo for importado em outro
# programa o usuário não tem acesso a essas variáveis

# Suponha que o código abaixo faz parte do módulo ferramentas.py:
_private_variable1  = 10
_private_variable12 = 20

non_private = _private_variable1 + _private_variable12

# Ao importar o módulo ferramentas.py o usuário não tem acesso às variáveis
# privadas, apenas à variável non_private. Porém, é possível importar 
# símbolos privados explicitamente
# Ex:
from ferramentas import * #Não tem acesso às variáveis privadas
from ferramentas import _private_variable1 # Dessa forma tem acesso à variável

###############################################################################
# Símbolos Públicos
# Com a instrução __all__ podemos definir os símbolos que serão importados 
# na importação do módulo
# Suponha que o código abaixo faz parte do módulo tools.py

__all__ = ['aa', 'bb']	

aa = 0
ab = 1
ba = 2
bb = 3
###########
from tools import* # Só serão importados os símbolos aa e bb

###############################################################################
# Módulo Principal (main)
# Internamente, o Python nomeia o script que está sendo executado como __main__
# O bytecode do main é gerado e executado na memória em tempo de execução

if __name__ == '__main__':
	pass  					