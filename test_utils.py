# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(6),720)
        self.assertEqual(utils.fact(0),0)
    
    def test_roots(self):
        self.assertEqual(utils.roots(5,1,1),"Racine négative")
        
    def test_integrate(self):
        self.assertEqual(utils.integrate(0,5,6),"Réussi")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
