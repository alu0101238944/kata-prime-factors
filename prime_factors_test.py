
import unittest
import numpy
from src.prime_factors import PrimeFactors

class FizzBuzzTests(unittest.TestCase):
  def setUp(self):
    self.prime_factors = PrimeFactors()
    
  def test_one_has_no_prime_factors(self):
    self.assertEqual(self.prime_factors.factorize(1), [])

  def test_two_has_only_itself_as_prime_factor(self):
    self.assertEqual(self.prime_factors.factorize(2), [2])

  def test_three_has_only_itself_as_prime_factor(self):
    self.assertEqual(self.prime_factors.factorize(3), [3])

  def test_four_has_two_twice_as_prime_factors(self):
    self.assertEqual(self.prime_factors.factorize(4), [2, 2])

  def test_product_of_prime_factors_of_a_number_matches_the_number(self):
    for i in range(1, 1000):
      result = self.prime_factors.factorize(i)
      self.assertEqual(i, numpy.prod(result))

  def test_fifty_has_two_and_five_twice_as_prime_factors(self):
    self.assertEqual(self.prime_factors.factorize(50), [2, 5, 5])
    
if __name__ == '__main__':
  unittest.main()
