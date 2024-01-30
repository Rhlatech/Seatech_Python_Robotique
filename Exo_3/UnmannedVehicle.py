from Vehicle import *
from abc import ABCMeta, abstractmethod, ABC


class UnmannedVehicle(Vehicle,ABC):

    def __init__(self, name=" No named unmaned "):
        super().__init__(name)
    
    def mission(self):
        print("La mission est enclanché pour : {} ".format(super().name))

    @abstractmethod
    def activation(self):
        pass