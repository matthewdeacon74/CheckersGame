import checkers

def game():
    valid_board = False
    board_size = 0
    while valid_board == False:
        board_size = int(input(f"Create a board of how many squares per side (4-16)? "))
        if 3 < board_size < 17:
            valid_board = True
            game_board = checkers.build_board(board_size)
            print(f"The board has {checkers.get_count(game_board, 'empty')} empty spaces")
            print(f"The board has {checkers.get_count(game_board, 'red')} red spaces")
            print(f"The board has {checkers.get_count(game_board, 'black')} black spaces")
            checkers.do_swap(game_board)
        else:
            print("Not a valid size.  4 through 16 only, please.")


# run game only if this file is running as main
if __name__ == '__main__':
    game()
