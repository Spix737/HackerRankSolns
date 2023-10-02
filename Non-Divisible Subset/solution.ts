/*https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
 * Complete the 'nonDivisibleSubset' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY s
 *
 * Credit to Yash Pal @ programs.programmingoneonone.com
 */

function nonDivisibleSubset(k: number, s: number[]): number {

  let factorArray: number[] = new Array(k).fill(0)

  //For each integer add 1 to the index of it's remainder when int is divided by k.
  for (let i = 0; i < s.length; i += 1) {
    factorArray[s[i] % k] += 1;
  }
  let size = 0;

  for (let i = 0; i < Math.floor(k / 2) + 1; i++) {
    if (i == 0 || k == i * 2) {
      size += (factorArray[i] != 0) ? 1 : 0;
    } else {
      size += Math.max(factorArray[i], factorArray[k - i]);
    }
  }
  return (size);
}