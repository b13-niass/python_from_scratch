class User:
    def __init__(self, nom):
        self.nom = nom
    def afficher_role(self):
        return f"{self.nom} est un utilisateur."
