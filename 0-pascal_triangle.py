#!/usr/bin/python3
"""Pascal's Triangle Implementation"""


def pascal_triangle(n):
    """
    Returns a list of lists representing
    Pascal's triangle up to the nth level.
    """
    if n <= 0:
        return []

    triangle = [0] * n

    for i in range(n):
        # Initialize the current row with 1s at both ends
        current_row = [0] * (i + 1)
        current_row[0] = 1
        current_row[-1] = 1

        for j in range(1, i):
            if 0 < j < len(current_row):
                left_parent = triangle[i - 1][j - 1]
                right_parent = triangle[i - 1][j]
                current_row[j] = left_parent + right_parent

        triangle[i] = current_row

    return triangle
