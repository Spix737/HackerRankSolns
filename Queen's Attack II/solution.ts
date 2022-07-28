/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

function queensAttack(n: number, k: number, r_q: number, c_q: number, obstacles: number[][]): number {
  //Bit tricky - this algorithm calculates the distance from the queen to the edge of the board in each direction to determine where she can attack
  //Then for each obstacle  check if it's in the Queen's way, and find what's closer, using that as the distance the queen may attack.

  //N, NE, E, SE, S, SW, W, NW
  let dir:number[] = [
  n-r_q, //N
  Math.min(n-r_q, n-c_q), //NE
  n-c_q, //E
  Math.min(r_q-1, n-c_q), //SE
  r_q-1, //S
  Math.min(c_q-1, r_q-1), //SW
  c_q-1, //W
  Math.min(c_q-1, n-r_q) //NW
  ];
  
  for(let i=0; i<k; i++){
    if(obstacles[i][0] === r_q){
      if (obstacles[i][1] < c_q) {            
              dir[6] = Math.min(dir[6], c_q - obstacles[i][1] - 1);
          } else {
              dir[2] = Math.min(dir[2], obstacles[i][1] - c_q - 1);
          }
    } else if(obstacles[i][1] === c_q) {
        if (obstacles[i][0] < r_q) {            
            dir[4] = Math.min(dir[4], r_q - obstacles[i][0] - 1);
          } else {
            dir[0] = Math.min(dir[0], obstacles[i][0] - r_q - 1);
          }
    } else if(obstacles[i][1] - obstacles[i][0] === c_q - r_q){
        if (obstacles[i][1] < c_q) {
            dir[5] = Math.min(dir[5], c_q - obstacles[i][1] - 1);
          } else {
            dir[1] = Math.min(dir[1], obstacles[i][1] - c_q - 1);
          }
    } else if(obstacles[i][1] + obstacles[i][0] === c_q + r_q){
        if (obstacles[i][1] < c_q) {
            dir[7] = Math.min(dir[7], c_q - obstacles[i][1] - 1);
          } else {
            dir[3] = Math.min(dir[3], obstacles[i][1] - c_q - 1);
          }
    }
  } 
  let sum:number = 0;
  for(let j=0; j<dir.length; j++){
    sum+=dir[j];
  }
  return sum;
}