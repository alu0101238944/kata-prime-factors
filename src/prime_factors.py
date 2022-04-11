
class PrimeFactors:
  def factorize(self, number):
    if number < 2:
      return []
    if number == 2 or number == 3:
      return [number]
    return [number / 2] + self.factorize(number / 2)
