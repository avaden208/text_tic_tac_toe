import random

#TODO: convert to use classes
#TODO: add two player option


#class TikTacToe():

    #def __init__(self):

default_values = {'1':'1', '2':'2', '3':'3',
                  '4':'4', '5':'5', '6':'6',
                  '7':'7', '8':'8', '9':'9', }
grid_values = default_values.copy()

still_playing = True

#     1 | 2 | 3
#    ---+---+---
#     4 | 5 | 6
#    ---+---+--- 
#     7 | 8 | 9 
def print_grid():
    sep = '---+---+---'
    line1 = ' {} | {} | {} '.format(grid_values['1'], grid_values['2'], grid_values['3'])
    line2 = ' {} | {} | {} '.format(grid_values['4'], grid_values['5'], grid_values['6'])
    line3 = ' {} | {} | {} '.format(grid_values['7'], grid_values['8'], grid_values['9'])    
    print(line1)
    print(sep)
    print(line2)
    print(sep)
    print(line3)
    print('')

def is_grid_full():
    grid_full = True
    for i in range(9):
        if str(i+1) in grid_values.values():
            grid_full = False
            break
    return grid_full

def choose_spot():
    choice = input('Choose your spot: ')
    if choice in grid_values.keys():
        if grid_values[choice] != 'x' and grid_values[choice] != 'o':
            grid_values[choice] = player_char
        else:
            print('That spot is already taken, try again.')
            return False
    else:
        print('That is not a valid choice, try again.')
        return False
    return True

def npc_spot():
    npc_char = 'x' if player_char == 'o' else 'o'
    choice = str(random.randint(1,9))
    try:
        if choice in grid_values.keys():
            if grid_values[choice] != 'x' and grid_values[choice] != 'o':
                grid_values[choice] = npc_char
            else:
                npc_spot()
    except Exception as ex:
        print(f'Exception: {str(ex)}')

def is_winning_combo():
    # 8 winning combo options
    if grid_values['1'] == grid_values['2'] == grid_values['3']:
        return True, grid_values['1']
    elif grid_values['4'] == grid_values['5'] == grid_values['6']:
        return True, grid_values['4']
    elif grid_values['7'] == grid_values['8'] == grid_values['9']:
        return True, grid_values['7']
    elif grid_values['1'] == grid_values['4'] == grid_values['7']:
        return True, grid_values['1']
    elif grid_values['2'] == grid_values['5'] == grid_values['8']:
        return True, grid_values['2']
    elif grid_values['3'] == grid_values['6'] == grid_values['9']:
        return True, grid_values['3']
    elif grid_values['1'] == grid_values['5'] == grid_values['9']:
        return True, grid_values['1']
    elif grid_values['3'] == grid_values['5'] == grid_values['7']:
        return True, grid_values['3']
    else:
        return False, '0'
    
def reset():
    grid_values = default_values.copy()
    print_grid()


player_char = input('Choose your side, "x" or "o": ')
if player_char.lower() != 'x':
    player_char = 'o'
    print('Great, you will be "o"\n')
else:
    print('Great, you will be "x"\n')

print_grid()
while still_playing:    
    while not choose_spot():
        pass
    if not is_grid_full():
        npc_spot()
    print_grid()
    win, winner = is_winning_combo()
    if win:
        again = input(f'The winner is {winner}!! Try again? "Y" or "N": ')
        if again.lower() != 'y':
            still_playing = False
        else:
            #reset()
            grid_values = default_values.copy()
            print_grid()
    if(is_grid_full()):
        still_playing = False
        again = input('No winner, try again? "Y" or "N": ') 
        if again.lower() != 'y':
            still_playing = False
        else:
            #reset()
            grid_values = default_values.copy()
            print_grid()