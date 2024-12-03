animaux = {"Chat", "Chien", "Oiseau", "Chat"}
print("\nEnsemble (sans doublons) :", animaux)

animaux.add("Poisson")
print("Après ajout :", animaux)

animaux.discard("Chien")
print("Après suppression :", animaux)

print("Est-ce que 'Chat' est présent ?", "Chat" in animaux)
