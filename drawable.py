# Nathan Wong
# 05/14/2024
# Program Description: To create a class that provides a template for drawing objects to
# a pygame surface

import pygame
from abc import ABC, abstractmethod

class Drawable(ABC):
    '''
    To provide a template for drawing objects to a pygame surface
    
    Parameters:
        ABC: Allows usage of the @abstractmethod decorator and prevents derived classes from
        functioning without a definition of the abstract method
    
    Attributes:
        x (int): The horizontal position at which the drawn object is to be displayed at
        y (int): The vertical postion at which the drawn object is to be displayed at
        visible (boolean): Whether the object to be drawn should be visible on the surface or not
        
    Methods:
        __init__: Instantiates the Drawable class
        draw: An abstract method that requires the derived class to define how its object is
        to be drawn onto the surface
        intersects: Create rectangles that cover the area of two objects and check if the two
        rectangles intersect each other
        intersectSide: Checks if one object has collided with the left or right side of another object
        get_rect: An abstract method that requires the derived class to define how a rectangle can be
        formed to cover the area of the derived class's object
        getLoc: A getter that returns the x and y attributes of Drawable
        isVisible: A getter that returns a boolean value that conveys whether the visibility of the object
        is on or off
        setLoc: Allows the user to change the x and y coordinate of the object
        setX: Allows the user to change the x coordinate of the object
        setY: Allows the user to change the y coordinate of the object
        setVisible: Allows the user to change the visibility of the object
    '''
    # Constructor
    def __init__(self, x=0, y=0):
        '''
        Initializes attribute values based on arguments passed
        
        Parameters:
            x (int): Horizontal position of object to be drawn
            y (int): Vertical position of object to be drawn
        
        Return value: None
        
        Sample call: draw1 = Drawable(5,5,True)
        '''
        self.__x = x
        self.__y = y
        self.__visible = True
    @abstractmethod
    def draw(self, surface):
        '''
        An abstract method that requires derived classes to define its own draw function
        
        Parameters:
            self (object): The instance of Drawable itself
            surface (object): The object to be displayed (a 2D image)
        
        Return value: N/A
        
        Sample call: N/A (abstract method)
        '''
        pass
    def intersects(self, other):
        '''
        Create rectangles that cover the area of two objects and check if the two
        rectangles intersect each other
        
        Parameters:
            self (object): The object itself
            other (object): Another object that is being compared to the self object
            
        Return value: Boolean indicating whether the two object's rectangles intersect
        each other or not
        
        Sample call: rect1.intersects(rect2)
        '''
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if (rect1.x < rect2.x + rect2.width) and \
           (rect1.x + rect1.width > rect2.x) and \
           (rect1.y < rect2.y + rect2.height) and \
           (rect1.height + rect1.y > rect2.y):
            return True
        return False
    def intersectSide(self, other):
        '''
        Checks if one object has collided with the left or right side of another object
        
        Parameters:
            self (object): The object itself
            other (object): Another object that is being compared to the self object
            
        Return value: Boolean indicating whether the left/right sides of the two objects collided
        
        Sample call: ball.intersectSide(paddle)
        '''
        surface = pygame.display.get_surface()
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        if ((rect1.x + rect1.width == rect2.x) or (rect1.x == rect2.x + rect2.width)) and \
           ((rect1.y + rect1.height >= rect2.y)):
            return True
        return False
    # Getters
    @abstractmethod
    def get_rect(self):
        '''
        An abstract method that returns a Pygame Rect object
        
        Parameters:
            self (object): The instance of Drawable itself
            
        Return value: N/A (abstract method)
        
        Sample call: N/A (abstract method)
        '''
        pass
    def getLoc(self):
        '''
        Returns horizontal and vertical positions of an object
        
        Parameters:
            self (object): The instance of Drawable itself
            
        Return value: A tuple containing instance attributes x and y
        
        Sample call: x, y = drawable1.getLoc()
        '''
        return (self.__x, self.__y)
    def isVisible(self):
        '''
        To determine whether the object's visibility is currently set to True or False
        
        Parameters:
            self (object): The object itself
            
        Return value: Boolean of whether the object's visibility is on or off
        
        Sample call: visibility = rect1.isVisible()
        '''
        return self.__visible
    # Setters
    def setLoc(self, x, y):
        '''
        Change the position of the object by changing the x and y coordinates
        
        Parameters:
            self (object): The object itself
            x (int): The new horizontal position of the object
            y (int): The new vertical position of the object
            
        Return value: None
        
        Sample call: rect1.setLoc(x+65, y+334)
        '''
        self.__x = x
        self.__y = y
    def setX(self, x):
        '''
        Change the horizontal position of the object
        
        Parameters:
            self (object): The object itself
            x (int): The new horizontal position of the object
            
        Return value: None
        
        Sample call: ball1.setX(2)
        '''
        self.__x = x
    def setY(self, y):
        '''
        Change the vertical position of the object
        
        Parameters:
            self (object): The object itself
            y (int): The new vertical position of the object
            
        Return value: None
        
        Sample call: ball1.setY(2)
        '''
        self.__y = y
    def setVisible(self, visible):
        '''
        Change the visibility of the object
        
        Parameters:
            self (object): The object itself
            visible (boolean): The new visibility (boolean) that the user wants for the object
            
        Return value: None
        
        Sample call: rect1.setVisible(False)
        '''
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False