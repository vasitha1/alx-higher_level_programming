#!/usr/bin/python3

"""
    This is the "2-matrix_divided" module which devides all elements of matrix
"""


def matrix_divided(matrix, div):
    """ matrix_divided function which divides matrix by div"""

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float))
               for row in matrix
               for element in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of int/float")

    if div == 0:
        raise TypeError("division by zero")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    first_len = len(matrix[0])

    for row in matrix:
        if len(row) != first_len:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element/div, 2))
        new_matrix.append(new_row)

    return new_matrix
