from abc import abstractmethod,ABC
import pygame

class State(ABC):
    def __init__(self,game):
        self.runDisplay = True
        self.game = game
    @abstractmethod
    def UpdateEvents(self):
        pass
    @abstractmethod
    def Update(self):
        pass
    @abstractmethod
    def Render(self):
        pass
    @abstractmethod
    def DisplayState(self):
        pass
    def BlitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()