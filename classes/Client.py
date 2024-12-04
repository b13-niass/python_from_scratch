from classes.User import User
class Client(User):
    def __init__(self, nom, numero_client):
        super().__init__(nom)
        self.numero_client = numero_client
    def afficher_role(self):
        return f"{self.nom} est un client avec le numéro {self.numero_client}."
