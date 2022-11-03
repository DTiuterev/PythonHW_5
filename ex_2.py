#2. Создайте программу для игры в ""Крестики-нолики"".
print('Уважаемые игроки в крестики-нолики! Определите жребием, кто начинает и будет ставить Х, а кто играет вторым и ставит О.')
print('Игровое поле представляет собой квадрат из 9 пронумерованных клеточек.')
print('Чтобы сделать ход, игрок вводит номер клеточки, в который хочет поставить свой знак Х или 0.')
print('Победит игрок, который сможет первым поставить три своих символа подряд по горизонтали, вертикали или диагонали.')

board = list(range(1, 10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)

def take_input(moves):
    valid = False
    while not valid:
        player_move = input("Игрок " + moves + ", введите номер клеточки, в которую Вы ставите свой знак: ")
        try:
            player_move = int(player_move)
        except:
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue
        if player_move >= 1 and player_move <= 9:
            if (str(board[player_move-1]) not in "XO"):
                board[player_move-1] = moves
                valid = True
            else:
                print("Эта клеточка уже занята. Сделайте другой ход.")
        else:
            print("Некорректный ввод. Введите число от 1 до 9, чтобы сделать ход.")

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print('Игрок '+tmp, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ходов больше не осталось. Ничья!')
            break
    draw_board(board)

main(board)