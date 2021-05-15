import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,imgSrc,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(imgSrc)
        self.imgRect = self.img.get_rect()
        self.imgRect.x = x
        self.imgRect.y = y
    def Draw(self,surface):
        surface.blit(self.img,(self.rect.x,self.rect.y))