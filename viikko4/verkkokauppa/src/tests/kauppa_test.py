import unittest
from unittest.mock import Mock, call

from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        self.saldot = {1: 10}
        self.tuotteet = {1: Tuote(1, "maito", 5)}
        self.varasto_mock.saldo.side_effect = self.saldot.get
        self.varasto_mock.hae_tuote.side_effect = self.tuotteet.get
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostos_pankin_metodia_tilisiirto_oikea(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_ostos_pankin_metodia_tilisiirto_oikea_kun_2_eri_tuotetta(self):
        self.saldot[2] = 5
        self.tuotteet[2] = Tuote(2, "vesi", 2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 7
        )

    def test_ostos_pankin_metodia_tilisiirto_oikea_kun_2_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_ostos_pankin_metodia_tilisiirto_oikea_kun_2_eri_tuotetta_ja_1_puuttuu(self):
        self.saldot[2] = 0
        self.tuotteet[2] = Tuote(2, "vesi", 2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_aloita_asiointi_kutsuminen_nollaa_edelisen_ostoksen_tiedot(self):
        self.saldot[2] = 0
        self.tuotteet[2] = Tuote(2, "vesi", 2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        expected = [call("pekka", 42, "12345", "33333-44455", 5), 
                    call("pekka", 42, "12345", "33333-44455", 0)]

        self.assertEqual(self.pankki_mock.tilisiirto.call_args_list, expected)

    def test_kauppa_pyytä_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        expected = [call("pekka", 42, "12345", "33333-44455", 5), 
                            call("pekka", 43, "12345", "33333-44455", 5)]

        self.assertEqual(self.pankki_mock.tilisiirto.call_args_list, expected)

    def test_poista_korista_poistaa_tuotte(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 0)


