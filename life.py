from random import randint, seed
from pprint import pprint


seed(208)
ALIVE, DEAD = 1, 0

def random_state(width=5, height=5, dead=False):
    cell = 0 if dead else randint(0, 1)
    board = []
    for _ in range(width):
        board.append([cell for _ in range(height)])
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
            if jth < 0 or jth >= height:
                continue
            if ith == i and jth == j:
                continue
            if board[ith][jth] == ALIVE:
                neighbors += 1

    if board[i][j] == ALIVE:
        if neighbors <= 1:
            return DEAD
        elif neighbors <= 3:
            return ALIVE
        else:
            return DEAD
    else:
        return ALIVE if neighbors == 3 else DEAD

def next_state(board):
    width = len(board)
    height = len(board[0])
    state = dead_state(width, height)

    for i in range(width):
        for j in range(height):
            state[i][j] = next_cell((i, j), board)

    return state

if __name__ == '__main__':
    pprint(random_state(dead=True))
    board = random_state()
    pprint(board)
    pprint(next_state(board))
