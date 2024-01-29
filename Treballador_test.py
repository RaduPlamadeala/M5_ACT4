import unittest
from Treballador import Treballador

class TreballadorTest(unittest.TestCase):
        #Aquest test prova si el programa detecta que volem assignar un nom
        #incorrecte i llença l'excepció que toca
        #Noteu que per als objectes individuals de la classe Treballador i
        #Exception podem triar els noms que ens done la gana,
        #no cal fer-los coincidir amb els de les classes"""
    def test_nom_treballador_incorrecte(self):
        
        treballador_meu = Treballador("pepe",1, 2000, 20 )
        with self.assertRaises(Exception) as test_meu:
            treballador_meu.set_nom("no")
        self.assertEqual(str(test_meu.exception), "El nom ha de tenir 3 o més caràcters")
    
    def test_nom_treballador_correcte(self):
        #Assignem un nom, com el mètode setNom pot produir excepcions ha d'anar en un
        #bloc try catch
        #A diferencia del cas anterior, aquí no estem provocant l'excepció a propòsit,
        #sino que és el tractament
        #habitual de les excepcions, ja ho veureu en M3"""
        nom_test = "Montsià"
        treballador = Treballador()
        #Si es produeix una excepcio, el bloc catch la captura i mostra per pantalla,
        #així el programa no peta
        try:
            treballador.set_nom(nom_test)
        except Exception as e:
            print(e.message)
            # L'assercio comprova que el nom és correcte i en cas contrari mostraria el
            #missatge d'error

        self.assertEqual(nom_test, treballador.get_nom(), "Els noms han de coincidir!!!")

    def test_nomina(self):
        nomina = 2300
        treballador = Treballador()
            #Assignem una nomina, com aquest mètode no provoca excepcions no necessitem el
            #bloc try-catch
            
        treballador.set_nomina(nomina)
        self.assertEqual(nomina, treballador.get_nomina(), "Els dos valors de la nomina han de coincidir!!!")
        #L'asserció comprova que la nomina és correcta i en cas contrari
        #mostra missatge d'error
        
        
    def test_hores_extres(self):
        hores_meu = 160
        treballador_meu = Treballador()
        treballador_meu.set_hores_extres(hores_meu)
        self.assertEqual(hores_meu, treballador_meu.get_hores_extres(), "Les hores han de coincidir!!!")
        
    def test_tipus_treballador_incorrecte(self):
        treballador_meu = Treballador("pepe",1, 2000, 20 )
        with self.assertRaises(Exception) as test_meu:
            treballador_meu.set_tipus_treballador("DIREKTOR")
        self.assertEqual(str(test_meu.exception), "Tipus de treballador no vàlid")
        
    def test_tipus_treballador_correcte(self):
        nom_test = "DIRECTOR"
        treballador = Treballador("pepe",1, 2000, 20 )
        try:
            treballador.set_tipus_treballador(nom_test)
        except Exception as e:
            print(e.message)
        self.assertEqual(nom_test, treballador.get_tipus_treballador())

        
        
if __name__ == '__main__':
    unittest.main()