# Nathan Wong
# 05/14/2024
# Program Description: Simulates a pygame that spawns moveable balls and a moveable paddle. The game uses
# attributes and methods from various classes.

import pygame, sys
from ball import Ball
from paddle import Paddle
from text import Text

if __name__ == "__main__":
    pygame.init()
    # Creates a rectangular display 800 x 600 pixels
    screenWidth = 800
    screenHeight = 600
    surface = pygame.display.set_mode((screenWidth,screenHeight))
    DREXEL_BLUE = (7, 41, 77)
    DREXEL_GOLD = (244, 219, 133)
    GREEN = (158, 214, 149)
    BLACK = (0, 0, 0)
    balls = []
    
    ball = Ball(400, 300, 30, DREXEL_GOLD)
    paddle = Paddle(200, 20, DREXEL_BLUE)
    scoreBoard = Text("Score: 0", 10, 10)
    
    balls.append(ball)
    
    numGreen = 0
    lose = False
    win = False
    fpsClock = pygame.time.Clock()
    while True:
        initialColor = (255, 255, 255)
        # Initializes a white background
        surface.fill(initialColor)
        paddle.draw(surface)
        scoreBoard.draw(surface)
        try:
            for i in range(0,len(balls)):
                # If balls[i] does not exist, then restart the for loop
                if balls[i] == None:
                    break
                balls[i].draw(surface)
                # Results in a game over if the ball hits the sides of the paddle
                if balls[i].intersectSide(paddle):
                    lose = True
                if balls[i].intersects(paddle):
                    # Increases movement speed each time the ball hits the paddle, but prevents the ball from moving too fast
                    if (balls[i].getYSpeed() < 5) and (balls[i].getYSpeed() > -5):
                        balls[i].setYSpeed(balls[i].getYSpeed()*-1.5)
                        balls[i].setXSpeed(balls[i].getXSpeed()*1.5)
                    else:
                        balls[i].setYSpeed(balls[i].getYSpeed()*-1)
                        balls[i].setXSpeed(balls[i].getXSpeed()*1)
                    # Checking if it was the gold ball that hit the paddle
                    if i == 0:
                        # Spawns a ball if the gold ball hit the paddle
                        if len(balls) < 10:
                            balls.append(Ball(400, 300, 18, BLACK))
                for ball in balls:
                    if (balls[i] is not ball) and balls[i].isTouchingBall(ball):
                        # Increases the number of green balls score by 2 if both balls were not initially green
                        if (balls[i].getColor() != GREEN) and (ball.getColor() != GREEN):
                            numGreen += 2
                        # Increases number of green balls score by 1 if only one of the balls weren't initially green
                        elif (balls[i].getColor() != GREEN) or (ball.getColor() != GREEN):
                            numGreen += 1
                        balls[i].setXSpeed(balls[i].getXSpeed()*-1)
                        ball.setXSpeed(ball.getXSpeed()*-1)
                        balls[i].setColor(GREEN)
                        ball.setColor(GREEN)
                # Causes the ball to move in the down-right direction
                balls[i].move()
                # Results in a game over if the ball hits the bottom of the screen
                if ((balls[i].getLoc())[1] + balls[i].getRadius()) >= screenHeight:
                    # If the initial ball (gold) disappears, then it is a game over
                    if i == 0:
                        lose = True
                    balls.pop(i)
                    # If the ball that went out of bounds was a green ball, then the score decreases
                    if (balls[i].getColor() == GREEN):
                        numGreen -= 1
                    break
                scoreBoard.setMessage("Number of green balls: " + str(numGreen))
        # Ignores the situation where list index is out of range, preventing the program from crashing
        except:
            print()
        # Number of green balls cannot be below 0
        if numGreen <= -1:
            lose = True
        # Spawning all balls possible and getting them all to collide with each other results in a victory
        elif numGreen >= 10:
            win = True
        if win == True:
            surface.fill(GREEN)
            WHITE = (255, 255, 255)
            playerWin = Text("YOU WON!!", (screenWidth/2)-50, (screenHeight/2), WHITE, 40)
        if lose == True:
            # Changes surface to display losing state
            PINK_UNICORN = (255, 192, 192)
            surface.fill(PINK_UNICORN)
            WHITE = (255, 255, 255)
            playerLose = []
            playerLose.append(Text("You lost :(", (screenWidth/2)-50, (screenHeight/2)-50, WHITE, 40))
            playerLose.append(Text("Press 'q' to quit", (screenWidth/2)-50, (screenHeight/2), WHITE, 40))
            for element in playerLose:
                element.draw(surface)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or \
               (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            # Below is not needed/detrimental to the game
            #elif event.type == pygame.MOUSEBUTTONDOWN:
            #    ball.setVisible(not ball.isVisible())
        # Regularly updates the display after any graphical changes are made
        pygame.display.update()
        fpsClock.tick(60)