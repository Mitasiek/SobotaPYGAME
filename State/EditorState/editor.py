from State.state import State
import pygame
# Nowe elementy: tlo, animacja tla, przewijanie, tick Clocka, Nowe rzeczy konstruktor
class Editor(State):
    def __init__(self,game):
        super().__init__(game)
        self.TILESIZE = 32
        self.LOWERMARGIN = 100
        self.SIDEMARGIN = 200
        self.COLS = 30
        self.ROWS = (self.game.DISPLAY_WIDTH - self.SIDEMARGIN) // self.TILESIZE
        self.scrollLeft = False
        self.scrollRight = False
        self.leftShift = False
        self.scroll = 0
        self.scrollSpeed = 1
        self.keyBackspace = False
        self.cloudImage = pygame.image.load('./Sprites/Background/sky_cloud.png').convert_alpha()
        self.skyImage = pygame.image.load('./Sprites/Background/sky.png').convert_alpha()
        #self.skyRect = self.skyImage.get_rect()
        self.mountainImage = pygame.image.load('./Sprites/Background/mountain2.png').convert_alpha()
        #self.mountainRect = self.mountainImage.get_rect()
        self.pineForestImg1 = pygame.image.load('./Sprites/Background/pine2.png').convert_alpha()
        #self.pineRect1 = self.pineForestImg1.get_rect()
        self.pineForestImg2 = pygame.image.load('./Sprites/Background/pine1.png').convert_alpha()
        #self.pineRect2 = self.pineForestImg2.get_rect()
        self.TILE_COUNT = 16
        self.InitTiles()
    def InitTiles(self):
        self.imgList = []
        for x in range(5):
            img = pygame.image.load(f'Sprites/Tiles/grass_{x+1}.png')
            img = pygame.transform.scale(img,(self.TILESIZE,self.TILESIZE))
            self.imgList.append(img)
        for x in range(11):
            img = pygame.image.load(f'Sprites/Tiles/ground_{x+1}.png')
            img = pygame.transform.scale(img, (self.TILESIZE, self.TILESIZE))
            self.imgList.append(img)
        print(self.imgList)
    def ResetKeys(self):
        self.keyBackspace = False
    def CheckInput(self):
        if (self.keyBackspace):
            print("Backspace")
        if (self.scrollLeft and self.scroll > 10):
            self.scroll -= 5 * self.scrollSpeed
        if (self.scrollRight):
            self.scroll += 5 * self.scrollSpeed
        if (self.leftShift):
            self.scrollSpeed = 5
        if (self.leftShift == False):
            self.scrollSpeed = 1

    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runDisplay = False
                self.game.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.keyBackspace = True
                    print(self.keyBackspace)
                if event.key == pygame.K_LEFT:
                    self.scrollLeft = True
                if event.key == pygame.K_RIGHT:
                    self.scrollRight = True
                if event.key == pygame.K_LSHIFT:
                    self.leftShift = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.scrollLeft = False
                if event.key == pygame.K_RIGHT:
                    self.scrollRight = False
                if event.key == pygame.K_LSHIFT:
                    self.leftShift = False
    def Update(self):
        self.UpdateEvents()
        self.CheckInput()
        self.ResetKeys()
        pygame.display.update()
    def DrawBg(self):
        # ZMIANY
        self.game.display.fill(self.game.COLORS["gray"])
        width = self.skyImage.get_width()
        for x in range(4):
            self.game.display.blit(self.cloudImage, ((x * width)-self.scroll * 0.5,0))
            self.game.display.blit(self.skyImage, ((x * width)-self.scroll * 0.6, self.game.DISPLAY_HEIGHT - self.skyImage.get_height() - 250))
            self.game.display.blit(self.mountainImage,((x * width)-self.scroll * 0.7, self.game.DISPLAY_HEIGHT - self.mountainImage.get_height() - 250))
            self.game.display.blit(self.pineForestImg2, ((x * width)-self.scroll * 0.8,self.game.DISPLAY_HEIGHT - self.pineForestImg2.get_height() - 180))
            self.game.display.blit(self.pineForestImg1, ((x * width)-self.scroll * 0.9,self.game.DISPLAY_HEIGHT - self.pineForestImg2.get_height() - 150))

    def DrawGrid(self):
        for i in range(self.COLS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(i * self.TILESIZE - self.scroll,0),(i*self.TILESIZE - self.scroll,self.game.DISPLAY_HEIGHT- self.LOWERMARGIN))
        for i in range(self.ROWS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(0,i * self.TILESIZE),(self.game.DISPLAY_WIDTH - self.SIDEMARGIN,i * self.TILESIZE))
    def InitButtons(self):
        pass
    def DrawEditorPanel(self):
        pygame.draw.rect(self.game.display,self.game.COLORS['black'],(self.game.DISPLAY_WIDTH - self.SIDEMARGIN,0,self.SIDEMARGIN,self.game.DISPLAY_HEIGHT + self.LOWERMARGIN))
        pygame.draw.rect(self.game.display,self.game.COLORS["black"],(0,self.game.DISPLAY_HEIGHT - self.LOWERMARGIN,self.game.DISPLAY_WIDTH,self.game.DISPLAY_HEIGHT - self.LOWERMARGIN))
    def Render(self):
        self.DrawBg()
        self.DrawGrid()
        self.DrawEditorPanel()
        self.BlitScreen()
    def DisplayState(self):
        print("Jestem w edytorze.")
        while self.runDisplay:
            self.Update()
            self.Render()
            # ZEGAR
            self.game.clock.tick( self.game.FPS )