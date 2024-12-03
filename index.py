personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

print("\nDictionnaire : ", personne)
print("Nom :", personne['nom'])

personne["age"] = 26
print("Après modification :", personne)

personne["profession"] = "Ingénieur"
print("Après ajout :", personne)

del personne["ville"]
print("Après suppression :", personne)

print("Est-ce que 'nom' est une clé ?", "nom" in personne)
