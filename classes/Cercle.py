from classes.Forme import Forme
from math import pi

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return pi * self.rayon ** 2

    def perimetre(self):
        return 2 * pi * self.rayon