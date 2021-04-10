from State.state import State

class Menu(State):
    def __init__(self,game):
        super().__init__()
        self.game = game
    def UpdateEvents(self):
        pass
    def Update(self):
        pass
    def Render(self):
        pass
    def DisplayState(self):
        print("Jestem w menu gry.")
        # TODO Petla okna Menu:
        self.game.display.fill( (255,0,0) )
