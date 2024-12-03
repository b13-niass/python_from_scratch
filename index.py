from typing import Union


# def saluer(prenom: str) -> str:
#     return f"Bonjour, {prenom} !"
#
# # Appel de la fonction
# prenom: str = "Alice"
# message = saluer(prenom)
# print("Message (str) :", message)

# def infos_utilisateur(nom: str, age: int) -> dict[str, str | int]:
#     return {"nom": nom, "age": age}
#
# # Appel de la fonction
# utilisateur = infos_utilisateur("Alice", 25)
# print("Infos utilisateur :", utilisateur)

# def liste_carrés(n: int) -> list[int]:
#     return [i ** 2 for i in range(n)]
#
# # Appel de la fonction
# print("Liste des carrés :", liste_carrés(5))  # [0, 1, 4, 9, 16]

# def calculer(a: int, b: int, operation: str) -> Union[int, str]:
#     if operation == "addition":
#         return a + b
#     elif operation == "soustraction":
#         return a - b
#     else:
#         return "Opération non reconnue"
#
# # Appel de la fonction
# print(calculer(5, 3, "addition"))       # 8
# print(calculer(5, 3, "soustraction"))   # 2
# print(calculer(5, 3, "multiplication")) # "Opération non reconnue"
#
#
# def afficher_message(message: str) -> None:
#     print(message)
#
# # Appel de la fonction
# afficher_message("Ceci est un message.")
