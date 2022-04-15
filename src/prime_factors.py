
class PrimeFactors():
  def __init__(self, number):
    if number > 1:
      self.number = number
    else:
      raise ValueError('Numbers smaller than 2 have no prime factors')

