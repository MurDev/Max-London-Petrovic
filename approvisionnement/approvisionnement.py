class Approvisionnement:
    quantite_approvisionnement = 0
    def __init__(self, id_commande, quantiite_gallon_gazoline, quantite_gallon_diesel, date_approvisionnement):
        self.id_approvisionnement = Approvisionnement.quantite_approvisionnement + 1
        self.id_commande = id_commande
        self.quantite_gallon_gazoline = quantiite_gallon_gazoline
        self.quantite_gallon_diesel = quantite_gallon_diesel
        self.date_approvisionnement = date_approvisionnement
        Approvisionnement.quantite_approvisionnement = Approvisionnement.quantite_approvisionnement + 1

    def afficher_detail_approvisionnement(self):
        print("------------------| DETAILS APPROVISIONNEMENT |--------------------------")
        print("ID approvisionnement     : ", self.id_approvisionnement)
        print("Id de la commande        : ", self.id_commande)
        print("Quantite gallon gazoline : ", self.quantite_gallon_gazoline)
        print("Quantite gallon diesel   : ", self.quantite_gallon_diesel)
        print("Date                     : ", self.date_approvisionnement)

    