class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.en_marche = False

    def demarrer(self):
        if not self.en_marche:
            self.en_marche = True
            print(f"La {self.marque} {self.modele} est maintenant en marche.")
        else:
            print(f"La {self.marque} {self.modele} est déjà en marche.")

