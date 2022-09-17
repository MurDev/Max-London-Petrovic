import datetime
import os
from select import select
from station import *
from commande import *
from approvisionnement import *
from vente import *

dict_station = {}
liste_commande = []
set_approvisionnement = set()
liste_vente = []

zone1 = "Lalue"
zone2 = "Tabarre"
zone3 = "Clercine"
zone4 = "Petion-Ville"

def askForMenu():
    input("\nPresser la touche 'ENTER' pour afficher le menu principal ")

while 1 :
    choix_menu_principal = menuPrincipal()

    match choix_menu_principal :
        case 0 :    # Choix de quitter le programme
            print("Fin du programme...")
            break
        case 1 :    # Choix d'entrer dans le module 'STATION'
            choix_menu_station = menuStation()

            if choix_menu_station == 0 :   # Retour
                continue
            elif choix_menu_station == 1 : # Enregistrer une nouvelle station
                choix_zone = choixZone()

               #Controle si il n y a pas deja une station enregistrer dans une zone choisie 
                if choix_zone == 0 :
                    continue
                elif choix_zone == 1 and zone1 in dict_station :
                    print("\nL'enregistrement ne peut pas etre effectue, une station a ete deja enregistree a Lalue! ")
                    pass
                elif choix_zone == 2 and zone2 in dict_station :
                    print("\nL'enregistrement ne peut pas etre effectue, une station a ete deja enregistree a Tabarre! ")
                    pass
                elif choix_zone == 3 and zone3 in dict_station :
                    print("\nL'enregistrement ne peut pas etre effectue, une station a ete deja enregistree a Clercine! ")
                    pass
                elif choix_zone == 4 and zone4 in dict_station :
                    print("\nL'enregistrement ne peut pas etre effectue, une station a ete deja enregistree a Petion-Ville ! ")
                    pass
                else :
                    # Recuperer la capacite en gazoline et en diesel
                    print("\nEntrez la capacite en gazoline (gallons) : ")
                    capacite_gazoline = controle_nbre_gallon(100, 500)
                    print("\nEntrez la capacite en diesel (gallons)   : ")
                    capacite_diesel   = controle_nbre_gallon(100, 500)

                    if choix_zone == 1:     #Choix de la zone Lalue
                        new_station = Station(zone1, capacite_gazoline ,capacite_diesel)
                        dict_station[zone1] = new_station
                        print("\nEnregistrement effectue avec success ")

                    elif choix_zone == 2:     #Choix de la zone Tabarre
                        new_station = Station(zone2, capacite_gazoline ,capacite_diesel)
                        dict_station[zone2] = new_station
                        print("\nEnregistrement effectue avec success ")

                    elif choix_zone == 3:     #Choix de la zone Clercine
                        new_station = Station(zone3, capacite_gazoline ,capacite_diesel)
                        dict_station[zone3] = new_station
                        print("\nEnregistrement effectue avec success ")

                    elif choix_zone == 4:     #Choix de la zone Petion-Ville
                        new_station = Station(zone4, capacite_gazoline ,capacite_diesel)
                        dict_station[zone4] = new_station
                        print("\nEnregistrement effectue avec success ")
                    else:
                        pass
                    
            elif choix_menu_station == 2 :  # Modifier la quantite de gallon que peut contenir une station

                nom_zone = choixZone()

                if nom_zone == 0 :
                    continue
                elif nom_zone == 1 :
                    nom_zone = zone1
                elif nom_zone == 2 :
                    nom_zone = zone2
                elif nom_zone == 3 :
                    nom_zone = zone3
                elif nom_zone == 4 :
                    nom_zone = zone4
                else:
                    pass

                # Avant de modifier la capacite de la station, verfication de la quantite de gallons deja disponbible. 
                # La nouvelle capacite ne doit pas etre inferieure a la quantite de gallons deja disponible.

                if not nom_zone in dict_station:
                    print("\nStation",nom_zone,"n'est pas enregistree pour le moment")
                else:
                    type_essence = choix_type_essence()
                    nouvelle_capacite_gazoline = 0
                    nouvelle_capacite_diesel = 0

                    match type_essence :
                        case 0 :
                            pass
                        case 1 :
                            print("\nCapacite de gazoline actuelle de la station",nom_zone,": ",dict_station[nom_zone].capacite_gazoline,"gallon(s)")
                            print("Quantite de gazoline disponible  :",dict_station[nom_zone].quantite_gazoline_disponible,"galon(s)")
                            print("\nEntre la nouvelle capacite de gazoline ")
                            nouvelle_capacite_gazoline = controle_nbre_gallon(100, 500)
                            nouvelle_capacite_diesel = dict_station[nom_zone].capacite_diesel
                        case 2 :
                            print("\nEntre la nouvelle capacite de diesel ")
                            nouvelle_capacite_diesel = controle_nbre_gallon(100, 500)
                            nouvelle_capacite_gazoline = dict_station[nom_zone].capacite_gazoline
                        case 3 :
                            print("\nEntre la nouvelle capacite de gazoline ")
                            nouvelle_capacite_gazoline = controle_nbre_gallon(100, 500)
                            print("\nEntre la nouvelle capacite de diesel ")
                            nouvelle_capacite_diesel = controle_nbre_gallon(100, 500)
                        case _ :
                            pass
                    
                    if dict_station[nom_zone].quantite_gazoline_disponible > nouvelle_capacite_gazoline:
                        print("\nLa modification ne peut pas etre effectue, la quantite de gazoline disponible est superieure a la nouvelle capacite saisie!")
                        print("Quantite de gazoline disponible actuellement : ",dict_station[nom_zone].quantite_gazoline_disponible,"gallon(s)")
                    elif dict_station[nom_zone].quantite_diesel_disponible > nouvelle_capacite_diesel:
                        print("\nLa modification ne peut pas etre effectue, la quantite de diesel disponible est superieure a la nouvelle capacite saisie!")
                        print("Quantite de diesel disponible actuellement : ",dict_station[nom_zone].quantite_diesel_disponible,"gallon(s)")
                    else:
                        dict_station[nom_zone].modifier_capacite_gazoline(nouvelle_capacite_gazoline)
                        dict_station[nom_zone].modifier_capacite_diesel(nouvelle_capacite_diesel)
                        print("\nModification effectuee avec succes!")

            elif choix_menu_station == 3 :  # Afficher des informations sur toutes les stations
                if not dict_station:
                    print("\nAucune station enregistree pour le moment...")
                else:
                    print("\n------------------------------INFORMATION STATION---------------------------------\n")
                    for station in dict_station.values():
                        station.afficher_station()
            else:
                continue
            askForMenu()
        case 2 :    # Choix d'entrer dans le module 'COMMANDE'
            choix_menu_commande = menuCommande()

            if choix_menu_commande == 0 :   # Retour
                continue
            elif choix_menu_commande == 1 : # Generer et enregistrer une commande
                commande_en_attente = False

                for commande in liste_commande:
                    if commande.etat == "N":
                        commande_en_attente = True

                if commande_en_attente == False:
                    list_info_commande = genererCommande(dict_station)
                    choix_admin = list_info_commande[0]

                    if choix_admin == 0:
                        print("\nLa commande generee n'a pas ete confirme")
                    elif choix_admin == 1:
                        qte_gazoline_commande = list_info_commande[1]
                        qte_diesel_commande = list_info_commande[2]
                        current_time = datetime.datetime.now()
                        new_commande = (round(qte_gazoline_commande), round(qte_diesel_commande), current_time)
                        liste_commande.append(new_commande)
                        print("Une nouvelle commande a ete enregistree.")
                    else:
                        pass
                else:
                    print("\nUne commande deja en attente!")
                    print("Veuillez approvisionner les stations")
                
            elif choix_menu_commande == 2 : # Afficher toutes les commandes
                if not liste_commande:
                    print("Aucune commande enregistree pour le moment...")
                else:
                    print("\n___________________DETAIL COMMANDE_______________________\n")
                    for commande in liste_commande:
                        commande.afficher_detail_commande()
            else:
                continue
            askForMenu()
        case 3 :    # Choix d'entrer dans le module 'APPROVISIONNEMENT'
            choix_menu_approvisionnement = menuApprovisionnement()

            if choix_menu_approvisionnement == 0 :  # Retour
                continue
            elif choix_menu_approvisionnement == 1 : # Enregistrer et lancer un approvisionnement
                if not liste_commande:
                    print("Aucune commande enregistree pour le moment...")
                else:

                    n_commande = False
                    for commande in liste_commande:
                        if commande.etat == "N" :
                            n_commande = True
                            new_approvisionnement = Approvisionnement(commande.id_commande, commande.quantite_gallon_gazoline, commande.quantite_gallon_diesel, datetime.datetime.now())
                            set_approvisionnement.add(new_approvisionnement)
                            commande.etat = "P"
                            break

                    # Renflouement des stations
                    # Gazoline
                    if n_commande == True:
                        if new_approvisionnement.quantite_gallon_gazoline > 0:
                            for station in dict_station.values():
                                if station.pourcentage_gazoline_disponible() < 100:
                                    quantite_manquant = station.capacite_gazoline - station.quantite_gazoline_disponible
                                    station.quantite_gazoline_disponible = station.quantite_gazoline_disponible + quantite_manquant
                                    print("\n",station.nom_station, " a ete approvisionne de ",quantite_manquant,"gallons de gazoline avec success")

                        if new_approvisionnement.quantite_gallon_diesel > 0 : 
                            for station in dict_station.values():
                                if station.pourcentage_diesel_disponible() < 100:
                                    quantite_manquant = station.capacite_diesel - station.quantite_diesel_disponible
                                    station.quantite_diesel_disponible = station.quantite_diesel_disponible + quantite_manquant
                                    print("\n",station.nom_station, " a ete approvisionne de ",quantite_manquant,"gallons de diesel avec success")
                        
                    else:
                        print("\nAucune nouvelle commande!")
            
            elif choix_menu_approvisionnement == 2 : # Afficher tous les approvisionnements
                if not set_approvisionnement :
                    print("Aucun approvisionnement n'a ete enregistre")
                else:
                    for approvisionnement in set_approvisionnement:
                        approvisionnement.afficher_detail_approvisionnement()
            else:
                continue
            askForMenu()
        case 4 :    # Choix d'entrer dans le module 'VENTE'
            choix_menu_vente = menuVente()
            nom_station = ""
            nbre_de_gal_gazoline = 0
            nbre_de_gal_diesel = 0

            if choix_menu_vente == 0 : # Retour au menu principal
                clearScreen()
                continue
            elif choix_menu_vente == 1 : # Enregistrer une vente
                choix_de_la_station = choixZone()
                match choix_de_la_station :
                    case 0 :
                        continue
                    case 1 :
                        nom_station = zone1
                    case 2 :
                        nom_station = zone2
                    case 3 :
                        nom_station = zone3
                    case 4 :
                        nom_station = zone4
                    case _ :
                        pass
                
                if nom_station in dict_station:
                    choix_du_type_essence = choix_type_essence()
                    print("\n---------------------| TARIF D'ESSENCES |----------------------------")
                    if choix_du_type_essence == 1:  # Gazoline seulement
                        print("Gazoline......................", prix_essence("Gazoline"),"HTG par gallon")
                        print("\nQuantite gallons : ")
                        nbre_de_gal_gazoline = controle_nbre_gallon(1, 1000)
                        nbre_de_gal_diesel = 0
                    elif choix_du_type_essence == 2: # Diesel seulement
                        print("Diesel.........................", prix_essence("Diesel"),"HTG par gallon")
                        print("\nQuantite gallons : ")
                        nbre_de_gal_diesel = controle_nbre_gallon(1, 1000)
                        nbre_de_gal_gazoline = 0
                    elif choix_du_type_essence == 3 : # Gazoline et Diesel
                        print("Gazoline......................", prix_essence("Gazoline"), "HTG par gallon")
                        print("Diesel........................", prix_essence("Diesel"), "HTG par gallon")
                        
                        print("\nQuantite gallons gazoline : ")
                        nbre_de_gal_gazoline = controle_nbre_gallon(1, 1000)
                        print("\nQuantite gallons diesel: ")
                        nbre_de_gal_diesel = controle_nbre_gallon(1, 1000)
                    else:
                        continue 
                    
                    if nbre_de_gal_gazoline <= dict_station[nom_station].quantite_gazoline_disponible and nbre_de_gal_diesel <= dict_station[nom_station].quantite_diesel_disponible:
                        new_vente = Vente(nom_station, nbre_de_gal_gazoline, nbre_de_gal_diesel, datetime.datetime.now())
                        dict_station[nom_station].quantite_gazoline_disponible = dict_station[nom_station].quantite_gazoline_disponible - nbre_de_gal_gazoline
                        dict_station[nom_station].quantite_diesel_disponible = dict_station[nom_station].quantite_diesel_disponible - nbre_de_gal_diesel
                        liste_vente.append(new_vente)
                        print("\nLa vente a ete effectue avec succes!")
                        print("\n***********************| RECU |*******************************")
                        new_vente.afficher_detail_vente()
                        print("\n**************************************************************")
                    else:
                        print("\nLa quantite disponible a", nom_station ,"est insuffisante!")
                        print("-----------------| Essence disponible a", nom_station, "|------------------------")
                        print("Qte gazoline restante : ",dict_station[nom_station].quantite_gazoline_disponible,"gallon(s)")
                        print("Qte diesel restante   : ",dict_station[nom_station].quantite_diesel_disponible,"gallon(s)")
                else:
                    print("\nCette station n'est pas encore enregistree!")

            elif choix_menu_vente == 2 : # Afficher les ventes
                if not liste_vente :
                    print("\nAucune vente n'a ete effectue pour le moment!")
                else:
                    for vente in liste_vente:
                        vente.afficher_detail_vente()
            else :
                continue
            askForMenu()
        case _ :
            break