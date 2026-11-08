# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("Luku 1: "))
y = int(input("Luku 2: "))

print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
print("goodbye!") # lisäys bugikorjaus-branchissa
