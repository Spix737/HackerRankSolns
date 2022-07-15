/* https://www.hackerrank.com/challenges/sherlock-and-squares
 *
 * Complete the 'squares' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER a
 *  2. INTEGER b
 */

function squares(a: number, b: number): number {
  // Attempt 2 - Iterate linearly to determine initial square number, then hop from square to square until out of range. A lot more efficient but less clean code.
  // I am not certain if true forever, but typically square numbers aren't next to each other...
  let iterator: number = a;
  let sqCount: number = 0;
  let aSquare: boolean = false
  while (aSquare == false && iterator < b + 1) {
    if (Math.sqrt(iterator) % 1 == 0) {
      sqCount++;
      aSquare = true;
    }
    else {
      iterator++;
    }
  }
  let mySquare: number = Math.sqrt(iterator) + 1;
  while (Math.pow(mySquare, 2) <= b) {
    sqCount++;
    mySquare++;
  }
  return sqCount

  // Attempt 1 - works, but iterates linearly. Can we increase the efficiency. 
  // let iterator:number = a;
  // let sqCount:number = 0;
  // while(iterator<b+1){
  //   if(Math.sqrt(iterator)%1==0){
  //     sqCount++;
  //   }
  //   iterator++;
  // }
  // return sqCount
}