
import {PrimeFactors} from '../src/prime-factors';

const primeFactors = new PrimeFactors();

describe('Base cases', () => {
  test('Negative numbers do not have prime factors', () => {
    expect(primeFactors.factorize(-1)).toEqual([]);
    expect(primeFactors.factorize(-2)).toEqual([]);
    expect(primeFactors.factorize(-3)).toEqual([]);
  });
  test('Zero has no prime factors', () => {
    expect(primeFactors.factorize(0)).toEqual([]);
  });
  test('One has no prime factors', () => {
    expect(primeFactors.factorize(1)).toEqual([]);
  });
  test('Two has only itself as prime factor', () => {
    expect(primeFactors.factorize(2)).toEqual([2]);
  });
  test('Three has only itself as prime factor', () => {
    expect(primeFactors.factorize(3)).toEqual([3]);
  });
});
