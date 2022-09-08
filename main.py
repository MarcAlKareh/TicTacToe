board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

player = 'X'
turns = 0

def draw_board(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def check_rows(player):
    return (board[0] == player and board[1] == player and board[2] == player) or (
                board[3] == player and board[4] == player and board[5] == player) or (
                       board[6] == player and board[7] == player and board[8] == player)


def check_cols(player):
    return (board[0] == player and board[3] == player and board[6] == player) or (
                board[1] == player and board[4] == player and board[7] == player) or (
                       board[2] == player and board[5] == player and board[8] == player)


def check_diagonals(player):
    return (board[0] == player and board[4] == player and board[8] == player) or (
                board[2] == player and board[4] == player and board[6] == player)


def check_win():
    # Check rows for X
    if check_rows('X'):
        return 'X'

    # Check columns for X
    if check_cols('X'):
        return 'X'

    # Check diagonals for X
    if (check_diagonals('X')):
        return 'X'

    # Check rows for O
    if check_rows('O'):
        return 'O'

    # Check columns for O
    if check_cols('O'):
        return 'O'

    # Check diagonals for O
    if (check_diagonals('O')):
        return 'O'

    return None


def main():
    global player
    global turns

    draw_board(board)

    win_status = check_win()
    if win_status == 'X':
        print('X won!')
        return
    elif win_status == 'O':
        print('O won!')
        return

    try:
        board_pos = int(input(f"{player}'s turn, Enter a number from 1 - 9: "))

        # Check if input is valid
        if board_pos < 1 or board_pos > 9:
            print('Input has to be a number from 1 - 9, try again.')
            main()

        board_index = board_pos - 1
        board[board_index] = player

        if turns == 9:
            return

        turns += 1

        if player == 'X':
            player = 'O'
        elif player == 'O':
            player = 'X'

        main()
    except ValueError:
        print('Input has to be a number from 1 - 9, try again.')
        main()
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()
