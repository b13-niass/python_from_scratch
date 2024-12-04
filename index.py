from classes.Cercle import Cercle
from classes.Rectangle import Rectangle

rect = Rectangle(5, 3)
print(f"Rectangle - Aire : {rect.aire()}, Périmètre : {rect.perimetre()}")

cercle = Cercle(4)
print(f"Cercle - Aire : {cercle.aire():.2f}, Périmètre : {cercle.perimetre():.2f}")