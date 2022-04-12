
import {PrimeFactors} from '../src/prime-factors';

const primeFactors = new PrimeFactors();

describe('Numbers smaller than the first prime number has no prime factors', () => {
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
});

describe('Prime number only have itself as prime factor', () => {
  test('Two has only itself as prime factor', () => {
    expect(primeFactors.factorize(2)).toEqual([2]);
  });
  test('Three has only itself as prime factor', () => {
    expect(primeFactors.factorize(3)).toEqual([3]);
  });
  test('Five has only itself as prime factor', () => {
    expect(primeFactors.factorize(5)).toEqual([5]);
  });
  test('Big prime number has only itself as prime factor', () => {
    expect(primeFactors.factorize(97379)).toEqual([97379]);
  });
  test('Huge prime number has only itself as prime factor', () => {
    expect(primeFactors.factorize(115648555991)).toEqual([115648555991]);
  });
});

describe('Composite number has its prime factors', () => {
  test('Four has two times the two as prime factors', () => {
    expect(primeFactors.factorize(4)).toEqual([2, 2]);
  });
  test('Six has two and three as prime factors', () => {
    expect(primeFactors.factorize(6)).toEqual([2, 3]);
  });
  test('Twelve has two times two and three as prime factors', () => {
    expect(primeFactors.factorize(12)).toEqual([2, 2, 3]);
  });
  test('Huge composite number has its prime factors', () => {
    expect(primeFactors.factorize(454884251)).toEqual([89,137,37307]);
  });
});
