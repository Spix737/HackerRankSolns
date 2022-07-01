/*
 * Complete the 'libraryFine' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER d1
 *  2. INTEGER m1
 *  3. INTEGER y1
 *  4. INTEGER d2
 *  5. INTEGER m2
 *  6. INTEGER y2
 */

function libraryFine(d1: number, m1: number, y1: number, d2: number, m2: number, y2: number): number {
    // Innefficient but works for all cases.
    if(y1 > y2){
        return 10000;
    }
    else if(y1 < y2){
        return 0;
    }
    else{
        if(m1>m2){
            return (Math.abs(m2-m1)*500)
        }
        else if(m1<m2){
            return 0;
        }
        else{
            if(d1>d2){
                return (Math.abs(d2-d1)*15);
            }
            else{
                return 0;
            }
        }
    }
}