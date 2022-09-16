class Station:
    def __init__(self, nom_station, capacite_gazoline, capacite_diesel):
        self.nom_station = nom_station
        self.capacite_gazoline = capacite_gazoline
        self.capacite_diesel = capacite_diesel
        self.quantite_gazoline_disponible = 0
        self.quantite_diesel_disponible = 0

    def modifier_quantite_gazoline_disponible(self, nouvelle_quantite):
        if nouvelle_quantite <= 0 :
            self.quantite_gazoline_disponible = 0
        else:
            self.quantite_gazoline_disponible = nouvelle_quantite

    def modifier_quantite_diesel_disponible(self, nouvelle_quantite):
        if nouvelle_quantite <= 0:
            self.quantite_diesel_disponible = 0
        else:
            self.quantite_diesel_disponible = nouvelle_quantite

    def modifier_capacite_gazoline(self, nouvelle_capacite):
        self.capacite_gazoline = nouvelle_capacite
    
    def modifier_capacite_diesel(self, nouvelle_capacite):
        self.capacite_diesel = nouvelle_capacite

    def pourcentage_gazoline_disponible(self):
        return (self.quantite_gazoline_disponible * 100) / self.capacite_gazoline
    
    def pourcentage_diesel_disponible(self):
        return (self.quantite_diesel_disponible * 100) / self.capacite_diesel

    def pourcentage_gazoline_utilise(self):
        return ((self.capacite_gazoline - self.quantite_gazoline_disponible) * 100) / self.capacite_gazoline

    def pourcentage_diesel_utilise(self):
        return ((self.capacite_diesel - self.quantite_diesel_disponible) * 100) / self.capacite_diesel
    
    def afficher_station(self):
        print("Nom                              : ", self.nom_station)
        print("Gazoline disposnible             : ", self.quantite_gazoline_disponible, " gallon(s)")
        print("Diesel disponible                : ", self.quantite_diesel_disponible, " gallon(s)")
        print("Capacite en Gazoline             : ", self.capacite_gazoline, " gallon(s)")
        print("Capacite en Diesel               : ", self.capacite_diesel, " gallon(s)")
        print("Pourcentage Gazoline disponible  : ", self.pourcentage_gazoline_disponible(), "%")
        print("Pourcentage Gazoline utilise     : ", self.pourcentage_gazoline_utilise(), "%")
        print("Pourcentage Diesel disponible    : ", self.pourcentage_diesel_disponible(), "%")
        print("Pourcentage Diesel utilise       : ", self.pourcentage_diesel_utilise(), "%")
        print("\n------------------------------------------------------------------------------------n")

