class User:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def afficher_info(self):
        print(f"Nom : {self.nom}, Email : {self.email}")

    def teste_order(self):
        print("Je suis un utilisateur")