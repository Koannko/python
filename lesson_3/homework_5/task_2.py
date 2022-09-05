# Игра двоих пользователей

from random import randint


def first_move():
    return randint(0, 1)


def who_goes_now(player_started, move_num):
    return (player_started + move_num) % 2


def get_candy_num_pers(count_of_candies, max_count):
    if count_of_candies >= max_count:
        output = int(input(f'Введите число от 1 до {max_count}\n'))
        if output > max_count:
            get_candy_num_pers(count_of_candies, max_count)
    if count_of_candies < max_count:
        output = int(input(f'Введите число от 1 до {count_of_candies}\n'))
        if output > count_of_candies:
            get_candy_num_pers(count_of_candies, max_count)
    return output


def candy_play(count_of_candies, max_count):
    first_moved_player = first_move()
    move_num = 0
    while count_of_candies > 0:
        player = who_goes_now(first_moved_player, move_num)
        count_of_candies -= get_candy_num_pers(count_of_candies, max_count)
        move_num += 1
        print(count_of_candies)
    if player == 1:
        return 'Выиграл второй игрок!'
    return 'Выиграл первый игрок!'


print(candy_play(221, 28))
