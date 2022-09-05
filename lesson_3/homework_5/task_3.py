# Создайте программу для игры в ""Крестики-нолики"".

from random import randint


def tic_player():
    return randint(0, 1)


def who_goes_now(move_num):
    return move_num % 2


def print_board(list_of_moves, num):
    board = [[], [], [], [], [], [], [], [], []]
    for j in range(0, 9):
        for i in range(0, 17):
            if (i + 1) % 6 == 0:
                board[j].append('|')
            elif (j + 1) % 3 == 0 and j != 8:
                board[j].append('_')

            elif (i + 4) % 6 == 0 and (j + 2) % 3 == 0:
                count = 1
                for a in range(num):
                    if list_of_moves[a][0] * 6 - 4 == i and list_of_moves[a][1] * 3 - 2 == j:
                        if list_of_moves[a][2] == 0:
                            board[j].append('X')
                        else:
                            board[j].append('0')
                        count = 0
                if count:
                    board[j].append(' ')
            else:
                board[j].append(' ')
    for row in board:
        for elem in row:
            print(elem, end='')
        print()
    return board


def tic_tac_toe():
    tic = tic_player()
    if tic == 0:
        print('Первый игрок - "крестики",\nвторой игрок - "нолики"')
    else:
        print('Второй игрок - "крестики",\nпервый игрок - "нолики"')

    num = 0
    list_of_moves = []
    winner = -1
    while winner == -1:
        player = who_goes_now(num)
        list_of_moves = do_your_move(player, list_of_moves)
        num += 1

        board = print_board(list_of_moves, num)
        winner = handle_move(board, num, player)
    if winner == 0:
        return ('Крестики победили!')
    elif winner == 1:
        return ('Нолики победили!')
    else:
        return ('Ничья!')


def do_your_move(player, list_of_moves):
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбца: '))
    verification(row, column, player, list_of_moves)
    return list_of_moves


def verification(row, column, player, list_of_moves):
    count = 1
    for move in list_of_moves:
        if move[1] == row and move[0] == column:
            print('Поле занято!')
            do_your_move(player, list_of_moves)
            count = 0

    if row > 3 or row < 1 or column > 3 or column < 1:
        print('Поле не существует!')
        do_your_move(player, list_of_moves)
        count = 0
    if count:
        list_of_moves.append([column, row, player])
    return list_of_moves


def handle_move(board, num, player):
    if num >= 5:
        if board[1][2] == board[4][8] == board[7][14]:
            return player

        if board[7][2] == board[4][8] == board[1][14]:
            return player

        for i in range(1, 4):
            if board[i * 3 - 2][2] == board[i * 3 - 2][8] == board[i * 3 - 2][14]:
                return player

        for j in range(1, 4):
            if board[1][j * 6 - 4] == board[4][j * 6 - 4] == board[7][j * 6 - 4]:
                return player
    if num == 9:
        return 2

    return -1


print(tic_tac_toe())
