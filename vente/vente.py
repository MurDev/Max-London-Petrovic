class Vente:
    quantite_vente = 0
    prix_gallon_gazoline = 250
    prix_gallon_diesel = 353
    
    def __init__(self, station, quantite_gallon_gazoline, quantite_gallon_diesel, date_vente):
        self.id_vente = Vente.quantite_vente + 1
        self.station = station
        self.quantite_gallon_gazoline = quantite_gallon_gazoline
        self.quantite_gallon_diesel = quantite_gallon_diesel
        self.date_vente = date_vente
        Vente.quantite_vente = Vente.quantite_vente + 1

    def prix_total_gazoline(self):
        return self.quantite_gallon_gazoline * Vente.prix_gallon_gazoline

    def prix_total_diesel(self):
        return self.quantite_gallon_diesel * Vente.prix_gallon_diesel

    def grand_total(self):
        return self.prix_total_gazoline() + self.prix_total_diesel()

    def afficher_detail_vente(self):
        print("\n**************************************************************")
        print("\nID vente ..............: ", self.id_vente)
        print("Date vente.............: ", self.date_vente)
        print("Station................: ", self.station)
        print("Prix gallon gazoline...: ", Vente.prix_gallon_gazoline, "HTG")
        print("Prix gallon diesel.....: ", Vente.prix_gallon_diesel, "HTG")
        print("Qte gallon gazoline....: ", self.quantite_gallon_gazoline)
        print("Qte gallon diesel......: ", self.quantite_gallon_diesel)
        print("\nPrix total gazoline....: ", self.prix_total_gazoline(), "HTG")
        print("Prix total diesel......: ", self.prix_total_diesel(), "HTG")
        print("\n----------------------- " )
        print("PRIX TOTAL.............: ", self.grand_total(), "HTG")
        print("\n**************************************************************")
    
    
    

    
