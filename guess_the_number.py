from random import *
from math import log2, ceil
print('Добро пожаловать в числовую угадайку')
larger = ['Нужно чисо меньше, попробуй еще разок', 'Давай-ка еще разок, приятель, нужно поменьше', 'Нужно меньше!', 'Надо поменьше']
smaller = ['Нужно число больше, попробуй еще разок', 'Давай-ка еще разок, приятель, нужно побольше', 'Нужно больше!', 'Надо побольше']
def new_game(): # начнем игру
    print(f'Введите максимальное число, которое можно загадать:')
    global max_num
    max_num = int(input()) # максимальное число
    global some_num, flag, counter
    some_num = randint(1, max_num) # рандомное число
    flag = False
    counter = 0 # счетчик попыток
    return 0

def is_valid(number): # проверка введенного числа на принадлежность промежутку
    if 0 <= int(number) <= max_num:
        return True
    else:
        return False

def num_check(number): # сравнение рандомного и введенного числа
    global counter
    counter += 1
    global flag
    if number > some_num:
        return choice(larger)
    elif number < some_num:
        return choice(smaller)
    else:
        flag = True
        return f'Вы угадали, поздравляем! И потратили на это {counter} попыток\nКстати, оптимальное количество попыток {ceil(log2(max_num))}:)\n'

def try_to_guess(): # основные рассчеты
    print(f'Введите число от 1 до {max_num}:')
    global number
    number = int(input())
    if is_valid(number): # в промежутке ли?
        number = int(number)
        print(num_check(number)) # больше, меньше или равно?
        if flag == True:
            return 0
    else:
        return f'А может быть все-таки введем целое число от 1 до {max_num}?'

new_game()
while True:
    try_to_guess()
    if flag == True:
        print(f'Может сыграем еще разок? да/нет')
        result = input()
        if result in ['lf', 'да']:
            new_game()
        else: 
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...^*^')
            break
