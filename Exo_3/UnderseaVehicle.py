from UnmannedVehicle import *
from abc import ABCMeta, abstractmethod, ABC

class UnderseaVehicle(UnmannedVehicle,ABC):

    def __init__(self, name=" No named undersea "):
        super().__init__(name)
    
    def activation(self):
        print(" Activation véhicule sous-marin ")

    @abstractmethod
    def type_UnderSeaVehicle(self):
        pass