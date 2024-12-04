class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire      # Public
        self._solde = solde             # Protégé
        self.__numero_compte = 123456  # Privé

