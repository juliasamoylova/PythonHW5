from random import randint

a = int(input('Введите количество конфет'))
hod = 0
wins = {0:'Игрок', 1:'Бот'}
while a>0:
    if a<= 28:
        print(f'Выиграл {wins[hod]}')
        break
    if hod%2 == 0:
        print('Ход игрока')
        d = int(input('Введите количество конфет, которое хотите взять: '))
        a -= d
        print(f'Осталось конфет {a}')
    else:
        print('Ход бота')
        d = a%29
        a -= d
        print(f'Осталось конфет {a}')
    hod = (hod+1)%2
            
