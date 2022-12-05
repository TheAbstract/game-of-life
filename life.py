from random import randint, seed
from pprint import pprint

seed(208)

def random_state(width=3, height=3):
    board = []
    for _ in range(width):
        board.append([randint(0, 1) for _ in range(height)])
    return board

def display(board):
    for row in board:
        for cell in row:
            print('* ' if cell == 1 else '. ', end='')
    
        print('\n')


if __name__ == '__main__':
    board = random_state(2, 3)
    print(board)
    display(board)
