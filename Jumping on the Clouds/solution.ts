/*
 * Complete the 'jumpingOnClouds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY c as parameter.
 */

function jumpingOnClouds(c: number[]): number {
  // Write your code here
  let jumpCount: number = 0;
  let index: number = 0;
  while (index < c.length - 1) {
    if (c[index + 2] == 0) {
      index += 2;
    }
    else {
      index += 1;
    }
    jumpCount += 1;
  }
  return jumpCount;
}