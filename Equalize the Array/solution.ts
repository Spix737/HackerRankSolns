/*
 * Complete the 'equalizeArray' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function equalizeArray(arr: number[]): number {
  // Simple
  let values: number[] = [];
  let counts: number[] = [];
  for (let i = 0; i < arr.length; i++) {
    //Get indexOf val so as to...
    let x: number = values.indexOf(arr[i]);
    //...check if val previously encountered
    if (x < 0) {
      values.push(arr[i]);
      counts.push(1);
    }
    else {
      // Increment count of val using index
      counts[x]++;
    }
  }
  return arr.length - Math.max(...counts);
}