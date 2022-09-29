import random

def get_player(player_0:str, player_1:str) -> str:
    '''
    Получение имени игроков
    Определение первого хода
    '''
    print('Сейчас мы разыграем право первого хода')
    temp = random.randint(0,1)
    if temp == 0:
        gamer = player_0
    else:
        gamer = player_1
    print(f'И первым у нас берет конфеты {gamer}')

def playing(candy:int, player:str, player_1:str, player_2:str):
    winner = ''
    while candy>0:
        if candy>28:
            if player == player_1:
                print(f'У нас {candy} конфет')
                move = get_number(f'{player}, сколько вы берете конфет? Вы можете взять от 1 до 28:')
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет')
                move = random.randint(1,28)
                print(f'Я беру {move} конфет')
                candy -= move
                player = player_1
                winner = player_2
        else:
            if player == player_1:
                print(f'У нас {candy} конфет')
                move = last_move(f'{player}, сколько вы берете конфет? Вы можете взять от 1 до {candy}: ', candy)


