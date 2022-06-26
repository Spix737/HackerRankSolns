'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

function extraLongFactorials(n) {
    // Ugh, cool to learn but ugh.
    if(n == 0){
        return 0
    }
    let result = 1n;
    while(n>0){
        result*=BigInt(n);
        n-=1;
    }
    console.log(String(result));
}



function main() {
    const n = parseInt(readLine().trim(), 10);

    extraLongFactorials(n);
}
