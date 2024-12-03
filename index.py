# # --- Gestion des exceptions de base ---
# try:
#     numerateur = int(input("Entrez un numérateur : "))
#     denominateur = int(input("Entrez un dénominateur : "))
#     resultat = numerateur / denominateur
#     print(f"Résultat : {resultat}")
# except ZeroDivisionError:
#     print("Erreur : Division par zéro impossible.")
# except ValueError:
#     print("Erreur : Vous devez entrer un nombre entier.")
# except Exception as e:
#     print(f"Erreur inattendue : {e}")
# else:
#     print("La division a été effectuée avec succès.")
# finally:
#     print("Fin du programme.")
#

# --- Lever une exception manuellement ---
def verifier_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    print(f"L'âge est : {age}")

try:
    verifier_age(-5)
except ValueError as e:
    print(f"Erreur : {e}")
