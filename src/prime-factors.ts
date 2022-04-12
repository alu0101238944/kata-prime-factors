
export class PrimeFactors {
  factorize(n: number) {
    const primeFactors = [];
    if (n > 1) {
      const sqrtN = Math.floor(Math.sqrt(n));
      let divisor = 2;
      while (divisor <= sqrtN) {
        while (n % divisor === 0) {
          n /= divisor;
          primeFactors.push(divisor);
        }
        divisor++;
      }
      if (n > 1) {
        primeFactors.push(n);
      }
    }
    return primeFactors;
  };
};
