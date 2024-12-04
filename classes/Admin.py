from classes.User import User
class Admin(User):
    def __init__(self, nom, permissions):
        super().__init__(nom)
        self.permissions = permissions
    def afficher_role(self):
        return f"{self.nom} est un administrateur avec les permissions : {', '.join(self.permissions)}."
