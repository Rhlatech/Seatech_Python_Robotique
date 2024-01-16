from Robot import *
from Humane import *
import time
import random

class Cyborg(Robot, Humane):
    
  # Constructeur
    def __init__(self, name, sex = "M"):
        Robot.__init__(self, name)
        Humane.__init__(self, name, sex)
  

    #Méthode qui va retourner toutes les info d'un cyborg sous format string
    def __str__(self):
        return "Nom du cyborg : {} / Sexe: {}".format(self.name, self.sexe)
    
    #Méthode qui va retourner toutes les info Robot et humain fusionne   
    def status(self):
        return (Robot.__str__(self)+ " // "+Humane.__str__(self))
    
    #Pti jeux sympa du cyborg
    def truc_fun(self):
        prix = random.randint(1, 10)
        score = 100
        tentatives = 0
        print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus.")
        while True:
            nombre = int(input())
            tentatives += 1
            if nombre < prix:
                print("Le just prix est plus haut")
            if nombre > prix:
                print("Le juste prix est plus bas")
            if nombre == prix:
                print("Félicitations, vous avez trouvé le juste prix {} en {} essais, votre score est {} !".format(prix, tentatives, int(score / tentatives)))
                print("Partie terminée")
                break
                