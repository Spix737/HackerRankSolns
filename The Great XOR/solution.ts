function theGreatXor(x: number): number {
    // This is not my best topic. My soln worked but not the intended
    // goal, which is an understanding of bitwise manipulation. Credit for solns to nagarjuna993 and: 
    //https://www.xarg.org/puzzle/hackerrank/the-great-xor/ respectively.
    // Understanding of binary required. Both solns work.
    // Soln 0
    return Math.pow(2, (x.toString(2).length)) - x - 1;
    // Soln 1
    return ~x & (2 ** Math.floor(Math.log2(x) + 1) - 1);
    // Soln 2
    let pos: number = 1;
    let count: number = 0;
    while (x > 0) {
        if ((x & 1) == 0) {
            count |= pos
        }
        pos <<= 1;
        x >>= 1;
    }
    return count;