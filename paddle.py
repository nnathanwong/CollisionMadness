# Nathan Wong
# 05/14/2024
# Program Description: A class to provide a blueprint to make a paddle object

import pygame
from drawable import Drawable

class Paddle(Drawable):
    '''
    Draws a rectangular "paddle" at the bottom of the display whose position can
    be controlled by the user's mouse movements
    
    Parameters:
        Drawable (base class): Instantiated in constructor
        
    Attributes:
        color (tuple): An RGB tuple that sets the color of the object
        width (int): The width of the paddle
        height (int): The height of the paddle
    
    Methods:
        __init__: Instantiates the Paddle class
        draw: Draws the rectangle object that defines the paddle to the display
        get_rect: Instantiates the rectangle object for the paddle
    '''
    # Constructor
    def __init__(self, width, height, color):
        '''
        Instantiates the base class Drawable as well as Paddle
        
        Parameters:
            self (object): The Paddle object itself
            width (int): The width of the paddle
            height (int): The height of the paddle
            color (tuple): An RGB tuple that sets the color of the object
            
        Return value: None
        
        Sample call: paddle1 = Paddle(1,2,(DREXEL_BLUE))
        '''
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        super().__init__(screenWidth/2, screenHeight/2)
        self.__color = color
        self.__width = width
        self.__height = height
    def draw(self, surface):
        '''
        Draws the paddle object to the surface in the form of a rectangle
        
        Parameters:
            self (object): The Paddle object itself
            surface (object): The display that is to be drawn on
            
        Return value: None
        
        Sample call: paddle1.draw(surface)
        '''
        pygame.draw.rect(surface, self.__color, self.get_rect())
    # Getter
    def get_rect(self):
        '''
        Instantiates a rectangle that covers the area of the paddle. Allows the rectangle/paddle's horizontal position
        to be controlled by the user's mouse movements.
        
        Parameters:
            self (object): The Paddle object itself
            
        Return value: A rectangle object that covers the area of the Paddle, whose position
        is based on the user's mouse's horizontal position
        '''
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        mouseX = pygame.mouse.get_pos()[0]
        return pygame.Rect(mouseX - (self.__width/2), screenHeight - 20 - self.__height, \
                           self.__width, self.__height)
    