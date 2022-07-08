/*
 * Complete the 'cutTheSticks' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function cutTheSticks(arr: number[]): number[] {
    // It works. wow. The arr.length+i took a while to figure out.
    let finArray: number[] = [];
    arr.sort((one, two) => (one > two ? -1 : 1));
    for(let i=0; i<arr.length+i; i++){
        finArray.push(arr.length);   
        let x = arr.pop();
        while (x == arr[arr.length-1]){
            arr.pop();
        }
    }
    return finArray;
}