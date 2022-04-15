
import unittest
from src.prime_factors import PrimeFactors

class PrimeFactorsTest(unittest.TestCase):
  def test_numbers_smaller_than_2_have_no_prime_factors(self):
    for number in [-3, -2, -1, 0, 1]:
      self.assertRaises(ValueError, PrimeFactors, number)

  def test_first_prime_number_only_has_itself_as_prime_factor(self):
    self.assertEqual(PrimeFactors(2).get_prime_factors(), [2])

  def test_powers_of_two_has_only_twos_as_prime_factors(self):
    for power in range(1, 6):
      prime_factors_value = PrimeFactors(2 ** power).get_prime_factors()
      expected = [2] * power

      self.assertEqual(prime_factors_value, expected)

  def test_powers_of_three_has_only_threes_as_prime_factors(self):
    for power in range(1, 6):
      prime_factors_value = PrimeFactors(3 ** power).get_prime_factors()
      expected = [3] * power

      self.assertEqual(prime_factors_value, expected)

  def test_big_number_has_its_prime_factors(self):
    big_number = 7 * 11 * 17 # 1309
    self.assertEqual(PrimeFactors(big_number).get_prime_factors(), [7, 11, 17])
  
  def test_huge_number_has_its_prime_factors(self):
    big_number = 2 * 3 * 5 * 7 * 11 * 23 # 53130
    self.assertEqual(PrimeFactors(big_number).get_prime_factors(), [2,  3,  5,  7,  11,  23])

if __name__ == "__main__":
  unittest.main()
