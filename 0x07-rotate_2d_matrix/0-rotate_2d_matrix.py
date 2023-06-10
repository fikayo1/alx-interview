#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a matrix 90 degrees clockwise
    """
    rotatedmat = []
    revList = []
    for m in range(len(matrix[0])):
        for i in matrix:
            rotatedmat.append(i[m])
        rotatedmat.reverse()
        revList.append(rotatedmat)
        rotatedmat = []
    print(rotatedmat)
