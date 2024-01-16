from exo1_starter_template import *





wall_e = Robot("wall_e")
print(wall_e.name)

# Allume robot
wall_e.power = True
if(wall_e.power):
    print("allume")

#eteindre robot
wall_e.power = False
if(not wall_e.power):
    print("Eteindre")

wall_e.rechargement()
    
wall_e.current_speed = 50
# Allume robot
wall_e.power = True
if(wall_e.power):
    print("Allume")

print(wall_e)

wall_e.stop()

print(wall_e)