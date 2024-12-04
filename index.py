from classes.Admin import Admin
from classes.Client import Client
from classes.User import User
def afficher_roles_utilisateurs(utilisateurs):
    for utilisateur in utilisateurs:
        print(utilisateur.afficher_role())
user = User("Alice")
client = Client("Bob", 12345)
admin = Admin("Charlie", ["ajouter utilisateur", "supprimer utilisateur"])

utilisateurs = [user, client, admin]

afficher_roles_utilisateurs(utilisateurs)

