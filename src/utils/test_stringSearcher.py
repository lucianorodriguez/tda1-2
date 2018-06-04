import unittest
from stringSearcher import *

class stringTest(unittest.TestCase):
    
    def test_kmp_armar_tabla_simple_funciona(self):
        string = "ABCDABD"
        self.assertEquals(armar_tabla_de_falla(string), [-1,0,0,0,-1,0,2])
        
    def test_kmp_armar_tabla_menos_simple_funciona(self):
        string = "ABACABABC"
        self.assertEquals(armar_tabla_de_falla(string), [-1,0,-1,1,-1,0,-1,3,2])
        
    def test_kmp_search_simple_encuentra_substring(self):
        patron = "ABC"
        texto = "BABDABABC"
        self.assertTrue(search_kmp(patron, texto), "Fallo al encontrar patron en caso simple")
        
    def test_kmp_search_simple_no_encuentra_substring(self):
        patron = "ABC"
        texto = "ADABDDAACBCBABD"
        self.assertFalse(search_kmp(patron, texto), "Fallo al no encontrar patron en caso simple")
    
    def test_kmp_search_complejo_encuentra_substring(self):
        patron = "ABACABABC"
        texto = "ABAABACABABACABACABABCD"
        self.assertTrue(search_kmp(patron, texto), "Fallo al encontrar patron en caso complejo")
    
    def test_kmp_search_complejo_no_encuentra_substring(self):
        patron = "ABACABABC"
        texto = "ABAABACABABACABACABABACD"
        self.assertFalse(search_kmp(patron, texto), "Fallo al no encontrar patron en caso complejo")
        
    def test_kmp_search_complejo_2_no_encuentra_substring(self):
        patron = "ABACABABC"
        texto = "CABABCABACAACABABCBCACAABACABCABCABBCABCBABACABABABABAACABADBC"
        self.assertFalse(search_kmp(patron, texto), "Fallo al no encontrar patron en caso complejo")