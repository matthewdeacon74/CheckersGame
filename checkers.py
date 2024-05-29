from numpy import random
from numpy import swapaxes


def build_board(size:int):
    board = random.choice(['empty', 'red', 'black'], (size, size))
    print('')
    print("Initial board layout:")
    print(board)
    return board


def get_count(current_board, square_state:str):
    new_count = current_board == square_state
    return new_count.sum()


def do_swap(array):
    print('')
    print("Board layout with swapped axes:")
    new_array = swapaxes(array, 0, 1)
    print(new_array)


if __name__ == '__main__':
    print("checkers.py is not meant to run as main script.  Please run main.py instead.")