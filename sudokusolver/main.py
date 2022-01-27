import math
import os
import time


class Cell:
    def __init__(self, r, c, val):
        self.r = r
        self.c = c
        self.val = val
        self.pot_vals = []



def get_block(board, r, c): # output: list2D
    left_corner = (r - r % 3, c - c % 3)
    block = []

    for r in range(left_corner[0], left_corner[0] + 3):
        block_row = []
        for c in range(left_corner[1], left_corner[1] + 3):
            block_row += [board[r][c]]
        block += [block_row]

    return block


def get_row(board, r): # output: list, 0-index
    return board[r]


def get_col(board, c): # output: list
    return [board[i][c] for i in range(len(board))]


def read_input():
    pass


def print_msg():
    pass

def main():
    """
    TODO: check user input length, only containing numbers.

    board = [['8', '2', '0', '0', '0', '0', '9', '4', '0'],
              ['0', '0', '0', '0', '0', '6', '1', '0', '8'],
              ['1', '0', '0', '0', '8', '0', '0', '0', '0'],
              ['9', '0', '8', '6', '7', '0', '3', '0', '1'],
              ['0', '0', '0', '0', '3', '0', '0', '0', '9'],
              ['0', '3', '1', '5', '0', '9', '0', '8', '0'],
              ['4', '9', '2', '7', '6', '3', '8', '1', '5'],
              ['3', '8', '7', '4', '1', '5', '0', '9', '0'],
              ['0', '1', '0', '0', '0', '0', '7', '3', '4']]


    board = [['0', '0', '3', '0', '0', '6', '4', '2', '0'],
             ['2', '5', '0', '7', '0', '0', '6', '8', '0'],
             ['0', '0', '0', '2', '3', '0', '9', '0', '0'],
             ['1', '0', '0', '4', '7', '3', '5', '0', '0'],
             ['4', '0', '9', '5', '0', '0', '1', '3', '2'],
             ['0', '0', '0', '9', '2', '1', '0', '0', '0'],
             ['3', '4', '5', '0', '9', '0', '8', '7', '0'],
             ['7', '0', '6', '1', '8', '0', '0', '0', '9'],
             ['0', '9', '0', '0', '0', '0', '0', '0', '0']]

    board = [['7', '0', '0', '0', '0', '0', '4', '0', '0'],
         ['0', '0', '8', '9', '0', '5', '0', '2', '0'],
         ['0', '0', '0', '0', '3', '0', '0', '0', '0'],
         ['0', '0', '3', '0', '2', '0', '0', '0', '0'],
         ['8', '0', '0', '6', '0', '3', '0', '0', '7'],
         ['0', '0', '0', '0', '1', '0', '0', '6', '0'],
         ['0', '0', '5', '8', '0', '6', '0', '9', '0'],
         ['0', '0', '0', '1', '0', '0', '0', '0', '0'],
         ['0', '9', '0', '0', '0', '0', '0', '0', '2']]
    """
    print("Please enter the sudoku board here. ")
    print("Format should be '123456789' without the ''.")
    print("If cell is unknown, write 0.")
    print("Do this for every row.")

    board = []
    for i in range(9): # collect 9 rows
        usr_row = input(f"Enter row {i}: ")
        usr_list = [x for x in usr_row]
        board += [usr_list]
    print(board)

    cell_board = []
    for i in range(9):
        cell_row = []
        for j in range(9):
            c = Cell(i, j, board[i][j])
            cell_row += [c]
        cell_board += [cell_row]
    """
    when to check pot_vals:
    * when going through 1-9 in a cell
    * when val is updated in a cell
        * then remove val from pot_vals in every cell in that row, column and block
    """
    game_running = True
    while game_running: # check board and alter pot_vals. if len(potvals) == 1 --> set val.
        game_running = False
        for r in range(9):
            for c in range(9):
                for v in range(1, 10): # check values from 1 to 9
                    if str(v) not in get_row(board, r) \
                            and str(v) not in get_col(board, c) \
                            and str(v) not in sum(get_block(board, r, c), []) \
                            and str(v) not in cell_board[r][c].pot_vals\
                            and board[r][c] == '0':
                        cell_board[r][c].pot_vals += [str(v)]

        for r in range(9):
            for c in range(9):
                print(cell_board[r][c].pot_vals)

                if len(cell_board[r][c].pot_vals) == 1 and board[r][c] == '0':
                    # game_running = True # run until no changes has been made
                    # set value for this cell and remove it from other pot_vals
                    prev = cell_board[r][c].val
                    cell_board[r][c].val = cell_board[r][c].pot_vals[0]
                    board[r][c] = cell_board[r][c].pot_vals[0]
                    cell_board[r][c].pot_vals = []
                    print(f"Changed board({r}, {c}) from {prev} to {board[r][c]}")
                    for cell in get_row(cell_board, r):
                        if cell_board[r][c].val in cell.pot_vals:
                            cell.pot_vals.remove(cell_board[r][c].val)
                    for cell in get_col(cell_board, c):
                        if cell_board[r][c].val in cell.pot_vals:
                            cell.pot_vals.remove(cell_board[r][c].val)
                    for cell in sum(get_block(cell_board, r, c), []):
                        if cell_board[r][c].val in cell.pot_vals:
                            cell.pot_vals.remove(cell_board[r][c].val)
            print("----------")
                
        for r in range(9):
            for c in range(9):
                if board[r][c] == '0':
                    game_running = True
        for i in range(9):
            print(board[i])

    for i in range(9):
        print(board[i])
    print("done")


main()
