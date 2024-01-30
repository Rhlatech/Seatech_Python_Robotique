from abc import ABCMeta, abstractmethod, ABC
from UnmannedVehicle import *

class GroundVehicle(UnmannedVehicle,ABC):

    def __init__(self, name=" No named ground "):
        super().__init__(name)
    
    def activation(self):
        print(" Activation véhicule terrestre ")

    @abstractmethod
    def type_GroundVehicle(self):
        pass