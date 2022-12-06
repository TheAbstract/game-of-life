from random import randint, seed
from pprint import pprint

seed(208)

def dead_state(width=3, height=3):
    board = []
    for _ in range(width):
        board.append([0 for _ in range(height)])
    return board

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

def next_cell(point, board):
    ALIVE, DEAD = 1, 0
    i, j = point
    width = len(board)
    height = len(board[0])

    neighbors = 0
    for ith in range((i - 1), (i + 1) + 1):
        if ith < 0 or ith >= width:
            continue
        for jth in range((j - 1), (j + 1) + 1):
            if i == ith and j == jth:
                continue
            if jth < 0 or jth >= height:
                continue
            if board[ith][jth] == ALIVE:
                neighbors += 1

        if board[ith][jth] == ALIVE:
            if neighbors <= 1:
                return DEAD
            elif neighbors <= 3:
                return ALIVE
            else:
                return DEAD
        else:
            if neighbors == 3:
                return ALIVE
            else:
                return DEAD

def next_state(board):
    width = len(board)
    height = len(board[0])
    state = dead_state(board)

    for i in range(width):
        for j in range(height):
            state[i][j] = next_cell((i, j), board)

    return state

if __name__ == '__main__':
    pprint(dead_state())
    board = random_state(5, 5)
    pprint(board)
