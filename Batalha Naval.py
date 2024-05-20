from random import randint
from colorama import init, Fore, Back, Style
import functools
init()

Carrier = 5
Dread = 4
Cruiser = 2
Sub = 1
simbol = ('✖','✦')

grid = {'A': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'B': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'], 
        'C': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'D': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'E': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'F': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'G': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'H': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'I': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|'],
        'J': ['~|','~|','~|','~|','~|','~|','~|','~|','~|','~|']}

# ===========================================================================================================
# Funções que fazem a máquina colocar todos os barcos em posições aleatórias
# ===========================================================================================================

def validate_pos(funcao):
    @functools.wraps(funcao)
    def teste(grid):
        nome_linha = ['A','B','C','D','E','F','G','H','I','J']
        pos_init = []
        contador = 0

        while contador < 5:
            x, y = funcao()
            pos_linha = nome_linha[x]
            if grid[pos_linha][y] not in pos_init:
                pos_init.append(f'{pos_linha}/{y}')
                contador += 1
    
        return pos_init

    return teste

@validate_pos
def posicao_barcos():
    linha = randint(1,10)
    coluna = randint(1,10)

    return linha, coluna
            
def restante_do_barco(inicial):
    barcos = {'Carrier':[], 'Dread':[],'Cruiser':[], 'Sub':[]}
    nome_linha = ['A','B','C','D','E','F','G','H','I','J']

    if (l:= nome_linha.index(inicial[0][0]) - 5) >= 0:
        pass


    return
# ===========================================================================================================

print(posicao_barcos(grid))

#inicial = posicao_barcos(grid)