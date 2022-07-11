function sumXor(n: number): number {
    // Tricky, easy to fall into bruteforce trap.
    // Solution is to convert to binary and total instances of 0, as xor is just addition without carrying over.
    // Then you can just find the values where + and xor are equal by calculating pow(2, count-of-0).
    if (n === 0) {
        return 1;
    }
    let count = 0;
    let numberInBinary = n.toString(2);
    for (let i = 0; i < numberInBinary.length; i++) {
        if (numberInBinary[i] === '0') {
            count++;
        }
    }
    return Math.pow(2, count);
}
