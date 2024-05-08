import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-10, 5), -5)
        self.assertEqual(calc.add(-10, -10), -20)
        self.assertEqual(calc.add(-10, 10), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-10, 5), -15)
        self.assertEqual(calc.subtract(-10, -10), 0)
        self.assertEqual(calc.subtract(-10, 10), -20)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-10, 5), -50)
        self.assertEqual(calc.multiply(-10, -10), 100)
        self.assertEqual(calc.multiply(-10, 10), -100)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-10, 5), -2)
        self.assertEqual(calc.divide(-10, -10), 1)
        self.assertEqual(calc.divide(-10, 10), -1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # Provocamos un error esperado
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # Cuando tenemos que dejar pasar muchos errores esperados, es mejor usar un administrador de contexto
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

# Para ahorrarnos tiempo al ejecutar podemos añadir
if __name__ == '__main__':
    unittest.main()