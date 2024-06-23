# Nathan Wong
# 05/14/2024
# Program Description: To provide a blueprint for a ball to move around a screen

import pygame, math, sys, random
from drawable import Drawable

class Ball(Drawable):
    '''
    Draws a ball at a given location that moves around a display
    
    Parameters:
        Drawable (base class): Instantiated in constructor
    
    Attributes:
        radius (int/float): The ball's radius, which dictates the size of the ball
        color (tuple): RBG tuple that sets the color of the ball object
        xSpeed (int): The speed at which the ball moves horizontally
        ySpeed (int): The speed at which the ball moves vertically
        
    Methods:
        __init__: Instantiates the ball object
        draw: Displays the ball object on the surface object if the Drawable object's
        isVisible attribute value is True
        get_rect: Instantiates a pygame.Rect object that covers the ball's area
        getColor: Returns the color attribute
        getRadius: Returns the radius attribute
        isTouchingBall:
        getXSpeed: Returns the xSpeed attribute
        getYSpeed: Returns the ySpeed attribute
        move: Changes the ball object's position on the surface
        setColor: Changes the ball's color
        setRadius: Changes the radius attribute
        setXSpeed: Changes the xSpeed attribute
        setYSpeed: Changes the ySpeed attribute
    '''
    # Constructor
    def __init__(self, x=0, y=0, radius=10, color=(0,0,0)):
        '''
        Instantiates the base class Drawable based on given arguments as well as the Ball object itself
        
        Parameters:
            x (int): Horizontal position of the ball relative to center
            y (int): Vertical position of the ball relative to center
            radius (int or float): The radius of the ball, measured from the center position
            color (integer tuple): RGB value (tuple of three integers) to represent the color of the ball
                
        Return value: None
        
        Sample call: ball1 = Ball(1,9,5,(255,0,0))
        '''
        super().__init__(x, y)
        self.__radius = radius
        self.__color = color
        # Randomizes the initial x-direction of the ball
        self.__xSpeed = random.randint(-1, 1) * 2
        if self.__xSpeed == 0:
            self.__xSpeed += 1
        self.__ySpeed = 2
    def draw(self, surface):
        '''
        Draws ball instances on a provided surface
        
        Parameters:
            self (object): The Ball object itself
            surface (object): The object to be drawn on
            
        Return value: None
        
        Sample call: ball1.draw(surface)
        '''
        # Only draws the Ball object to the surface if visibility is true
        if self.isVisible():
            loc = self.getLoc()
            pygame.draw.circle(surface, self.__color, \
                               (loc[0], loc[1]), self.__radius)
    # Getters
    def get_rect(self):
        '''
        Instantiate and return a pygame.Rect object that covers the Ball's area
        
        Parameters:
            self (object): The Ball object itself
            
        Return value: A pygame.Rect object
        
        Sample call: ball1.get_rect()
        '''
        loc = self.getLoc()
        radius = self.__radius
        return pygame.Rect(loc[0] - radius, loc[1] - radius, \
                           2 * radius, 2 * radius)
    def getColor(self):
        '''
        Return the instance's color attribute
        
        Parameters:
            self (object): The Ball object itself
        
        Return value: A three-integer tuple representing the Ball object's RBG color
        
        Sample call: ball1.getColor()
        '''
        return self.__color
    def getRadius(self):
        '''
        Return the instance's radius attribute
        
        Parameters:
            self (object): The Ball object itself
            
        Return value: An integer representing the instance's current radius
        
        Sample call: radius = ball1.getRadius()
        '''
        return self.__radius
    def isTouchingBall(self, other):
        '''
        Checks if a ball collided with another ball.
        
        Parameters:
            self (object): The Ball object itself
            other (object): The object that is being compared against
            
        Return value: Boolean indicating whether the ball collided with "other" or not
        
        Sample call: ball.isTouchingBall(ball[1])
        '''
        if self.intersects(other):
            return True
        return False
    def getXSpeed(self):
        '''
        Return the instance's xSpeed attribute
        
        Parameters:
            self (object): The Ball object itself
            
        Return value: An integer value representing the ball's horizontal movement speed
        
        Sample call: xSpeed = ball1.getXSpeed()
        '''
        return self.__xSpeed
    def getYSpeed(self):
        '''
        Return the instance's ySpeed attribute
        
        Parameters:
            self (object): The Ball object itself
            
        Return value: An integer value representing the ball's vertical movement speed
        
        Sample call: ySpeed = ball1.getYSpeed()
        '''
        return self.__ySpeed
    # Setters
    def move(self):
        '''
        Increases the Ball object's horizontal and vertical positions by based on attributes
        xSpeed and ySpeed. This method also handles instances where the ball's position intersects
        with the display surface's edges.
        
        Parameters:
            self (object): The Ball object itself
            
        Return value: None
        
        Sample call: ball1.move()
        '''
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed
        self.setX(newX)
        self.setY(newY)
        
        # Stores the width and height pixel values of the surface
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        
        # Checks to see if the ball's edges hit any of the display surface's edges
        # If so, the ball's movement goes in the opposite direction
        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1
        if newY <= self.__radius:
            self.__ySpeed *= -1
    def setColor(self, color=(0,0,0)):
        '''
        Allow the user to change the ball object's color
        
        Parameters:
            self (object): The Ball object itself
            color (tuple): The new color to fill the ball object based on RGB values. If no argument
            is passed, the color automatically changes to black.
        
        Return value: None
        
        Sample call: ball1.setColor((255,54,205))
        '''
        self.__color = color
    def setRadius(self, radius):
        '''
        Allow the user to change the ball object's radius and thus its size
        
        Parameters:
            self (object): The Ball object itself
            radius (int/float): The new value that dictates the ball's radius
            
        Return value: None
        
        Sample call: ball1.setRadius(5.5)
        '''
        self.__radius = radius
    def setXSpeed(self, speed):
        '''
        Allow the user to change the speed at which the ball moves horizontally
        
        Parameters:
            self (object): The Ball object itself
            speed (int): The new horizontal speed at which the ball moves
            
        Return value: None
        
        Sample call: ball1.setXSpeed(5)
        '''
        self.__xSpeed = speed
    def setYSpeed(self, speed):
        '''
        Allow the user to change the speed at which the ball moves vertically
        
        Parameters:
            self (object): The Ball object itself
            speed (int): The new vertical speed at which the ball moves
            
        Return value: None
        
        Sample call: ball1.setYSpeed(6)
        '''
        self.__ySpeed = speed