from UnmannedVehicle import *
from abc import ABCMeta, abstractmethod, ABC

class AerialVehicle(UnmannedVehicle,ABC):


    def __init__(self, name=" No named aerial "):
        super().__init__(name)
    
    def activation(self):
        print(" Activation véhicule sous-aérien ")


    @abstractmethod
    def type_AerialVehicle(self):
        pass