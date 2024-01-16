from Cyborg import *


# bob = Humane("Bob","M",["Banane", "Prune","Burger"])
# print(bob)
# bob.sexe = "F"
# bob.name = "Brigitte"
# bob.eat("Camembert")
# bob.digest()
# print(bob)

regis = Cyborg("Regis","F")

print(regis)
#regis.rechargement()
regis.eat("banana")
regis.digest()
print(regis.status())
regis.eat(["chicken","Coca"])
print(regis.status())