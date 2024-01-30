from GroundVehicle import *

class UGV(GroundVehicle):

    def __init__(self, name=" No named undersea "):
        super().__init__(name)

    def type_GroundVehicle(self,type):
        print("Le type de véhicue terrestre : "+ type)