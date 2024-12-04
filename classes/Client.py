from classes.Paiement import Paiement
from classes.User import User
class Client(User, Paiement):
    def __init__(self, nom, email, solde, numero_client):
        # Appeler les constructeurs des classes parents
        User.__init__(self, nom, email)
        Paiement.__init__(self, solde)
        self.numero_client = numero_client

    def afficher_info_client(self):
        self.afficher_info()  # Méthode de Utilisateur
        print(f"Numéro client : {self.numero_client}, Solde : {self.solde}€")
