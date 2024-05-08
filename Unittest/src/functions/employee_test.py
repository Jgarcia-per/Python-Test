import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    # Al inicio de todo
    @classmethod
    def setUpClass(cls):
        print('Set Up Class\n')
    
    # Despues de todo
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # Antes de cada función
    def setUp(self):
        print(' SetUp')
        self.emp_1 = Employee('Juan', 'Garcia', 50000)
        self.emp_2 = Employee('Pedro', 'Mapache', 60000)

    # Después de cada función
    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('Test Email')
        self.assertEqual(self.emp_1.email, 'Juan.Garcia@email.com')
        self.assertEqual(self.emp_2.email, 'Pedro.Mapache@email.com')

        self.emp_1.first = 'Manuel'
        self.emp_2.first = 'Cheems'

        self.assertEqual(self.emp_1.email, 'Manuel.Garcia@email.com')
        self.assertEqual(self.emp_2.email, 'Cheems.Mapache@email.com')

    def test_fullname(self):
        print('Test Fullname')
        self.assertEqual(self.emp_1.fullname, 'Juan Garcia')
        self.assertEqual(self.emp_2.fullname, 'Pedro Mapache')

        self.emp_1.first = 'Manuel'
        self.emp_2.first = 'Cheems'

        self.assertEqual(self.emp_1.fullname, 'Manuel Garcia')
        self.assertEqual(self.emp_2.fullname, 'Cheems Mapache')
    
    def test_apply_raise(self):
        print('Test Raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

# Para ahorrarnos tiempo al ejecutar podemos añadir
if __name__ == '__main__':
    unittest.main()