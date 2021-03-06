import pygame, sys
from pygame.locals import *
from random import randrange

"""
This Module aims to accelerate the game and count score based on obstacles
"""
#accelerates the game and count score based on obstacles
class Obstacle:
    """
    This class aims to create an obstacle
    """
    def __init__(self,param,type=1):# list image et l'obstacle est choisie a l'aleatoire
        """
        Args:
            param(parameters.param): An instance from parameters.param class, used to configure the Obstacle's behavior.
            type: between 1 and 3, it selects the type of the obstacle
        """
        self.param = param
        self.x = param.width + 50
        self.y = param.posy - 70
        if type == 1 :
            self.img=pygame.image.load("img/obf1.png")
        elif type == 2 :
            self.img=pygame.image.load("img/obf2.png")
        elif type == 3 :
            self.img=pygame.image.load("img/obf3.png")
        self.img=pygame.transform.scale(self.img, (param.tailleObs-30, param.tailleObs))
        self.out = False

    def animate(self,screen):
        """ this method manage the animation of the obstacle and detect when its position surpass the screen's weight
        """
        self.x -= self.param.vitesse
        screen.blit(self.img,(self.x,self.y))
        if self.x < 0 :
           self.out = True

class ObstacleGenerator :
    """this class aims to create obstacles
    """

    def __init__(self,param,minDist=210,max=2):
        self.param = param
        self.obstacleBuffer = []
        self.maxObstacles = max
        self.minDistance = minDist
        self.randomDistance = minDist
        self.addObstacle()

    def addObstacle(self):
        """add an obstacle randomly using the `randrange()`_ function

        .. _randrange():
                https://docs.python.org/3.1/library/random.html#random.randrange
        """
        obstacleType = randrange(1,4)
        obstacleObject = Obstacle(self.param,obstacleType)
        self.obstacleBuffer.append(obstacleObject)

    def randomize(self):
        """add an obstacle when the distance between the current place and the last obstacle is bigger than randomDistance
        """
        if (self.obstacleBuffer[-1].x < (self.param.width -self.randomDistance)):
            self.addObstacle()
            if self.param.vitesse < self.param.vitesseMax:
                self.param.accelerate(0.5)
            self.randomDistance = randrange(self.minDistance,self.param.width)

    def animateObstacles(self, screen):
        """add, delete obstacles and count the score
        """
        self.randomize()
        if self.obstacleBuffer[0].out :
            del self.obstacleBuffer[0]
            self.param.obsCount+=1
            if self.param.obsCount < self.param.comboMax:
                self.param.combo = self.param.obsCount
                self.param.score += self.param.combo
            else:
                self.param.combo = self.param.comboMax
                self.param.score += self.param.combo
        for obs in self.obstacleBuffer :
            obs.animate(screen)
        # print self.randomDistance

    def getObst(self):
        """returns the first obstacle shown on the screen
        """
        return self.obstacleBuffer[0]
