# test_calculadora.py
#@uthor Luis Fernando José Miguel   ljosem@miumg.edu.gt


# Importamos el módulo unittest para crear y ejecutar las pruebas
import unittest

# Importamos la función sumar desde el archivo calculadora.py
from calculadora import sumar  

# Definimos una clase que contiene nuestras pruebas. 
# Esta clase debe heredar de unittest.TestCase para que unittest la reconozca como un conjunto de pruebas.
class TestCalculadora(unittest.TestCase):  
    """Clase de pruebas para la función sumar."""

    # Cada método de prueba debe comenzar con "test_" para que unittest lo reconozca como un test

    def test_suma_positivos(self):
        """Prueba la suma de dos números positivos."""
        resultado = sumar(2, 3)  # Llamamos a la función sumar con los valores 2 y 3
        self.assertEqual(resultado, 5)  # Verificamos que el resultado sea 5

    def test_suma_negativos(self):
        """Prueba la suma de dos números negativos."""
        resultado = sumar(-1, -2)  # Llamamos a la función sumar con -1 y -2
        self.assertEqual(resultado, -3)  # Verificamos que el resultado sea -3

    def test_suma_mixta(self):
        """Prueba la suma de un número positivo y uno negativo."""
        resultado = sumar(-1, 1)  # Llamamos a la función sumar con -1 y 1
        self.assertEqual(resultado, 0)  # Verificamos que el resultado sea 0

# Garantiza que si ejecutamos este archivo directamente, se ejecutarán los tests.
if __name__ == "__main__":
    unittest.main()
