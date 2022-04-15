
class PrimeFactors():
  def __init__(self, number):
    if number > 1:
      self.number = number
      self.needed_divisors = self.__compute_needed_divisors()
    else:
      raise ValueError('Numbers smaller than 2 have no prime factors')

  def __compute_needed_divisors(self):
    needed_primes = [2]
    for divisor in range(3, self.number + 1, 2):
      divisor_is_prime = True
      for prime in needed_primes:
        if divisor % prime == 0:
          divisor_is_prime = False
          break
      if divisor_is_prime:
        needed_primes.append(divisor)
    return needed_primes

  def get_prime_factors(self):
    number = self.number
    prime_factors = []
    i = 0
    while number > 1 and i < len(self.needed_divisors):
      current_divisor = self.needed_divisors[i]
      while number % current_divisor == 0:
        prime_factors.append(current_divisor)
        number /= current_divisor
      i += 1
    return prime_factors
