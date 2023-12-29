import random
from tabulate import tabulate


def place_ships(board, ships):
    for ship in ships:
        placed = False
        while not placed:
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board) - 1)
            orientation = random.choice(['horizontal', 'vertical'])
            if can_place_ship(board, x, y, orientation, ship) and not is_adjacent(board, x, y, orientation, ship):
                place_ship(board, x, y, orientation, ship)
                placed = True

def is_adjacent(board, x, y, orientation, ship):
    if orientation == 'horizontal':
        for i in range(ship):
            for j in range(-1, ship+1):
                if x + i >= 0 and x + i < len(board) and y + j >= 0 and y + j < len(board[0]) and board[x + i][y + j] != 0:
                    return True
    else:
        for i in range(ship):
            for j in range(-1, ship+1):
                if y + i >= 0 and y + i < len(board[0]) and x + j >= 0 and x + j < len(board) and board[x + j][y + i] != 0:
                    return True
    # Check if the cell above, below, and diagonally adjacent to the ship are also free
    for i in range(-1, ship+1):
        for j in range(-1, ship+1):
            if x + i >= 0 and x + i < len(board) and y + j >= 0 and y + j < len(board[0]) and board[x + i][y + j] != 0:
                return True
    return False


def can_place_ship(board, x, y, orientation, ship):
    if orientation == 'horizontal':
        for i in range(ship):
            if x + i >= len(board) or board[x + i][y] != 0:
                return False
    else:
        for i in range(ship):
            if y + i >= len(board) or board[x][y + i] != 0:
                return False
    return True


def place_ship(board, x, y, orientation, ship):
    if orientation == 'horizontal':
        for i in range(ship):
            board[x + i][y] = ship
    else:
        for i in range(ship):
            board[x][y + i] = ship
    return board

