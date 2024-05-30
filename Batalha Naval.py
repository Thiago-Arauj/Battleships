from random import randint
from colorama import init, Fore, Back
from os import system
import functools
init(autoreset=True)

grid = {'A': [0,1,2,3,4,5,6,7,8,9,10],
        'B': [0,1,2,3,4,5,6,7,8,9,10], 
        'C': [0,1,2,3,4,5,6,7,8,9,10],
        'D': [0,1,2,3,4,5,6,7,8,9,10],
        'E': [0,1,2,3,4,5,6,7,8,9,10],
        'F': [0,1,2,3,4,5,6,7,8,9,10],
        'G': [0,1,2,3,4,5,6,7,8,9,10],
        'H': [0,1,2,3,4,5,6,7,8,9,10],
        'I': [0,1,2,3,4,5,6,7,8,9,10],
        'J': [0,1,2,3,4,5,6,7,8,9,10]}

# ===========================================================================================================
# Funções que fazem a máquina colocar todos os barcos em posições aleatórias
# ===========================================================================================================

# Decorador que gera o restante dos barcos
def ship_complete(funcao):
    @functools.wraps(funcao)
    def auto_completer():
        nome_linha = ['A','B','C','D','E','F','G','H','I','J']
        while True:
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

            if intersect_check(ships):
                break
        
        return ships

    return auto_completer


# Função que irá gerar as posições iniciais dos barcos
@ship_complete
def ship_init():
    x = randint(1,10)
    y = randint(1,10)

    return x, y

def intersect_check(ships):
    a = set(ships['Carrier'])
    b = set(ships['Dread'])
    c = set(ships['Destroyer'])
    d = set(ships['Sub1'])
    e = set(ships['Sub2'])

    total_check = 0
    Test = [a,b,c,d,e]

    for i in Test:
        each_check = 0
        for j in Test:
            if i == j:
                pass
            else:
                if i.isdisjoint(j):
                    each_check += 1
        
        if each_check == 4:
            total_check += 1
    
    if total_check == 5:
        return True
    else:
        return False
            



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

        elif (C := column - size) > 0:
            for colunas in range(C, column):
                ships[i].append(f'{x}/{colunas}')
    
    return ships

# Gera os barcos na horizontal
def horizontal_generator(size, row, x, column, ships, i):
    nome_linha = ['A','B','C','D','E','F','G','H','I','J']
    if (C := column + size) < 10:
        for colunas in range(column, C):
            ships[i].append(f'{x}/{colunas}')

    elif (C := column - size) > 0:
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

def grid_show(funcao):
    @functools.wraps(funcao)
    def wrapping(*args, **kwargs):
        funcao(*args, **kwargs)
        simbol = ('✖','✦')
        print('  ', end='')
        for n in range(1,11):
            print(n, end=' ')
        print()
        
        for linha in grid:
            print(linha, end=' ')
            for coluna in range(len(grid[linha])):
                if grid[linha][coluna] == 0:
                    pass
                elif type(grid[linha][coluna]) == int:
                    print(Back.BLUE + '~',end=Back.BLUE + ' ')
                elif type(grid[linha][coluna]) == str:
                    if grid[linha][coluna] == simbol[0]:
                        print(Fore.YELLOW + grid[linha][coluna], end=Back.BLUE + ' ')
                    elif grid[linha][coluna] == simbol[1]:
                        print(Fore.RED + grid[linha][coluna], end=Back.BLUE + ' ')

            print()
    
    return wrapping

@grid_show
def is_in(pos,barcos,grid):

    simbol = ('✖','✦')
    x, y = pos.split('/')
    y = int(y)

    ship_hit = False

    for name in barcos:
        if pos in barcos[name]:
            ship_hit = True
            ship_name = name
    
    if ship_hit:
        barcos[ship_name].remove(pos)
        grid[x][y] = simbol[1]
    else:
        grid[x][y] = simbol[0]
    
    return grid

    
def check_sink(barcos):

    doomsday_counter = []

    for nome in barcos:
        if len(barcos[nome]) == 0:
            doomsday_counter.append(nome)
    
    return doomsday_counter

     


    

# ===========================================================================================================


barcos = ship_init()
print(barcos)
no_repeat = 0
Wanna_play = 1
Partidas = 0
Record = []


while Wanna_play > 0:
    info = 0
    play = int(input(Fore.WHITE + 'Quer jogar?\n[1] Sim!\n[0] Não\n'))
    contador = 0

    if play == 1:

        while True:
            pos = input('Digite um par de coordenadas nesse modelo "A/5"\n').upper()
            if '0' in pos and '1' not in pos:
                print(Fore.RED + 'Posição inválida, por favor tente novamente!')
                pass
            else:
                system('cls')
                is_in(pos,barcos,grid)

                counter = check_sink(barcos)
                contador += 1

                if len(counter) == 5:
                    print(Fore.YELLOW + f'Parabéns soldado, você afundou todos eles em {contador} jogadas!')
                    break
                elif len(counter) > no_repeat:
                    print(Fore.YELLOW + f'Parabéns soldado, já afundou {len(counter)} navio(s) do inimigo')
                    print(Fore.RED + 'Eram eles')
                    for barco in counter:
                        print(Fore.RED + f'{barco}')
                
                
                no_repeat = len(counter)
            
    
    Partidas += 1
    info = (Partidas, contador)
    Record.append(info)
else:
    print(Fore.WHITE + 'Tudo bem! Aqui está seu histórico')
    for partida in Record:
        print(Fore.WHITE + f'Partida {partida[0]} terminou em {partida[1]} jogadas!')