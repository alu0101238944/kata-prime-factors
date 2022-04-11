
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

  def test_a_big_prime_number_has_only_itself_as_prime_factor(self):
    big_prime_number = 104729
    self.assertEqual(self.prime_factors.factorize(big_prime_number), [big_prime_number])

  def test_big_coprime_integers_have_only_themselves_as_prime_factors(self):
    big_coprime_integers = [104717, 104723, 104729]
    self.assertEqual(self.prime_factors.factorize(numpy.prod(big_coprime_integers)), big_coprime_integers)

if __name__ == '__main__':
  unittest.main()
