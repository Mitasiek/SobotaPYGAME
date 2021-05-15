import pygame

class Button():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.img = pygame.transform.scale(image,int(width) * scale,int(height) * scale)
        self.imgRect = self.img.get_rect()
        self.imgRect.topleft(x,y)
        self.Clicked = False
    def Draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if (self.imgRect.collidepoint(pos)):
            if (pygame.mouse.get_pressed()[0] == 1 and self.Clicked == False):
                action = True
                self.Clicked = True
        if (pygame.mouse.get_pressed()[0] == 0):
            self.Clicked = False
        surface.blit(self.img,(self.imgRect.x,self.imgRect.y))
        return action
