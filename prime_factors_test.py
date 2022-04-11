
import unittest
from src.prime_factors import PrimeFactors

class FizzBuzzTests(unittest.TestCase):
  def setUp(self):
    self.prime_factors = PrimeFactors()
    
  def test_one_has_no_prime_factors(self):
    self.assertEqual(self.prime_factors.factorize(1), [])

  def test_two_has_only_itself_as_prime_factor(self):
    self.assertEqual(self.prime_factors.factorize(2), [2])

if __name__ == '__main__':
  unittest.main()
