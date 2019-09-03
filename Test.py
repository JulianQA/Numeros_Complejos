import unittest
import NumerosComplejos

class TestmyFunctions(unittest.TestCase):
    def testadd(self):
        a = (1,2)
        b = (1,3)
        esperado = (2,5)
        res = NumerosComplejos.suma(a,b)
        self.assertEqual(esperado,res)
    def testsubs(self):
        a = (1, 2)
        b = (1, 3)
        esperado = (0, -1)
        res = NumerosComplejos.resta(a, b)
        self.assertEqual(esperado, res)

    def testmulti(self):
        a = (1, 2)
        b = (1, 3)
        esperado = (-5, 5)
        res = NumerosComplejos.multiplicacion(a, b)
        self.assertEqual(esperado, res)
    def testdivision(self):
        a = (1, 2)
        b = (1, 3)
        esperado = (0.7, -0.1)
        res = NumerosComplejos.division(a, b)
        self.assertEqual(esperado, res)
    def testconju(self):
        a = (1, 2)
        esperado = (1, -2)
        res = NumerosComplejos.conju(a)
        self.assertEqual(esperado, res)
    def testmodulo(self):
        a = (1, 2)
        esperado = 2.24
        res = NumerosComplejos.modulo(a)
        self.assertEqual(esperado, res)
    def testfase(self):
        a = (1, 2)
        esperado = 63.43
        res = NumerosComplejos.fase(a)
        self.assertEqual(esperado, res)
    def testpolar(self):
        a = (1, 2)
        esperado = (2.24,63.43)
        res = NumerosComplejos.polar(a)
        self.assertEqual(esperado, res)
    def testcarte(self):
        a = (2.24, 1.1071487177940904)
        esperado = (1,2)
        res = NumerosComplejos.cartesiano(a)
        self.assertEqual(esperado, res)
    def testsumvectores(self):
        a = [(1,2),(2,1)]
        b = [(1,3),(3,1)]
        esperado = [(2,5),(5,2)]
        res = NumerosComplejos.suma_vectores(a, b)
        self.assertEqual(esperado, res)
    def testinvectores(self):
        a = [(1,2),(2,1)]
        esperado = [(-1,-2),(-2,-1)]
        res = NumerosComplejos.inversa_vectores(a)
        self.assertEqual(esperado, res)
    def testsumvectores(self):
        a = 3
        b = [(1,2),(3,1)]
        esperado = [(3,6),(9,3)]
        res = NumerosComplejos.multi_escalar_vec(a, b)
        self.assertEqual(esperado, res)
    def testsumamatriz(self):
        a = [[(1,2)],[(2,1)]]
        b = [[(3,1)],[(1,3)]]
        esperado = [[(4,3)], [(3,4)]]
        res = NumerosComplejos.suma_matrices(a,b)
        self.assertEqual(esperado,res)
    def testmultimatriz(self):
        a = 3
        b = [[(1,2)],[(3,3)],[(1,1)]]
        esperado = [[(3,6)], [(9,9)], [(3,3)]]
        res = NumerosComplejos.multi_matrices(a,b)
        self.assertEqual(esperado,res)
    def testtranspuesta(self):
        a = [[(1,2),(2,3),(1,5)],[(3,2),(6,8),(1,2)],[(2,1),(2,3),(2,5)]]
        esperado = [[(1, 2), (3, 2), (2, 1)], [(2, 3), (6, 8), (2, 3)], [(1, 5), (1, 2), (2, 5)]]
        res = NumerosComplejos.transpuesta(a)
        self.assertEqual(esperado,res)
    def testinversa(self):
        a = [[(1,2)],[(3,3)],[(1,1)]]
        esperado = [[(-1, -2)], [(-3, -3)], [(-1, -1)]]
        res = NumerosComplejos.inver_matriz(a)
        self.assertEqual(esperado,res)
    def testcojugada(self):
        a = [[(-1, -2)], [(-3, -3)], [(-1, -1)]]
        esperado = [[(-1, 2)], [(-3, 3)], [(-1, 1)]]
        res = NumerosComplejos.mat_conjugada(a)
        self.assertEqual(esperado,res)
    def testadjunta(self):
        a = [[(5,0),(4,5)],[(4,-5),(13,0)]]
        esperado = [[(5,0),(4,5)],[(4,-5),(13,0)]]
        res = NumerosComplejos.mat_adjunta(a)
        self.assertEqual(esperado,res)
    def testhermitian(self):
        a = [[(5,0),(4,5)],[(4,-5),(13,0)]]
        esperado = True
        res = NumerosComplejos.hermitian(a)
        self.assertEqual(esperado,res)
    def testnorma(self):
        a = [[(3,2),(4,2),(7,1)]]
        esperado = 9.11
        res = NumerosComplejos.norma(a)
        self.assertEqual(esperado,res)
    def testnorma(self):
        a = [(3,0),(4,0),(7,0)]
        b = [(-1,0),(2,0)]
        esperado = [(-3, 0), (6, 0), (-4, 0), (8, 0), (-7, 0), (14, 0)]
        res = NumerosComplejos.producto_tensor_vector(a,b)
        self.assertEqual(esperado,res) 
    
        
        
if __name__ == '__main__':
    unittest.main()
