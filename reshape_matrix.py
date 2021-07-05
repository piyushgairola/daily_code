"""
Date: 05/07/2021
Problem: 566. Reshape the Matrix [https://leetcode.com/problems/reshape-the-matrix/]
"""

def matrixReshape(mat,r,c):
    _r,_c = len(mat), len(mat[0])

    if _r*_c != r*c:
        return mat

    _mat = [[0]*c for _ in range(r)]
    count = 0

    for i in range(_r):
        for j in range(_c):
            _mat[count//c][count%c] = mat[i][j]
            count += 1

    return _mat