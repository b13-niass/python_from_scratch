class User:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def se_connecter(self):
        print(f"{self.nom} s'est connecté avec l'email {self.email}.")
