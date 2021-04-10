from abc import abstractmethod,ABC


class State(ABC):
    def __init__(self):
        self.runDisplay = True
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