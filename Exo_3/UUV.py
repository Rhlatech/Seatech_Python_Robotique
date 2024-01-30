from UnderseaVehicle import *

class UUV(UnderseaVehicle):

    def __init__(self, name=" No named undersea "):
        super().__init__(name)

    def type_UnderSeaVehicle(self,type):
        print("Le type de sous-marin : "+ type)