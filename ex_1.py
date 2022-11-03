#1. Создайте программу для игры с конфетами человек против человека.
# Победная стратегия для компьютера: после хода компьютера на столе должно оставаться количество конфет, кратное максимальному ходу + 1 (макс+1).
# После каждого хода игрока компьютер должен забирать недостающее количесво до кратного макс+1 остатка.
# Два момента, нарушающих работу алгоритма, решены просьбой компьютера ввести другие параметры.
print('Добрый день! Давайте сыграем в игру с конфетами.')
print('Вы решите, сколько конфет будет на столе и по жребию по очереди с компьютером будете забирать себе конфеты в установленном Вами количестве.')
print('Все конфеты достаются сделавшему последний ход.')
print('Игрок, взявший некорректное количество конфет, проигрывает игру.')
print('Сейчас мы проведем жеребьевку между Вами и компьютером за право сделать первый ход. ')
print('Компьютер случайным образом выберет 1 или 2, означающую, будет он ходить первым или вторым')
import random
bot = random.randint(1, 2)
print(f'Компьютер выбрал, что он будет ходить {bot}ым.')
print('Задайте через пробел общее количество конфет и максимальное количество конфет, которое может взять игрок.')
entered_list = input().split()
num_list = [int(i) for i in entered_list]
total_candies = num_list[0]
remaining_candies = total_candies
max_step = num_list[1]
min_step = 1
steps = total_candies//(max_step + 1)
print(f'Итак, на столе {total_candies} конфет, за один ход можно взять не менее 1 и не более {max_step} конфет.')

def candies_game():
    global remaining_candies

    for i in range(1, steps+1):
        if remaining_candies > 0:
            print(f'Ваш ход. Возьмите конфеты (от 1 до {max_step}):')
            step1 = int(input())
            if 1 <= step1 <= max_step:
                step2 = (max_step + 1) - step1
                print(f'Компьютер взял {step2} конфет.')
                remaining_candies = remaining_candies - (step2 + step1)
                print(f'Осталось {remaining_candies} конфет.')
                i += i

            else:
                print(f'Вы ввели некорректное количество конфет (от 1 до {max_step}), нарушили правила игры и проиграли.')
                break
        else:
            print('Компьютер победил в игре и выиграл все конфеты. Сыграем еще раз?')
            exit()

if bot == 1:
    if total_candies % (max_step + 1) != 0:
        step_bot = total_candies % (max_step + 1)
        remaining_candies = total_candies - step_bot
        print(f'Компьютер взял {step_bot} конфет, осталось {remaining_candies} конфет.')
        candies_game()
    else:
        print('Один из двух введенных Вами параметров существенно замедляет работу программы.')
        print('Начните заново, изменив любой из них хотя бы на 1.')
        exit()
else:
    print(f'Ваш ход. Возьмите конфеты (от 1 до {max_step}):')
    step1 = int(input())
    if (total_candies - step1) % (max_step + 1) != 0:
        step2 = (total_candies - step1) % (max_step + 1)
        print(f'Компьютер взял {step2} конфет.')
        remaining_candies = total_candies - (step1 + step2)
        print(f'Остаток {remaining_candies} конфет.')
        candies_game()
    else:
        print('Один из трех введенных Вами параметров существенно замедляет работу программы.')
        print('Начните заново, изменив любой из них хотя бы на 1.')
        exit()

print('Компьютер победил в игре и выиграл все конфеты. Сыграем еще раз?')

