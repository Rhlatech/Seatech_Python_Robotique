from UUV import *
from UGV import *
from UAV import *



wall_e_normal = UGV(" wall_e ")
wall_e_normal.activation()
wall_e_normal.mission()
wall_e_under_water = UUV("wall_e under water ")
wall_e_under_water.activation()
wall_e_under_water.mission()
wall_e_aérien = UAV("wall_e flying ")
wall_e_aérien.activation()
wall_e_aérien.mission()
wall_e_aérien.type_AerialVehicle(" DRONE ")

