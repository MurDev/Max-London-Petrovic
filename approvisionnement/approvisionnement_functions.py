def menuApprovisionnement():
    print("\n-------------| APPROVISIONNEMENT |-------------")
    print("1. Enregistrer une approvisionnement")
    print("2. Afficher toutes les approvisionnement")
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



