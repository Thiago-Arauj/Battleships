from random import randint
from colorama import init, Fore, Back, Style
import functools
init()

simbol = ('✖','✦')

grid = {'A': [x for x in range(1,11)],
        'B': [x for x in range(1,11)], 
        'C': [x for x in range(1,11)],
        'D': [x for x in range(1,11)],
        'E': [x for x in range(1,11)],
        'F': [x for x in range(1,11)],
        'G': [x for x in range(1,11)],
        'H': [x for x in range(1,11)],
        'I': [x for x in range(1,11)],
        'J': [x for x in range(1,11)]}

# ===========================================================================================================
# Funções que fazem a máquina colocar todos os barcos em posições aleatórias
# ===========================================================================================================

# Decorador que gera o restante dos barcos
def ship_complete(funcao):
    @functools.wraps(funcao)
    def auto_completer():
        nome_linha = ['A','B','C','D','E','F','G','H','I','J']
        ships = {'Carrier': [], 'Dread': [], 'Destroyer': [], 'Sub1': [], 'Sub2':[]}
        
        for i in ships:
            row, column = funcao()
            x = nome_linha[row-1]
            match i:
                case 'Carrier':

                    # Essa variavél serve para determinar se o teste será feito primeiro na vertical ou diagonal
                    # 1 para vertical e 2 para horizontal
                    decision = randint(1,2)

                    if decision == 1:
                        ships = vertical_generator(5, row, x, column, ships, i)

                    elif decision == 2:
                        ships = horizontal_generator(5, row, x, column, ships, i)
                
                case 'Dread':
                    decision = randint(1,2)

                    if decision == 1:
                        ships = vertical_generator(3, row, x, column, ships, i)

                    elif decision == 2:
                        ships = horizontal_generator(3, row, x, column, ships, i)
                
                case 'Destroyer':
                    decision = randint(1,2)

                    if decision == 1:
                        ships = vertical_generator(2, row, x, column, ships, i)

                    elif decision == 2:
                        ships = horizontal_generator(2, row, x, column, ships, i)
                
                case 'Sub1':
                    ships[i].append(f'{x}/{column}')

                case 'Sub2':
                    ships[i].append(f'{x}/{column}')
        
        return ships

    return auto_completer


# Função que irá gerar as posições iniciais dos barcos
@ship_complete
def ship_init():
    x = randint(1,10)
    y = randint(1,10)

    return x, y


# Gera os barcos na vertical
def vertical_generator(size, row, x, column, ships, i):
    nome_linha = ['A','B','C','D','E','F','G','H','I','J']
    if (L := row + size) < 10:
        for linhas in range(row, L):
            ships[i].append(f'{nome_linha[linhas]}/{column}')
    elif (L := row - size) >= 0:
             for linhas in range(L, row):
                ships[i].append(f'{nome_linha[linhas]}/{column}')
    else:
        if (C := column + size) < 10:
            for colunas in range(column, C):
                    ships[i].append(f'{x}/{colunas}')

        elif (C := column - size) >= 0:
            for colunas in range(C, column):
                ships[i].append(f'{x}/{colunas}')
    
    return ships

# Gera os barcos na horizontal
def horizontal_generator(size, row, x, column, ships, i):
    nome_linha = ['A','B','C','D','E','F','G','H','I','J']
    if (C := column + size) < 10:
        for colunas in range(column, C):
            ships[i].append(f'{x}/{colunas}')

    elif (C := column - size) >= 0:
        for colunas in range(C, column):
            ships[i].append(f'{x}/{colunas}')
    else:
        if (L := row + size) < 10:
            for linhas in range(row, L):
                ships[i].append(f'{nome_linha[linhas]}/{column}')
        elif (L := row - size) >= 0:
             for linhas in range(L, row):
                ships[i].append(f'{nome_linha[linhas]}/{column}')

    return ships
 
# ===========================================================================================================

def grid_show(grid,barcos):

    print('  ', end='')
    for n in range(1,11):
        print(n, end=' ')
    
    print()
    
    for linha in grid:
        print(linha, end=' ')
        for coluna in grid[linha]:
            pos = f'{linha}/{coluna}'
            
            if pos in barcos['Carrier']:
                print('X', end=' ')
            else:
                print('~', end=' ')
        print()


# ===========================================================================================================


barcos = ship_init()

print(barcos)
Finished = 0

while True:
    grid_show(grid, barcos)
    break
