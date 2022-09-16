def menuCommande():
    print("\n-------------| COMMANDE |-------------")
    print("1. Enregistrer une commande")
    print("2. Afficher toutes les commandes")
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

def genererCommande(dict_station):
    total_gallon_gazoline_manquant = 0
    total_gallon_diesel_manquant = 0
    list_info_commande = [-1]

    if not dict_station:
        print("\nAucune station enregistree pour le moment")
        return list_info_commande
    elif len(dict_station) < 4:
        print("\nVeuillez enregistrer toutes les stations")
        return list_info_commande
    else:
        passer_commande_gazoline = False
        passer_commande_diesel   = False
        total_gallon_gazoline_manquant = 0
        total_gallon_diesel_manquant = 0
        qte_gazoline_commande = 0
        qte_diesel_commande = 0

        print("\n-------------| SELECTIONNEZ LE TYPE D'ESSENCE |-------------")
        print("1. Gazoline ")
        print("2. Diesel ")
        print("3. Gazoline et Diesel ")
        print("0. Retour ")
        print("--------------------------------------------------------------")

        choix_du_type_essence = input(">> : ")
        while 1:
            if not choix_du_type_essence.isdigit() or (int(choix_du_type_essence)<0 or int(choix_du_type_essence)>3):
                choix_du_type_essence = input('Entrez une valeur numerique entiere entre 0 et 3 : ')
            else:
                choix_du_type_essence = int(choix_du_type_essence)
                break

        print("\n---------------| Informations sur les stations |---------------------------------")
        for station in dict_station.values():
            print("Nom du station       : ", station.nom_station)
            print("Gazoline disponible  : ", station.quantite_gazoline_disponible, " gallons")
            print("Gazoline utilise     : ", (station.pourcentage_gazoline_utilise() * station.capacite_gazoline)/100, " gallons")
            print("Diesel disponible    : ", station.quantite_diesel_disponible, " gallon")
            print("Diesel utilise       : ", (station.pourcentage_diesel_utilise() * station.capacite_diesel)/100, " gallons")
            print("-------------------------------------------------------------------------------")
            
            if station.pourcentage_gazoline_disponible() < 100:
                passer_commande_gazoline = True
                total_gallon_gazoline_manquant += station.capacite_gazoline - station.quantite_gazoline_disponible
            
            if station.pourcentage_diesel_disponible() < 100 :
                passer_commande_diesel = True
                total_gallon_diesel_manquant += station.capacite_diesel - station.quantite_diesel_disponible
            
            
        match choix_du_type_essence:
            case 0:
                pass
            case 1:
                if passer_commande_gazoline == True:    
                    qte_gazoline_commande = (1.25 * total_gallon_gazoline_manquant)
                else:
                    print("\nToutes les stations sont remplies de gazoline a 100%")
            case 2:
                if passer_commande_diesel == True:
                    qte_diesel_commande = (1.10 * total_gallon_diesel_manquant)
                else:
                    print("\nToutes les stations sont remplies de diesel a 100%")
            case 3:
                if passer_commande_gazoline == True:    
                    qte_gazoline_commande = (1.25 * total_gallon_gazoline_manquant)
                else:
                    print("\nToutes les stations sont remplies de gazoline a 100%")
                
                if passer_commande_diesel == True:
                    qte_diesel_commande = (1.10 * total_gallon_diesel_manquant)
                else:
                    print("\nToutes les stations sont remplies de diesel a 100%")
            case _:
                pass


        if (passer_commande_gazoline==True and qte_gazoline_commande>0)  or (passer_commande_diesel==True and qte_diesel_commande>0):
            print("\nUne commande a ete genere automatiquement")

            print("\n-----------------------COMMANDE---------------------------------")
            print("Gazoline................", round(qte_gazoline_commande), "gallon(s)")
            print("Diesel..................", round(qte_diesel_commande),   "gallon(s)")

            print("\nVoulez-vous enregistrer la commande genere ci-dessus?")
            print("1. OUI")
            print("0. NON")
            choix_admin = input(">> : ")

            while 1:
                if not choix_admin.isdigit() or (int(choix_admin)<0 or int(choix_admin)>1):
                    print("Entrez une valeur numerique entiere entre 0 et 1")
                    choix_admin = input(">> : ")
                else:
                    choix_admin = int(choix_admin)
                    break
            
            list_info_commande[0] = (choix_admin)
            list_info_commande.append(qte_gazoline_commande)
            list_info_commande.append(qte_diesel_commande)
        
    return list_info_commande
