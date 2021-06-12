from Entity.entity import Entity
class Player(Entity):
    def __init__(self,game):
        super().__init__(100,100,"Sprites/Player/gifs/Hero-idle.gif",2,game)
        self.speed=1
        self.directionX=0
        self.directionY=0

    def Draw(self):
        self.game.display.blit(self.image,(self.imgRectangle.y,self.imgRectangle.x))

    def Move(self,value):
        #self.imgRectangle.x -= 1
        print("poruszanie sie")
        self.imgRectangle.x+=1


