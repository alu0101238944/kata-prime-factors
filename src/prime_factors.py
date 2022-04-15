
class PrimeFactors():
  def __init__(self, number):
    if number > 1:
      self.number = number
      self.needed_divisors = self.__compute_needed_divisors()
    else:
      raise ValueError('Numbers smaller than 2 have no prime factors')

  def __compute_needed_divisors(self):
    return [2]

  def get_prime_factors(self):
    number = self.number
    prime_factors = []
    i = 0
    while number > 1:
      current_divisor = self.needed_divisors[i]
      while number % current_divisor == 0:
        prime_factors.append(current_divisor)
        number /= current_divisor
      i += 1
    return prime_factors
