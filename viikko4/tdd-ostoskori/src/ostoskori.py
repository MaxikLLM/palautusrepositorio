from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tavaroita = 0
        self._hinta = 0
        self._ostos = None

    def tavaroita_korissa(self):
        return self._tavaroita

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._tavaroita += 1
        self._hinta += lisattava.hinta()
        if self._tavaroita == 1:
            self._ostos = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        pass

    def tyhjenna(self):
        pass

    def ostokset(self):
        return [self._ostos] if self._tavaroita == 1 else []
