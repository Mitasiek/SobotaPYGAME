from abc import abstractmethod, ABC
import pygame
class Entity(ABC):
    def __init__(self,x,y,img,scale,game):
        self.game=game
        self.image=pygame.image.load(img)
        self.positionX=x
        self.positionY=y
        self.imgRectangle = self.image.get_rect()
        self.image=pygame.transform.scale(self.image,(self.imgRectangle.width*scale,self.imgRectangle.height*scale))
        self.imgRectangle.x=self.positionX
        self.imgRectangle.y=self.positionY
    @abstractmethod
    def Draw(self):
        pass