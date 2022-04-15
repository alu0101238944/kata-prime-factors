
class PrimeFactors():
  def __init__(self, number):
    if number > 1:
      self.number = number
      self.needed_divisors = self.__compute_needed_divisors()
    else:
      raise ValueError('Numbers smaller than 2 have no prime factors')

  def __compute_needed_divisors(self):
    return [self.number]

  def get_prime_factors(self):
    return self.needed_divisors
