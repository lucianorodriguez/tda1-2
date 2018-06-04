import unittest
from rotacion_ciclica import *


class RotacionTest(unittest.TestCase):
    
    def test_rotacion_fuerza_bruta_simple_matchea(self):
        original = "ABRACADABRA"
        rotado = "DABRAABRACA"
        self.assertTrue(es_rotacion_fuerza_bruta(original,rotado), "Fallo fuerza bruta simple matchea")
    
    def test_rotacion_fuerza_bruta_simple_no_matchea(self):
        original = "ABRACADABRA"
        rotado = "DABRAABRADA"
        self.assertFalse(es_rotacion_fuerza_bruta(original,rotado), "Fallo fuerza bruta simple no matchea")
        
    def test_rotacion_fuerza_bruta_simple_no_matchea_borde(self):
        original = "ABRACADABRA"
        rotado = "DABRRABRACA"
        self.assertFalse(es_rotacion_fuerza_bruta(original,rotado), "Fallo fuerza bruta simple no matchea ultimo caracter")
        
    def test_rotacion_fuerza_bruta_simple_largos_distintos(self):
        original = "ABRACADABRA"
        rotado = "DABRAAABRACA"
        self.assertFalse(es_rotacion_fuerza_bruta(original,rotado), "Fallo fuerza bruta simple largos distintos")
        
    ############ rotacion ciclica con kmp ############
    def test_rotacion_kmp_simple_matchea(self):
        original = "ABRACADABRA"
        rotado = "DABRAABRACA"
        self.assertTrue(es_rotacion_kmp(original,rotado), "Fallo kmp simple matchea")
    
    def test_rotacion_kmp_simple_no_matchea(self):
        original = "ABRACADABRA"
        rotado = "DABRAABRADA"
        self.assertFalse(es_rotacion_kmp(original,rotado), "Fallo kmp simple no matchea")
        
    def test_rotacion_kmp_simple_no_matchea_borde(self):
        original = "ABRACADABRA"
        rotado = "DABRRABRACA"
        self.assertFalse(es_rotacion_kmp(original,rotado), "Fallo kmp simple no matchea ultimo caracter")
        
    def test_rotacion_kmp_simple_largos_distintos(self):
        original = "ABRACADABRA"
        rotado = "DABRAAABRACA"
        self.assertFalse(es_rotacion_kmp(original,rotado), "Fallo kmp simple largos distintos")
    
    ############ rotacion ciclica con kmp optimizado ############    
    def test_rotacion_kmp_optimizado_simple_matchea(self):
        original = "ABRACADABRA"
        rotado = "DABRAABRACA"
        self.assertTrue(es_rotacion_kmp_optimizado(original,rotado), "Fallo kmp optimizado simple matchea")
    
    def test_rotacion_kmp_optimizado_simple_no_matchea(self):
        original = "ABRACADABRA"
        rotado = "DABRAABRADA"
        self.assertFalse(es_rotacion_kmp_optimizado(original,rotado), "Fallo kmp optimizado simple no matchea")
        
    def test_rotacion_kmp_optimizado_simple_no_matchea_borde(self):
        original = "ABRACADABRA"
        rotado = "DABRRABRACA"
        self.assertFalse(es_rotacion_kmp_optimizado(original,rotado), "Fallo kmp optimizado simple no matchea ultimo caracter")
        
    def test_rotacion_kmp_optimizado_simple_largos_distintos(self):
        original = "ABRACADABRA"
        rotado = "DABRAAABRACA"
        self.assertFalse(es_rotacion_kmp_optimizado(original,rotado), "Fallo kmp optimizado simple largos distintos")