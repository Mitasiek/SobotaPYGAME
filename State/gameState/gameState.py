from State.state import State
from Entity.Player.player import Player
import pygame

class GameState (State):
    def __init__(self,game):
        super().__init__(game)
        self.player=Player(game)
        self.KEY_LEFT = False
        self.KEY_RIGHT = False



    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runDisplay = False
                self.game.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    print("wyjście")
                    self.game.RemoveState()
                    self.runDisplay=False
                if event.key == pygame.K_LEFT:
                    self.KEY_LEFT=True
                if event.key == pygame.K_RIGHT:
                        self.KEY_RIGHT = True

    def CheckInputs(self):
        if (self.KEY_LEFT):
            print("w lewo")
        if (self.KEY_RIGHT):
            print("w prawo")


    def ResetKeys(self):
        self.KEY_LEFT=False
        self.KEY_RIGHT=False

    def Update(self):
        self.UpdateEvents()
        self.CheckInputs()


    def Render(self):
        self.game.display.fill(self.game.COLORS["red"])
        self.player.Draw()
        self.BlitScreen()


    def DisplayState(self):
        print("Jestem w grze.")
        self.runDisplay = True
        while self.runDisplay:
            self.Update()
            self.Render()

