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
        self.keyBackspace = False
    def ResetKeys(self):
        self.keyBackspace = False
    def CheckInput(self):
        if (self.keyBackspace):
            print("Backspace")
    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runDisplay = False
                self.game.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.keyBackspace = True
                    print(self.keyBackspace)
    def Update(self):
        self.UpdateEvents()
        self.CheckInput()
        self.ResetKeys()
        pygame.display.update()
    def DrawGrid(self):
        for i in range(self.COLS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(i * self.TILESIZE,0),(i*self.TILESIZE,self.game.DISPLAY_HEIGHT- self.LOWERMARGIN))
        for i in range(self.ROWS):
            pygame.draw.line(self.game.display,self.game.COLORS["white"],(0,i * self.TILESIZE),(self.game.DISPLAY_WIDTH - self.SIDEMARGIN,i * self.TILESIZE))
    def Render(self):
        self.game.display.fill(self.game.COLORS["gray"])
        self.DrawGrid()
        self.BlitScreen()
    def DisplayState(self):
        print("Jestem w edytorze.")
        while self.runDisplay:
            self.Update()
            self.Render()