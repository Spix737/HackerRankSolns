/* https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true
 * Complete the 'serviceLane' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY cases
 */

function serviceLane(n: number, cases: number[][], t: number, width: number[]): number[] {
  // Good implementation, requires editing the problem to pass in extra parameters (width)
  let safeWidth: number[] = [];
  for (let i = 0; i < t; i++) {
    let maxW: number = Math.max(...width);
    for (let j = cases[i][0]; j < cases[i][1] + 1; j++) {
      if (width[j] < maxW) {
        maxW = width[j]
      }
    }
    safeWidth.push(maxW)
  }
  return safeWidth
}