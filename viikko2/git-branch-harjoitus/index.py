# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("Luku 1: "))
y = int(input("Luku 2: "))

<<<<<<< HEAD
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}") # muutos mainissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}") # muutos mainissa
=======
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}") # muutos mainissa
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}") # muutos mainissa
>>>>>>> bugikorjaus

logger("lopetetaan ohjelma")
print("goodbye!")
