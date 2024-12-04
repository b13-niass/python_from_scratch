class CompteBancaire:
    # Attributs de classe (communs à toutes les instances)
    taux_interet = 0.05

    # Constructeur : initialise les attributs d'instance
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire  # Attribut d'instance
        self.solde = solde          # Attribut d'instance

    # Méthode d'instance pour débiter un certain montant
    def retirer(self, montant):
        if montant > self.solde:
            print("Fonds insuffisants.")
        else:
            self.solde -= montant
            print(f"{montant}€ retirés. Nouveau solde : {self.solde}€")

    # Méthode de classe pour changer le taux d'intérêt
    @classmethod
    def changer_taux_interet(cls, nouveau_taux):
        cls.taux_interet = nouveau_taux
        print(f"Nouveau taux d'intérêt : {cls.taux_interet * 100}%")

    # Méthode statique (pas liée à l'instance ni à la classe)
    @staticmethod
    def afficher_bienvenue():
        print("Bienvenue dans votre banque !")