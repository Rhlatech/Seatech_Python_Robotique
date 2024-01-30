from AerialVehicle import *

class UAV(AerialVehicle):

    def __init__(self, name=" No named undersea "):
        super().__init__(name)

    def type_AerialVehicle(self,type):
        print("Le type de véhicue  aérien : "+ type)