from random import randint, seed
from pprint import pprint

seed(208)

def random_state(width=3, height=3):
    board = []
    for _ in range(width):
        board.append([randint(0, 1) for _ in range(height)])
    return board

def display(board):
    alive = '🙂 '
    dead = '💀 '
    for row in board:
        for cell in row:
            print('* ' if cell == 1 else '. ', end='')
            # print(alive if cell == 1 else dead, end='')
        print('\n')

def next_state(board):
    pass

if __name__ == '__main__':
    # print(random_state(5, 5))
    board = random_state(2, 3)
    print(board)
    display(board)
