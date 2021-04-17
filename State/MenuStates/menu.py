from State.state import State
import pygame
# TODO: SKALOWANIE ZDJECIA MENU, inne staty, przeskiwanie statow, wczytanie tla
class Menu(State):
    def __init__(self,game):
        super().__init__(game)
        self.mid_w = self.game.DISPLAY_WIDTH / 2
        self.mid_h = self.game.DISPLAY_HEIGHT / 2
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100
        self.start_h = self.mid_h - 40
        self.option_h = self.start_h + 40
        self.editor_h = self.option_h + 40
        self.credits_h = self.editor_h + 40
        self.exit_h = self.credits_h + 40
        # State controls:
        self.menuState = "Start"
        self.cursor_rect.midtop = (self.mid_w - 80, self.start_h)
        # Keys
        self.keyDown = False
        self.keyUp = False
        self.keyEnter = False
    def DrawCursor(self):
        self.game.DrawText("*", 30, self.cursor_rect.x, self.cursor_rect.y + 5, self.game.COLORS["white"])
    def DrawMenu(self):
        self.game.DrawText("Menu", 48, self.mid_w, self.mid_h - 200, self.game.COLORS["white"])
        self.game.DrawText("Start Game", 32, self.mid_w, self.start_h, self.game.COLORS["white"])
        self.game.DrawText("Options",32,self.mid_w,self.option_h,self.game.COLORS["white"])
        self.game.DrawText("Editor",32,self.mid_w,self.editor_h,self.game.COLORS["white"])
        self.game.DrawText("Credits",32,self.mid_w,self.credits_h,self.game.COLORS["white"])
        self.game.DrawText("Quit Game",32,self.mid_w,self.exit_h,self.game.COLORS["white"])
        self.DrawCursor()
    def MoveCursor(self):
        print(self.menuState)
        if (self.keyDown == True):
            if (self.menuState == "Start"):
                self.cursor_rect.midtop = (self.mid_w - 50, self.option_h)
                self.menuState = "Options"
            elif (self.menuState == "Options"):
                self.cursor_rect.midtop = (self.mid_w - 50, self.editor_h)
                self.menuState = "Editor"
            elif (self.menuState == "Editor"):
                self.cursor_rect.midtop = (self.mid_w - 50, self.credits_h)
                self.menuState = "Credits"
            elif (self.menuState == "Credits"):
                self.cursor_rect.midtop = (self.mid_w - 70, self.exit_h)
                self.menuState = "Exit"
            elif (self.menuState == "Exit"):
                self.cursor_rect.midtop = (self.mid_w - 80, self.start_h)
                self.menuState = "Start"
            self.keyDown = False
        if (self.keyUp == True):
            if (self.menuState == "Start"):
                self.cursor_rect.midtop = (self.mid_w - 70, self.exit_h)
                self.menuState = "Exit"
            elif (self.menuState == "Options"):
                self.cursor_rect.midtop = (self.mid_w - 80, self.start_h)
                self.menuState = "Start"
            elif (self.menuState == "Editor"):
                self.cursor_rect.midtop = (self.mid_w - 50, self.option_h)
                self.menuState = "Options"
            elif (self.menuState == "Credits"):
                self.cursor_rect.midtop = (self.mid_w - 50, self.editor_h)
                self.menuState = "Editor"
            elif (self.menuState == "Exit"):
                self.cursor_rect.midtop = (self.mid_w - 50, self.credits_h)
                self.menuState = "Credits"
            self.keyUp = False
    def CheckInput(self):
        if (self.keyEnter):
            print("Klawisz Enter został wcisnięty")
            print(f'State: {self.menuState}')
    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runDisplay = False
                self.game.start = False
            if event.type == pygame.KEYDOWN:
                #Lista obslugiwanych klawiszy
                if event.key == pygame.K_RETURN:
                    self.keyEnter = True
                    self.CheckInput()
                if event.key == pygame.K_BACKSPACE:
                    print("Cofamy się")
                if event.key == pygame.K_DOWN:
                    self.keyDown = True
                    self.MoveCursor()
                if event.key == pygame.K_UP:
                    self.keyUp = True
                    self.MoveCursor()
    def Update(self):
        self.UpdateEvents()
        pygame.display.update()
    def Render(self):
        self.game.display.fill(self.game.COLORS["red"])
        self.game.display.blit(self.game.bg,self.game.bgRect)
        self.DrawMenu()
        self.BlitScreen()
    def DisplayState(self):
        print("Jestem w menu gry.")
        while self.runDisplay:
            self.Update()
            self.Render()

        #self.game.display.fill( (255,0,0) )
