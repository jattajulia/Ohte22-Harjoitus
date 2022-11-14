import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassapaate_luotu_oikein_(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat), (100000, 0, 0))
    
    def test_syo_edullisesti_kateisella_kun_raha_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.edulliset), ((100240), 60, 1))

    def test_syo_edullisesti_kateisella_kun_raha_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.edulliset), ((100000), 200, 0))

    def test_syo_maukkaasti_kateisella_kun_raha_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.maukkaat), ((100400), 100, 1))

    def test_syo_maukkaasti_kateisella_kun_raha_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual((self.kassapaate.kassassa_rahaa, vaihtoraha, self.kassapaate.maukkaat), ((100000), 200, 0))
    
    def test_syo_edullisesti_kortilla_kun_raha_riittaa(self):
        kortti = Maksukortti(300)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual((kortti.saldo, onnistui, self.kassapaate.edulliset, self.kassapaate.kassassa_rahaa), (60, True, 1, 100000))

    def test_syo_edullisesti_kortilla_kun_raha_ei_riita(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual((kortti.saldo, onnistui, self.kassapaate.edulliset, self.kassapaate.kassassa_rahaa), (200, False, 0, 100000))

    def test_syo_maukkaasti_kortilla_kun_raha_riittaa(self):
        kortti = Maksukortti(600)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual((kortti.saldo, onnistui, self.kassapaate.maukkaat, self.kassapaate.kassassa_rahaa), (200, True, 1, 100000))

    def test_syo_maukkaasti_kortilla_kun_raha_ei_riita(self):
        kortti = Maksukortti(200)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual((kortti.saldo, onnistui, self.kassapaate.maukkaat, self.kassapaate.kassassa_rahaa), (200, False, 0, 100000))
    
    def test_rahan_lataus_kortille_onnistuu(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual((kortti.saldo, self.kassapaate.kassassa_rahaa), (200, 100100))

    def test_negatiivisen_summan_lataus_kortille_ei_onnistu(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual((kortti.saldo, self.kassapaate.kassassa_rahaa), (100, 100000))
