
export class PrimeFactors {
  factorize(n: number) {
    const primeFactors = [];

    if (n > 1) {
      const sqrtN = Math.floor(Math.sqrt(n));
      // divisors = [1, 3, 5, 7, 9, 11, ..., (sqrtN | sqrtN - 1)]
      const divisors = Array.from(Array(sqrtN).keys())
                            .filter((e: number) => e % 2 === 1);
      divisors.shift();     // Pop 1
      divisors.unshift(2);  // Push 2

      // divisor in range [2, 3, 5, 7, 9, 11, ..., (sqrtN | sqrtN - 1)]
      for (const divisor of divisors) {
        while (n % divisor === 0) {
          n /= divisor;
          primeFactors.push(divisor);
        }
      }
      if (n > 1) {
        primeFactors.push(n);
      }
    }

    return primeFactors;
  };
};
