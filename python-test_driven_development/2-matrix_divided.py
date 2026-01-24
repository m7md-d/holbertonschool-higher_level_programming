#!/usr/bin/python3
"""
This module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number

    Args:
        matrix (list): A list of lists of integers or floats
        div (int/float): The number to divide by

    Returns:
        list: A new matrix representing the result of the division

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If each row of the matrix does not have the same size
        TypeError: If div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    """

    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(matrix_err)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(matrix_err)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(matrix_err)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
