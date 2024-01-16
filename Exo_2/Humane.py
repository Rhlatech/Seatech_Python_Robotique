import time, sys

class Humane():
    __name = "<unnamed>"
    __sexe = "M"
    __food = ["Rien"]
    
  # Constructeur
    def __init__(self, name, sex = "M", foods = ["Rien"]):
        self.name = name
        self.sexe = sex
        self.food = foods
  
  ### Get/Set ###
  # Name getter function 
    @property
    def name(self): 
         #print("getter method called") 
         return self.__name
       
  # Name setter function 
    @name.setter
    def name(self, a): 
         #print("setter method called") 
         self.__name = a 

  # Sexe getter function 
    @property
    def sexe(self):
        #print("getter method called")
        return self.__sexe
       
  # Sexe setter function 
    @sexe.setter
    def sexe(self, a): 
        #print("setter method called")
        if(a == "M" or a == "F"):
           self.__sexe = a
        else : print(" Wrong value set for the sex either M or F")

  # Food getter function 
    @property
    def food(self): 
         #print("getter method called") 
         return self.__food

  # Food setter function 
    @food.setter
    def food(self, a): 
         #print("setter method called") 
         self.__food = a
    
    def eat(self,a = []):
        #print(" Eats method called")
        if type(a) == list:
            self.food = a
        elif type(a) == str:
            self.food.append(a)
    
    def digest(self):
         self.food.remove(self.food[0])

  #Méthode qui va retourner toutes les info d'un robot sous format string
    def __str__(self):
        return "Nom de l'humain : {} / Sexe: {} / Foods : {}".format(self.name, self.sexe, self.food)