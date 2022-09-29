import random

def playing(candy:int, player:str, player_1:str, player_2:str, messages:list) -> str:
    winner = ''
    while candy >0:
        if candy == 2021 and player == player_2:
            move = 5
            print(f'Я беру {move} конфет')
            candy -= move
            player = player_1
            winner = player_2
        if candy > 28:
            if player == player_1:
                print(f'У нас {candy} конфет')
                index = random.randint(0,4)
                move = get_number_game(f'{player} {messages[index]}. Вы можете взять от одной до 28: ')
                candy -= move
                player = player_2
                winner = player_1
            else:
                print(f'У нас {candy} конфет')
                move = 29 - move
                print(f'я беру {move} конфет')
                candy -= move
                player = player_1
                winner = player_2
        else:
            if player == player_1:
                print(f'У нас {candy} конфет')
                



