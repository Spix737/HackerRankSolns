/* https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
 * Complete the 'nonDivisibleSubset' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY s
 * https://medium.com/@mrunankmistry52/non-divisible-subset-problem-comprehensive-explanation-c878a752f057
 */
//NOT WORKING RN AAA

function nonDivisibleSubsetNot(k: number, s: number[]): number {
  // Sick solution, credit to Mrunank Mistry
  let count: number[] = new Array(k).fill(0)

  for (let i = 0; i < s.length; i++) {
    let remainder: number = i % k
    count[remainder] += 1
  }

  //Handling cases where A%k + B%k = 0
  let ans: number = Math.min(count[0], 1)

  //Handling even exception case
  if (k % 2 == 0) {
    ans += Math.min(count[Math.floor(k / 2)], 1)
  }

  //Check for the pairs and take appropriate count
  for (let j = 1; j < Math.floor(k / 2) + 3; j++) {
    //Avoid over-counting when k is even
    if (j != k - j) {
      ans += Math.max(count[j], count[k - j])
    }
  }
  return ans
}