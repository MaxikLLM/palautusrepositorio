# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("Luku 1: "))
y = int(input("Luku 2: "))

print(f"Lukujen {x} ja {y} summa on {summa(x, y)}")
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}")
print(f"Lukujen {x} ja {y} tulo on {tulo(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!")
