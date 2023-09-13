'''
    Practica de Testing ;)
'''

import unittest
from Biseccion import biseccion, funcion_ejemplo

class TestBiseccion(unittest.TestCase):
    def test_biseccion(self):
        # Prueba el algoritmo de bisección con la función de ejemplo
        raiz_aproximada = biseccion(funcion_ejemplo, 0, 5, 100)
        self.assertAlmostEqual(raiz_aproximada, 0.7 , places=1) # Comprueba si la raíz es aproximadamente 0 con 6 decimales de precisión



if __name__ == '__main__':
    unittest.main()
