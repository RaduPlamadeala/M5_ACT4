class Treballador:
    BASE = 1
    DIRECTOR = "DIRECTOR"
    SUBDIRECTOR = "SUBDIRECTOR"
    
    def __init__(self, nom="", tipus=BASE, nomina=0.0, hores=0):
        self.nomTreballador = nom
        self.tipusTreballador = tipus
        self.nominaTreballador = nomina
        self.horesExtresTreballador = hores

    def set_nom(self, nom):
        if len(nom) < 3:
            raise Exception("El nom ha de tenir 3 o més caràcters")
        self.nomTreballador = nom

    def get_nom(self):
        return self.nomTreballador

    def set_nomina(self, euros):
        self.nominaTreballador = euros

    def get_nomina(self):
        return self.nominaTreballador

    def set_hores_extres(self, hores):
        self.horesExtresTreballador = hores

    def get_hores_extres(self):
        return self.horesExtresTreballador

    def set_tipus_treballador(self, tipus):
        if tipus in [self.DIRECTOR, self.SUBDIRECTOR, self.BASE]:
            self.tipusTreballador = tipus
        else:
            raise Exception("Tipus de treballador no vàlid")

    def get_tipus_treballador(self):
        return self.tipusTreballador