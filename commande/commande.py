class Commande:
    quantite_commande = 0
    def __init__(self, quantite_gallon_gazoline, quantite_gallon_diesel, date_commande):
        self.id_commande = Commande.quantite_commande + 1
        self.quantite_gallon_gazoline = quantite_gallon_gazoline
        self.quantite_gallon_diesel = quantite_gallon_diesel
        self.date_commande = date_commande
        self.etat = "N"
        Commande.quantite_commande = Commande.quantite_commande + 1
    
    def changer_etat(self, nouveau_etat):
        self.etat = nouveau_etat

    def afficher_detail_commande(self):
        print("ID commande...................: ", self.id_commande)
        print("Quantite gazoline.............: ", self.quantite_gallon_gazoline,"gallon(s)")
        print("Quantite diesel...............: ", self.quantite_gallon_diesel,"gallon(s)")
        print("Date de la commande...........: ", self.date_commande)
        print("Etat de la commande...........: ", self.etat)
        print("\n__________________________________________________________\n")