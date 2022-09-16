import vente
from vente.vente import Vente
def menuVente():
    print("\n-------------| VENTE |-------------")
    print("1. Enregistrer une vente")
    print("2. Afficher toutes les ventes")
    print("0. Retour")
    print("----------------------------------------")

    choix = input(">> : ")

    while 1:
        if not choix.isdigit() or (int(choix)<0 or int(choix)>2):
            choix = input('Entrez une valeur numerique entiere entre 0 et 2 : ')
        else:
            choix = int(choix)
            break
    return choix

def prix_essence(essence):
    if essence == "Gazoline":
        return Vente.prix_gallon_gazoline
    elif essence == "Diesel":
        return Vente.prix_gallon_diesel
    else:
        return 0

