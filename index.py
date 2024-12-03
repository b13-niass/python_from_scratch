# --- Définir une fonction avec plusieurs paramètres ---
def addition(a, b):
    return a + b

# Appeler la fonction avec deux arguments
resultat = addition(5, 3)
print("Résultat de l'addition :", resultat)

# --- Définir une fonction avec des valeurs par défaut ---
def saluer_personnalise(prenom="inconnu", age=0):
    print(f"Bonjour, {prenom}. Vous avez {age} ans.")

# Appeler sans arguments (utilise les valeurs par défaut)
saluer_personnalise()

# Appeler avec des arguments
saluer_personnalise("Bob", 25)
saluer_personnalise(prenom="Bob", age=25)

# --- Définir une fonction avec un nombre variable d'arguments ---
def afficher_nombres(*nombres):
    print("Les nombres sont :", nombres)

# Appeler avec plusieurs arguments
afficher_nombres(1, 2, 3, 4, 5)


# --- Définir une fonction avec des arguments nommés ---
def infos(**details):
    for cle, valeur in details.items():
        print(f"{cle} : {valeur}")

# Appeler avec des arguments nommés
infos(nom="Alice", age=30, ville="Paris")

