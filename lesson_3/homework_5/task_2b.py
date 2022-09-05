# b) Игра против бота с "интеллектом"

from random import randint


def first_move():
    return randint(0, 1)


def who_goes_now(player_started, move_num):
    return (player_started + move_num) % 2


def get_candy_num_bot(count_of_candies, max_count):
    if count_of_candies <= max_count * 2 + 1 and count_of_candies > max_count + 1:
        return count_of_candies - max_count - 1
    if count_of_candies <= max_count:
        return count_of_candies
    if count_of_candies > max_count * 2 + 1:
        return randint(1, max_count)


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
        if player == 0:
            count_of_candies -= get_candy_num_bot(count_of_candies, max_count)
        else:
            count_of_candies -= get_candy_num_pers(count_of_candies, max_count)
        print(count_of_candies)
        move_num += 1
    if player == 1:
        return 'Вы выиграли!'
    return 'Вы проиграли!'


print(candy_play(21, 4))
