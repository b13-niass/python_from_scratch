import time
def mesurer_temps_execution(fonction):
    def wrapper(*args, **kwargs):
        debut = time.time()
        print(args)
        print(kwargs)
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print(f"Temps d'exécution de '{fonction.__name__}': {fin - debut:.4f} secondes")
        return resultat
    return wrapper

@mesurer_temps_execution
def somme_nombres(n,nom="sss"):
    time.sleep(1)
    return sum(range(1, n + 1))

resultat = somme_nombres(1000000, nom="Test")
print(f"Résultat : {resultat}")