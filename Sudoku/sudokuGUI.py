import pygame, sys
from pygame.locals import *
import random
from sudokuGenerator import *
import numpy as np
import copy

# next to implement: single arrays of size 81, more interactive UI (pop up/movement showing that the player has won)
# , highlighting boxes to show errors in player solution, making input available on: the numpad of the keyboard,
# or on the UI, multiple difficulty levels 

pygame.init()

clock = pygame.time.Clock()

# array for mapping each pygame value to its keyboard part
pyNum = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9] 

# declaring colors 
color_passive = pygame.Color('lightskyblue3')
color1 = color_passive
color2 = color_passive
boxColor = (0, 0, 0)
select_color = (70, 135, 70)

# display screen and set background to white
screen = pygame.display.set_mode([800, 800])
screen.fill((255, 255, 255))

# setting the font used for pygame UI
base_font = pygame.font.Font(None, 32)
button_font = pygame.font.SysFont('Arial', 12)

# initializing matrices to store values for rendering 
w, h = 9, 9;
matrix = [[0 for x in range(w)] for y in range(h)] 
activeArr = [[0 for x in range(w)] for y in range(h)]
user_text = [[0 for x in range(w)] for y in range(h)]
user_text2 = [[0 for x in range(w)] for y in range(h)]
color = [[0 for x in range(w)] for y in range(h)]
text_surface2 = [[0 for x in range(w)] for y in range(h)] 
solutionMatrix = [[0 for x in range(w)] for y in range(h)] 

submit_button = pygame.Rect(( (510 ), (500)), (50, 30))

# generate a sudoku puzzle and its solution from the sudokuGenerator file
generateMatrix()

tempAnsMatrix = sudokuList[0]

storage = copy.deepcopy(tempAnsMatrix)

gMatrix = removeValues(tempAnsMatrix)

unchange = checkChange(gMatrix)

# setting up the sudoku puzzle/creating values to be displayed 
for i in range(9):
    for j in range(9):
        turn_unicode = str(gMatrix[i,j]).encode("utf-8").decode("utf-8") 
        user_text2[i][j] = turn_unicode
        
        matrix[i][j] = pygame.Rect( (200 + (20*(i*2)), (100 + 20*(j*2))), (32, 35))
        
        text_surface2[i][j] = base_font.render(user_text2[i][j], True, (0, 0, 0))
        screen.blit(text_surface2[i][j], (matrix[i][j].x+6, matrix[i][j].y+6))
        
        color[i][j] = color_passive
        activeArr[i][j] = 0
        user_text[i][j] = ''
    
# solution matrix to keep track of the user input and comparing it to the solution
for i in range(9):
    for j in range(9):
        solutionMatrix[i][j] = gMatrix[i,j]

def inputSolution(num, i ,j): 
    realNum = [1,2,3,4,5,6,7,8,9]
    val = pyNum.index(num)
    solutionMatrix[i][j] = realNum[val]
    
# checks whether the player has won the game or not 
def checkSolution():
    count = 0
    print(storage.transpose())
    listtypeMat = np.asmatrix(solutionMatrix).transpose()
    print(listtypeMat.tolist())
    for i in range(9):
        for j in range(9):
            if solutionMatrix[i][j] == storage[i,j]:
                count = count + 1
    if count >= 81:
        print("you won")

# draws the sudoku boxes and its components
def drawBoxes():
    cordHorizontal = 196
    cordVertical = 97
    pygame.draw.rect(screen, boxColor, pygame.Rect(cordHorizontal, cordVertical, 360, 360),  2)
    pygame.draw.rect(screen, boxColor, pygame.Rect(cordHorizontal-1, cordVertical+1, 360, 360),  2)
    pygame.draw.rect(screen, boxColor, pygame.Rect(cordHorizontal+1, cordVertical-1, 360, 360),  2)

    for i in range(1, 4):
        for j in range(1, 4):
            pygame.draw.rect(screen, boxColor, pygame.Rect(cordHorizontal, cordVertical, 360*(i/3), 360*(j/3)),  2)
    
# While the game is running, the program renders boxes and values and makes it possible for values to be changed. 
# It will also check if the player inputed correct solutions if prompt.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(9):
                for j in range(9):
                    if matrix[i][j].collidepoint(event.pos):
                        activeArr[i][j] = 1
                        color[i][j] = select_color
                    else:
                        activeArr[i][j] = 0     
                        color[i][j] = color_passive
                        
        if event.type == pygame.KEYDOWN:
            for i in range(9):
                for j in range(9):
                    if activeArr[i][j] == True:
                        if event.key == pygame.K_BACKSPACE:
                            user_text[i][j] = user_text[i][j][:-1]
                        if event.key: 
                            for num in pyNum :
                                if event.key == num:
                                    inputSolution(num, i, j)
                                    user_text[i][j] += event.unicode
                                    user_text[i][j] = user_text[i][j][:1]
                                    
                        else: 
                            print("action not taken into account")
                            break
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if submit_button.collidepoint(event.pos):
                color2 = select_color
                checkSolution()
            else:  
                color2 = color_passive
        

    text_surface = [[0 for x in range(w)] for y in range(h)] 
    
    for i in range(9):
        for j in range(9):
            if unchange[i, j] == 1:
                pygame.draw.rect(screen, color[i][j], matrix[i][j], 2)
            else: 
                pygame.draw.rect(screen, color[i][j], matrix[i][j])
                pygame.draw.rect(screen, color1, submit_button)
                drawBoxes()
                text_submit = button_font.render("CHECK", True, (0,0,0))
                
                screen.blit(text_submit, (submit_button.x + 3, submit_button.y + 6 ))
                text_surface[i][j] = base_font.render(user_text[i][j], True, (0, 0, 0))
                screen.blit(text_surface[i][j], (matrix[i][j].x+6, matrix[i][j].y+6))
    
    pygame.display.update()
      
    clock.tick(60)
