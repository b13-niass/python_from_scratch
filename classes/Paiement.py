class Paiement:
    def __init__(self, solde):
        self.solde = solde

    def effectuer_paiement(self, montant):
        if montant <= self.solde:
            self.solde -= montant
            print(f"Paiement de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Fonds insuffisants pour effectuer le paiement.")

    def teste_order(self):
        print("Je suis un paiement")