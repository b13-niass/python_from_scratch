# --- Concaténation ---
prenom = "Alice"
salutation = "Bonjour, " + prenom + "!"
print("Concaténation :", salutation)

# --- Répétition ---
print("Répétition :", "Python " * 3)

# --- Accès aux caractères ---
texte = "Bonjour, le monde !"
premier_caractere = texte[0]  # Premier caractère
dernier_caractere = texte[-1]  # Dernier caractère
print("Premier caractère :", premier_caractere)
print("Dernier caractère :", dernier_caractere)

# --- Slicing (sous-chaînes) ---
sous_chaine = texte[0:7]  # Du 0e au 6e caractère (exclut l'index 7)
print("Sous-chaîne :", sous_chaine)

# --- Méthodes de transformation ---
print("En majuscules :", texte.upper())
print("En minuscules :", texte.lower())
print("Première lettre en majuscule :", texte.capitalize())
print("Chaque mot avec majuscule :", texte.title())

# --- Suppression des espaces ---
texte_avec_espaces = "   Python est génial !   "
print("Sans espaces à gauche et à droite :", texte_avec_espaces.strip())

# --- Remplacement de mots ---
nouveau_texte = texte.replace("monde", "univers")
print("Remplacement :", nouveau_texte)

# --- Découpage (split) ---
mots = texte.split()  # Sépare selon les espaces
print("Découpage en mots :", mots)

# --- Fusion (join) ---
phrase = "-".join(mots)  # Fusionne les mots avec "-"
print("Fusion des mots :", phrase)

# --- Recherche dans une chaîne ---
print("Position de 'monde' :", texte.find("monde"))  # Renvoie l'index ou -1
print("Existe-t-il 'le' dans le texte ?", "le" in texte)

# --- Validation de contenu ---
print("Est-ce que tout est en majuscules ?", texte.isupper())
print("Est-ce que tout est en minuscules ?", texte.islower())
print("Est-ce que tout est alphanumérique ?", texte.isalnum())  # Pas d'espaces ou de symboles

# --- Longueur de la chaîne ---
print("Longueur de la chaîne :", len(texte))
# --- Inverser une chaîne ---
chaine_inversee = texte[::-1]
print("Chaîne inversée :", chaine_inversee)

texte = "radar"
est_palindrome = texte == texte[::-1]
print(est_palindrome)  # Affiche True
