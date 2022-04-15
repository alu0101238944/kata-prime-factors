
import unittest
from src.prime_factors import PrimeFactors

class PrimeFactorsTest(unittest.TestCase):
  def test_numbers_smaller_than_2_have_no_prime_factors(self):
    for number in [-3, -2, -1, 0, 1]:
      self.assertRaises(ValueError, PrimeFactors, number)

if __name__ == "__main__":
  unittest.main()
