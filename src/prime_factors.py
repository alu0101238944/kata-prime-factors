
class PrimeFactors():
  def __init__(self, n):
    if n > 1:
      self.n = n
    else:
      raise ValueError('Numbers smaller than 2 have no prime factors')

