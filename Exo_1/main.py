from Robot import *





wall_e = Robot("wall_e", True, 150)
print(wall_e.name)

# Allume robot
wall_e.running()
print(wall_e)

#eteindre robot
wall_e.shutdown()
print(wall_e)
#wall_e.rechargement()
    
wall_e.current_speed = 50

# Allume robot
wall_e.running()

wall_e.running()

print("------------------")
wall_e.stop()

print(wall_e)