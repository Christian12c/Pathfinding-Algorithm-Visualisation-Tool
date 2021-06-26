#Importing modules, procedures and constants that are referenced in this file
import pygame
import sys
from pygame_Setup import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, createVisualGrid

class Dropdown():
    def __init__(self, rectangle, color, text, screen):
        self.__rectangle = rectangle
        self.__color = color
        self.__screen = screen
        self.__text = text
        self.__array = [text]
        self.__isDropdownDown = False

    #Adds an option to a dropdown
    def addButton(self, text): 
        self.__array.append(text)

    #Changes the name of
    def changeMain(self, i): 
        self.__array[0] = self.__array[i]

    #Adds an option to a dropdown
    def returnMain(self):
        return self.__array[0]
    
    #Clears the algorithms from dropdown
    def clearMain(self): 
        self.__array[0] = self.__text

    #Returns if the dropdown is opened or closed
    def getIsDropdownDown(self): 
        return self.__isDropdownDown

    #Draws the dropdown in either state, open or closed
    def drawDropdown(self, fullList=False):
        if fullList == True:
            n = len(self.__array)
            self.__isDropdownDown = True
        else:
            n = 1
            self.__isDropdownDown = False
        for i in range(n):
            font = pygame.font.Font('freesansbold.ttf', 15) 
            writing = font.render(self.__array[i], True, (0,0,0), self.__color)
            textRect = writing.get_rect()  
            textRect.center = (self.__rectangle[2]/2, self.__rectangle[3]/2 + i*self.__rectangle[3])

            newRectangle = (self.__rectangle[0], self.__rectangle[1]+i*self.__rectangle[3], self.__rectangle[2], self.__rectangle[3])
            pygame.draw.rect(self.__screen, self.__color, newRectangle)
            self.__screen.blit(writing, textRect)
        for i in range(n):
            pygame.draw.line(self.__screen, (0,0,0), (self.__rectangle[0], self.__rectangle[3]*(i+1)), (self.__rectangle[2], self.__rectangle[3] + self.__rectangle[3]*i))
                    
    #Updates the dropdown when clicking on the dropdown   
    def update(self, grid):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x <= self.__rectangle[0]+self.__rectangle[2] and x >= self.__rectangle[0] and y <= self.__rectangle[1]+self.__rectangle[3] and y >= self.__rectangle[1] and self.__isDropdownDown == False:
                    self.drawDropdown(fullList=True)
                elif x <= self.__rectangle[0]+self.__rectangle[2] and x >= self.__rectangle[0] and y <= self.__rectangle[1]+self.__rectangle[3] and y >= self.__rectangle[1] and self.__isDropdownDown == True:
                    self.__screen.fill((0,0,0))
                    createVisualGrid(grid)
                    self.drawDropdown(fullList=False)
                elif x <= self.__rectangle[0]+self.__rectangle[2] and x >= self.__rectangle[0] and y < self.__rectangle[1]+len(self.__array)*self.__rectangle[3] and y >= self.__rectangle[1] and self.__isDropdownDown == True:               
                    self.changeMain(int(y//self.__rectangle[3]))
                    self.drawDropdown(fullList=True)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.clearMain()
                    if self.__isDropdownDown == False:
                        self.drawDropdown(fullList=True)
                    else:
                        self.drawDropdown(fullList=True)
