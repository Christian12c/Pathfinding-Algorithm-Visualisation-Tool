#Importing modules, procedures and constants that are referenced in this file
import pygame
import sys
from pygame_Setup import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT

class Menu():
    def __init__(self, rectangle, color, text, screen, menuWidth, menuHeight):
        self.__rectangle = rectangle
        self.__color = color
        self.__screen = screen
        self.__text = text
        self.__array = [text]
        self.__menuWidth = menuWidth
        self.__menuHeight = menuHeight

    #Adds an option to a menu
    def addButton(self, text):
        self.__array.append(text)

    #Returns the index of the menu item
    def returnMenuItemIndex(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x >= self.__rectangle[0] and x <= SCREEN_WIDTH and y <= self.__menuHeight and y >= self.__rectangle[1]:
                    return int(x//(SCREEN_WIDTH/self.__menuWidth))

    #Draws the menu
    def drawMenu(self):
        #Iterates through the array and draws the each menu item
        for i in range(len(self.__array)):
            pygame.draw.rect(SCREEN, self.__color, (self.__rectangle[0]*(i+1), self.__rectangle[1], self.__rectangle[2], self.__rectangle[3]))
            pygame.draw.line(SCREEN, (0,0,0), (self.__rectangle[0]*(i+1), 0), (self.__rectangle[0]*(i+1), self.__menuHeight))

            font = pygame.font.Font('freesansbold.ttf', 15)
            writing = font.render(self.__array[i], True, (0,0,0), self.__color)
            textRect = writing.get_rect()  
            textRect.center = (self.__rectangle[0]*(i+1)+ SCREEN_WIDTH/(2*self.__menuWidth),self.__menuHeight/2)
            SCREEN.blit(writing, textRect)
