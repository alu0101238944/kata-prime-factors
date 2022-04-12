
import {PrimeFactors} from '../src/prime-factors';

const primeFactors = new PrimeFactors();

describe('Base cases', () => {
  test('Negative numbers do not have prime factors', () => {
    expect(primeFactors.factorize(-1)).toEqual([]);
    expect(primeFactors.factorize(-2)).toEqual([]);
    expect(primeFactors.factorize(-3)).toEqual([]);
  });
});
