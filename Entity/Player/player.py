import pygame

from Entity.entity import Entity
class Player(Entity):
    def __init__(self,game):
        super().__init__(100,300,"Sprites/Player/gifs/Hero-idle.gif",2,game)
        self.speed=5
        self.directionX=0
        self.directionY=0
        self.deltaX=0
        self.deltaY=0
        self.GRAVITY=0.75
        self.flip=False
        self.jump=False
        self.velocityY=0
        self.updateTime=pygame.time.get_ticks()
        self.isInAir=False

    def Draw(self):
        #self.game.display.blit(self.image,self.imgRectangle)
        self.game.display.blit(pygame.transform.flip(self.image,self.flip,False),self.imgRectangle)


    def Move(self, rightMove, leftMove):
        print(f'{self.deltaX}')
        self.deltaX=0
        self.deltaY=0

        if rightMove==True:
            self.deltaX=self.speed
            self.directionX=1
            self.flip=False
        if leftMove==True:
            self.deltaX=-self.speed
            self.directionX=-1
            self.flip=True

        if (self.jump==True and self.isInAir==False):
            self.velocityY=-11
            self.jump=False
            self.isInAir=True
            print("skok")

        self.deltaY+=self.velocityY
        self.velocityY+=self.GRAVITY
        if self.velocityY>10:
            self.velocityY

        self.deltaY+=self.velocityY
        if self.imgRectangle.bottom +self.deltaY>400:
            self.deltaY=400-self.imgRectangle.bottom
            self.isInAir=False
        self.imgRectangle.x+=self.deltaX
        self.imgRectangle.y+=self.deltaY




