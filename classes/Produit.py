class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def __str__(self):
        return f"Produit: {self.nom}, Prix: {self.prix}€, Quantité: {self.quantite}"

    def __repr__(self):
        return f"Produit({repr(self.nom)}, {self.prix}, {self.quantite})"

    def __add__(self, autre):
        if isinstance(autre, Produit) and self.nom == autre.nom:
            return Produit(self.nom, self.prix, self.quantite + autre.quantite)
        raise ValueError("Les produits doivent être identiques pour les additionner.")

    def __len__(self):
        return self.quantite