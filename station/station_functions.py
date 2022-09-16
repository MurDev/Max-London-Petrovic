def menuPrincipal():
    print("\n-------------| MAX LONDON PETROVIC |-------------")
    print("1. Station")
    print("2. Commande")
    print("3. Approvisionnement")
    print("4. Vente")
    print("0. Quitter le programme")
    print("---------------------------------------------------")

    print("\nChoisis un module en utilisant le chiffre correspondant ")
    choixModule = input(">> : ")
    
    while 1:
        if not choixModule.isdigit() or (int(choixModule)<0 or int(choixModule)>4):
            choixModule = input('Entrez une valeur numerique entiere entre 0 et 4 : ')
        else:
            choixModule = int(choixModule)
            break
    return choixModule

def menuStation():
    print("\n-------------| STATION |-------------")
    print("1. Enregistrer un station")
    print("2. Modifier la capacite")
    print("3. Afficher toutes les stations")
    print("0. Retour")
    print("----------------------------------------")

    choix = input(">> : ")

    while 1:
        if not choix.isdigit() or (int(choix)<0 or int(choix)>3):
            choix = input('Entrez une valeur numerique entiere entre 0 et 3 : ')
        else:
            choix = int(choix)
            break
    return choix

def choixZone():
    print("\n-------------| SELECTIONNEZ LA ZONE |-------------")
    print("1. Lalue ")
    print("2. Tabarre ")
    print("3. Clercine ")
    print("4. Petion-Ville ")
    print("0. Retour ")
    print("----------------------------------------------------")

    choix = input(">> : ")

    while 1:
        if not choix.isdigit() or (int(choix)<0 or int(choix)>4):
            choix = input('Entrez une valeur numerique entiere entre 0 et 4 : ')
        else:
            choix = int(choix)
            break
    return choix

def choix_type_essence():
    print("\n-------------| SELECTIONNEZ LE TYPE D'ESSENCE |-------------")
    print("1. Gazoline ")
    print("2. Diesel ")
    print("3. Gazoline et Diesel ")
    print("0. Retour ")
    print("--------------------------------------------------------------")

    choix = input(">> : ")
    while 1:
        if not choix.isdigit() or (int(choix)<0 or int(choix)>3):
            choix = input('Entrez une valeur numerique entiere entre 0 et 3 : ')
        else:
            choix = int(choix)
            break
    return choix

def controle_nbre_gallon(min, max):
    nbre_gallon = input(">> : ")
    while 1:
        if not nbre_gallon.isdigit() or (int(nbre_gallon)<min or int(nbre_gallon)>max):
            print("Entrez une valeur numerique entiere entre ", min, " et ", max)
            nbre_gallon = input(">> : ")
        else:
            nbre_gallon = int(nbre_gallon)
            break
    return nbre_gallon
