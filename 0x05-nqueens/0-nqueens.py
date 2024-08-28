#!/usr/bin/python3
'''N Queens Challenge'''

import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    queens_positions = []
    stop_search = False
    row = 0
    column = 0


    while row < n:
        go_back = False
        while column < n:
            
            is_safe = True
            for coord in queens_positions:
                col = coord[1]
                if(col == column or col + (row - coord[0]) == column or
                        col - (row - coord[0]) == column):
                    is_safe = False
                    break

            if not is_safe:
                if column == n - 1:
                    go_back = True
                    break
                column += 1
                continue


            coords = [row, column]
            queens_positions.append(coords)
            if row == n - 1:
                solutions.append(queens_positions[:])
                for coord in queens_positions:
                    if coord[1] < n - 1:
                        row = coord[0]
                        column = coord[1]
                for i in range(n - row):
                    queens_positions.pop()
                if row == n - 1 and column == n - 1:
                    queens_positions = []
                    stop_search = True
                row -= 1
                column += 1
            else:
                column = 0
            break
        if stop_search:
            break
        if go_back:
            row -= 1
            while row >= 0:
                column = queens_positions[row][1] + 1
                del queens_positions[row]
                if column < n:
                    break
                row -= 1
            if row < 0:
                break
            continue
        row += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
