from classes.Produit import Produit

produit1 = Produit("Pommes", 2, 10)
produit2 = Produit("Pommes", 2, 5)

# Utilisation de __str__ et __repr__
print(produit1)  # Utilise __str__
print(repr(produit1))  # Utilise __repr__

# Utilisation de __add__
produit3 = produit1 + produit2
print(produit3)

# Utilisation de __len__
print(f"Quantité totale : {len(produit3)}")