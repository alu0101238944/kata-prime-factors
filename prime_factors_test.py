
import unittest
from src.prime_factors import PrimeFactors

class FizzBuzzTests(unittest.TestCase):
  def setUp(self):
    self.prime_factors = PrimeFactors()
    
  def test_one_has_no_prime_factors(self):
    self.assertEqual(self.prime_factors.factorize(1), [])

if __name__ == '__main__':
  unittest.main()
