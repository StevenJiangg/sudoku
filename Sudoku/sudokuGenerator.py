import random
import math
import numpy as np
from random import randrange
import sudokuSolver as ss
import copy

# file creates a generic matrix and shuffles it to erase patterns 

sudokuList = []
sudokuAns = []
C = [[0 for x in range(9)] for y in range(9)]

def randomShuffle(partHolder1, partHolder2, partHolder3): 
    randVal = random.randint(1, 5)
    if randVal == 1: 
        matrix = np.concatenate((partHolder1, partHolder3), axis = 0)
        matrix = np.concatenate((matrix, partHolder2), axis = 0)
        return matrix
    if randVal == 2: 
        matrix = np.concatenate((partHolder3, partHolder2), axis = 0)
        matrix = np.concatenate((matrix, partHolder1), axis = 0)
        return matrix
    if randVal == 3: 
        matrix = np.concatenate((partHolder2, partHolder3), axis = 0)
        matrix = np.concatenate((matrix, partHolder1), axis = 0)
        return matrix
    if randVal == 4: 
        matrix = np.concatenate((partHolder3, partHolder1), axis = 0)
        matrix = np.concatenate((matrix, partHolder2), axis = 0)
        return matrix
    if randVal == 5: 
        matrix = np.concatenate((partHolder2, partHolder1), axis = 0)
        matrix = np.concatenate((matrix, partHolder3), axis = 0)
        return matrix

def shuffleSudokuRow(m):
    partHolder1 = np.zeros(81, dtype = int).reshape((9, 9))
    partHolder2 = np.zeros(81, dtype = int).reshape((9, 9))
    partHolder3 = np.zeros(81, dtype = int).reshape((9, 9))
    i = 0
    while i < 9:
        for j in range(9):
            if i >= 0 and i < 3: 
                partHolder1[i][j] = m[i][j]
            if i >= 3 and i < 6:
                partHolder2[i][j] = m[i][j]
            if i >= 6 and i < 9:
                partHolder3[i][j] = m[i][j] 
        i += 1
        
    partHolder1 = partHolder1[partHolder1 != 0].reshape(3, 9)
    np.random.shuffle(partHolder1)
    partHolder2 = partHolder2[partHolder2 != 0].reshape(3, 9)
    np.random.shuffle(partHolder2)
    partHolder3 = partHolder3[partHolder3 != 0].reshape(3, 9)
    np.random.shuffle(partHolder3)
    matrix = randomShuffle(partHolder1, partHolder2, partHolder3)
    return matrix
    
def shuffleSudokuCol(m):
    partHolder1 = np.zeros(81, dtype = int).reshape((9, 9))
    partHolder2 = np.zeros(81, dtype = int).reshape((9, 9))
    partHolder3 = np.zeros(81, dtype = int).reshape((9, 9))
   
    i = 0
    while i < 9:
        for j in range(9):
            if j >= 0 and j < 3: 
                partHolder1[j][i] = m[i][j]
            if j >= 3 and j < 6:
                partHolder2[j][i] = m[i][j]
            if j >= 6 and j < 9:
                partHolder3[j][i] = m[i][j] 
        i += 1
    
    partHolder1 = partHolder1[partHolder1 != 0].reshape(3, 9)
    np.random.shuffle(partHolder1)
    partHolder2 = partHolder2[partHolder2 != 0].reshape(3, 9)
    np.random.shuffle(partHolder2)
    partHolder3 = partHolder3[partHolder3 != 0].reshape(3, 9)
    np.random.shuffle(partHolder3)
    matrix = randomShuffle(partHolder1, partHolder2, partHolder3).transpose()
    return matrix   


def generateMatrix():
    value = 0
    lst = [1,2,3,4,5,6,7,8,9]
    random.shuffle(lst)
    #print(lst)
    temp = lst
    
    matrix = [[0 for x in range(9)] for y in range(9)] 

    j = 0
    for i in range(9):
        if(j > 9):
            j = j % 9
        if i == 2 or i == 5:
            matrix[i] = lst[j:] + lst[0:j]
            j = j + 1
        else:
            matrix[i] = lst[j:] + lst[0:j]
            j = j + 3
            
    m = np.asmatrix(matrix)
    #m = np.rot90(m)
    m = m.tolist()
    matrix = shuffleSudokuCol(matrix)
    matrix = shuffleSudokuRow(matrix)
    sudokuList.append(matrix)
    return matrix 
    

def removeValues(matrix):
    return ss.deleteValue(matrix)

def checkChange(matrix: np.matrix):
    boolMat = np.zeros(81, dtype = int).reshape((9, 9)) 
    for i in range(9): 
        for j in range(9):
            if matrix[i, j] != 0: 
                boolMat[i, j] = 1
    return boolMat

#generateMatrix()