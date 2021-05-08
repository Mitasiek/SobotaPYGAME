from State.state import State
import pygame

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
        self.scroll = 0
        self.scrollSpeed = 1
        self.keyBackspace = False
        self.cloudImage = pygame.image.load('./Sprites/Background/sky_cloud.png').convert_alpha()
        self.skyImage = pygame.image.load('./Sprites/Background/sky.png').convert_alpha()
        self.skyRect = self.skyImage.get_rect()
        self.mountainImage = pygame.image.load('./Sprites/Background/mountain2.png').convert_alpha()
        self.mountainRect = self.mountainImage.get_rect()
        self.pineForestImg1 = pygame.image.load('./Sprites/Background/pine2.png').convert_alpha()
        self.pineRect1 = self.pineForestImg1.get_rect()
        self.pineForestImg2 = pygame.image.load('./Sprites/Background/pine1.png').convert_alpha()
        self.pineRect2 = self.pineForestImg2.get_rect()

    def ResetKeys(self):
        self.keyBackspace = False
    def CheckInput(self):
        if (self.keyBackspace):
            print("Backspace")
        if (self.scrollLeft):
            self.scroll -= 5 * self.scrollSpeed
        if (self.scrollRight):
            self.scroll += 5 * self.scrollSpeed

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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.scrollLeft = False
                if event.key == pygame.K_RIGHT:
                    self.scrollRight = False
    def Update(self):
        self.UpdateEvents()
        self.CheckInput()
        self.ResetKeys()
        pygame.display.update()
    def DrawBg(self):
        self.game.display.fill(self.game.COLORS["gray"])
        self.game.display.blit(self.cloudImage, self.cloudImage.get_rect())
        self.game.display.blit(self.skyImage, (self.skyRect.x, self.skyRect.y + 200))
        self.game.display.blit(self.mountainImage, (self.mountainRect.x, self.mountainRect.y + 250))
        self.game.display.blit(self.pineForestImg1, (self.pineRect1.x, self.pineRect1.y + 300))
        self.game.display.blit(self.pineForestImg2, (self.pineRect2.x, self.pineRect1.y + 350))
    def DrawGrid(self):
        for i in range(self.COLS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(i * self.TILESIZE - self.scroll,0),(i*self.TILESIZE - self.scroll,self.game.DISPLAY_HEIGHT- self.LOWERMARGIN))
        for i in range(self.ROWS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(0,i * self.TILESIZE),(self.game.DISPLAY_WIDTH - self.SIDEMARGIN,i * self.TILESIZE))
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