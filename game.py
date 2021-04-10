import pygame
from State.MenuStates.menu import Menu

class Game():
    # Konstruktor klasy Game:
    def __init__(self):
        pygame.init()
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.DISPLAY_WIDTH = 800
        self.DISPLAY_HEIGHT = 640
        self.start = True
        self.display = pygame.Surface( (self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT) )
        self.window = pygame.display.set_mode( (self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT) )
        self.menuState = Menu(self)
        self.currentState = self.menuState
        self.fontSRC = "Font/GODOFWAR.TTF"
        self.COLORS = {
            "white":(255,255,255),
            "black":(0,0,0),
            "red":(255,0,0),
            "green":(0,255,0),
            "blue":(0,0,255)
        }
    # Narzedzia do obslugi gry
    def DrawText(self, text, size, x, y, color):
        # TODO: Domyslny kolor ustawić na biały
        font = pygame.font.Font(self.fontSRC, size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.center = ( x, y )
        self.display.blit(textSurface,textRect)
    # Obsluga klasy Game
    def InitGameSettings(self):
        pygame.display.set_caption("Nasza gra z Creative Club")
    def Update(self):
        pygame.display.update()
    def Render(self):
        self.currentState.DisplayState() # WYSWIETLAM MENU
        self.window.blit( self.display, (0,0) ) # wyswietla zawartosc display od pkt X = 0 Y = 0
    def Run(self):
        self.InitGameSettings()
        while self.start:
            self.Update()
            self.Render()
            self.clock.tick( self.FPS )
