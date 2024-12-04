from classes.User import User
class Client(User):
    def __init__(self, nom, email, numero_client):
        # Appeler le constructeur de la classe parent
        super().__init__(nom, email)
        self.numero_client = numero_client

    def afficher_informations(self):
        print(f"Nom : {self.nom}, Email : {self.email}, Numéro client : {self.numero_client}")
