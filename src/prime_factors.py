
from math import sqrt, floor

class PrimeFactors:
  def factorize(self, number):
    if number < 2:
      return []
    for divisor in [2] + list(range(3, floor(sqrt(number)), 2)):
      if number % divisor == 0:
        quotient = number // divisor
        if quotient != 1:
          return [quotient] + self.factorize(divisor)
        else:
          return [number]
    return [number]
