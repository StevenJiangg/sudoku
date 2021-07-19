import random
import math
import numpy as np
from typing import List
import time
import copy
start_time = time.time()

# testing matrices 
A = [[1, 0, 5, 0, 7, 0, 0, 0, 6],
     [0, 7, 0, 2, 8, 0, 0, 0, 0],
     [0, 0, 6, 0, 9, 5, 7, 0, 0],
     [8, 6, 0, 0, 5, 0, 0, 0, 0],
     [9, 0, 2, 0, 4, 0, 0, 6, 1],
     [7, 4, 3, 0, 0, 0, 9, 0, 0],
     [4, 3, 0, 6, 0, 9, 5, 0, 0],
     [0, 0, 0, 0, 2, 7, 4, 0, 0],
     [0, 0, 0, 4, 3, 0, 0, 0, 7]]
 
B = [[1, 9, 5, 3, 7, 4, 2, 8, 6], 
    [3, 7, 4, 2, 8, 6, 1, 9, 5], 
    [2, 8, 6, 1, 9, 5, 7, 4, 3], 
    [8, 6, 1, 9, 5, 2, 3, 7, 4], 
    [9, 5, 2, 7, 4, 3, 8, 6, 1], 
    [7, 4, 3, 8, 6, 1, 9, 5, 2], 
    [4, 3, 7, 6, 1, 9, 5, 2, 8], 
    [6, 1, 8, 5, 2, 7, 4, 3, 9], 
    [5, 2, 9, 4, 3, 8, 6, 1, 7]] 
C = [[0 for x in range(9)] for y in range(9)]
# constraints: 
# row, column, 3x3 grid 

# return true if the value we want to input has no other conflicting values in the same row 
def checkRow(matrix, i, val):
    for col in range(9):
        if matrix[i][col] == val:
            return False
    return True
    
# return true if the value we want to input has no other conflicting values in the same column 
def checkCol(matrix, j, val):
    for row in range(9):
        if matrix[row][j] == val:
            return False
    return True
    
def sqMap(i, j):
    lowerBoundi, upperBoundi, lowerBoundj, upperBoundj = 0, 0, 0, 0
    if i >= 0 and i <= 2:
        lowerBoundi = 0
        upperBoundi = 3
    if i >= 3 and i <= 5:
        lowerBoundi = 3
        upperBoundi = 6
    if i >= 6 and i <= 8:
        lowerBoundi = 6
        upperBoundi = 9    
    if j >= 0 and j <= 2:
        lowerBoundj = 0
        upperBoundj = 3
    if j >= 3 and j <= 5:
        lowerBoundj = 3
        upperBoundj = 6
    if j >= 6 and j <= 8:
        lowerBoundj = 6
        upperBoundj = 9 
    return lowerBoundi, upperBoundi, lowerBoundj, upperBoundj
    
# return true if the value we want to input has no other conflicting values in the same 3x3 grid         
def checkBox(matrix, i, j, val):
    lowerBoundi, upperBoundi, lowerBoundj, upperBoundj = sqMap(i, j)
    for i in range(lowerBoundi, upperBoundi):
        for j in range(lowerBoundj, upperBoundj):
            if matrix[i][j] == val:
                return False
    return True
 
# return true if the current value is not conflicting with other values in same row, col or box 
def isValid(matrix, i, j, val):
    if checkRow(matrix, i, val) and checkCol(matrix, j, val) and checkBox(matrix, i, j, val):
        return True
    return False


# now that we have all the constraints listed out and put into code, next step is to combine them together
# and then check each square to see what we can input
checkArr = []   
def solveSudoku(matrix, i, j):
    if i == 8 and j == 9: 
        currentMatrix = copy.deepcopy(matrix)
        checkArr.append(currentMatrix)
        i = 0
        j = 0
        return True
    # if there exists more than 1 unique solution then we stop and return false
    if len(checkArr) >= 2:
        return False
    if j == 9:
        i += 1
        j = 0
    if matrix[i][j] > 0:
        return solveSudoku(matrix, i, j+1)
    # check each value (1-9) for each square, inputing it and moving to the next square if its a possible value
    for val in range(1, 10):
        if isValid(matrix, i, j, val):
            matrix[i][j] = val
            solveSudoku(matrix, i, j + 1)
        matrix[i][j] = 0
    return False


# makes sure that the sudoku puzzle we generate will be unique,
# returns a sudoku puzzle that only has 1 solution
def deleteValue(matrix):
    temp, iholder, jholder = 0,0,0
    tempMatrix = list(matrix)
    solveSudoku(tempMatrix, 0, 0)
    while len(checkArr) == 1:
        checkArr.pop()
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if tempMatrix[i][j] != 0:
            temp = tempMatrix[i][j]
            iholder = i
            jholder = j
            matrix[i][j] = 0
        solveSudoku(tempMatrix, 0, 0)
    
    tempMatrix[iholder][jholder] = temp
    
    return np.asmatrix(tempMatrix)



    
    