from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass