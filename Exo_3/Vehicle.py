from abc import ABCMeta, abstractmethod

class Vehicle(metaclass=ABCMeta):
    __name = "<unnamed>"
    
    def __init__(self, name=" No named "):
        self.__name = name
  
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

    
    @abstractmethod
    def mission(self, name):
        pass

  #Méthode qui va retourner toutes les info d'un robot sous format string
    def __str__(self):
        return "Nom du véhicule : {} ".format(self.name)