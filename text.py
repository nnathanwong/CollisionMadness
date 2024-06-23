# Nathan Wong
# 05/14/2024
# Program Description: To provide a class that displays textual information that can be drawn onto
# a pygame surface

from drawable import Drawable
import pygame

class Text(Drawable):
    '''
    To display textual information on a pygame surface
    
    Parameters:
        Drawable (base class): Instantiated in constructor to receive x and y coordinate information
    
    Attributes:
        message (string): The text to be displayed on the surface
        x (int): The horizontal position at which the text is to be displayed at
        y (int): The vertical position at which the text is to be displayed at
        color (tuple): A three-integer RBG tuple that sets the color of the text
        size (int): The font size of the text
    
    Methods:
        __init__: Instantiates the Text class
        draw: Creates a new surface object that depicts the text and draws it to the original surface object
        get_rect: Instantiates and returns a rectangle object covering the area of the Text object
        setMessage: Changes the text (message attribute) to be displayed
    '''
    # Constructor
    def __init__(self, message="Pygame", x=0, y=0, color=(0,0,0), \
                 size=24):
        '''
        Instantiates the base class Drawable as well as Text based on given arguments
        
        Parameters:
            message (string): The text that the user wants to display
            x (int): The horizontal position at which the user wants the text to be displayed at
            y (int): The vertical position at which the user wants the text to be displayed at
            color (tuple): A three-integer RBG tuple to set the color of the text
            size (int): The font size of the text
            
        Return value: None
        
        Sample call: hello = Text("Hello!", 200, 400, DREXEL_BLUE, 50)
        '''
        super().__init__(x, y)
        self.__message = message
        self.__color = color
        self.__fontObj = pygame.font.Font("freesansbold.ttf", size)
    def draw(self, surface):
        '''
        Creates a new surface object that depicts text and then draws it
        to the original surface object
        
        Parameters:
            self (object): The Text object itself
            surface (object): The original surface object that is currently drawn to the screen
            
        Return value: None
        
        Sample call: text1.draw(surface)
        '''
        # Text's surface object
        self.__surface = self.__fontObj.render(self.__message, \
                                               True, self.__color)
        # Combines text's surface with the base surface object
        surface.blit(self.__surface, self.getLoc())
    # Getter
    def get_rect(self):
        '''
        Instantiates and returns a rectangle object covering the area of the Text object
        
        Parameters:
            self (object): The text object itself
        
        Return value: A rectangle object covering the area of the text object
        
        Sample call: text1.get_rect()
        '''
        return self.__surface.get_rect()
    # Setter
    def setMessage(self, message):
        '''
        Changes the text to be displayed
        
        Parameters:
            self (object): The text object iself
            message (string): The new message to be displayed
        
        Return value: None
        
        Sample call: text1.setMessage("Thank you for playing!")
        '''
        self.__message = message