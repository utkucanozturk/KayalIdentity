import unittest
from kayaEquation import *

class TestKayaEquation(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_result(self):
        actual = kayaEquation(pop=50, gdp=40, energy_intensity=100, carbon_intensity=0.05)
        expected = 50*40*100*0.05
        self.assertEqual(actual, expected)
    
    def test_valid_pop(self):
        actual = kayaEquation(pop=-50, gdp=40, energy_intensity=100, carbon_intensity=0.05)
        expected = -50*40*100*0.05
        self.assertEqual(actual, expected)
    
    def test_valid_gdp(self):
        actual = kayaEquation(pop=50, gdp=-40, energy_intensity=100, carbon_intensity=0.05)
        expected = 50*-40*100*0.05
        self.assertEqual(actual, expected)
    
    def test_output_C(self):
        actual = kayaEquation(pop=50, gdp=40, energy_intensity=100, carbon_intensity=0.05, output_type='C')
        expected = 50*40*100*0.05/3.67
        self.assertEqual(actual, expected)
    
    def test_valid_output(self):
        actual = kayaEquation(pop=50, gdp=40, energy_intensity=100, carbon_intensity=0.05, output_type='C_tonnes')
        expected = 50*40*100*0.05/3.67
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()