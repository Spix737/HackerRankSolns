/*
 * Complete the 'minimumNumber' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. STRING password
 */

function minimumNumber(n: number, password: string): number {
    // Return the minimum number of characters to make the password strong
    const numbers = "0123456789"
    const lower_case = "abcdefghijklmnopqrstuvwxyz"
    const upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    const special_characters = "!@#$%^&*()-+"
    //"Dictionary" array acts as switch for each required character group
    let checks:number[] = [1,1,1,1];
    //for each char, check which group it is in. If found, flip checks[i] & dont check that character group again
    for(let i=0; i<n; i++){
        if(checks[0] == 1 && numbers.includes(password[i])){
            checks[0]--;            
        }
        else if(checks[1] == 1 && lower_case.includes(password[i])){
            checks[1]--;            
        }
        else if(checks[2] == 1 && upper_case.includes(password[i])){
            checks[2]--;            
        }
        else if(checks[3] == 1 && special_characters.includes(password[i])){
            checks[3]--;            
        }
    }
    //add up total checks
    let total:number = 0;
    for(let j=0; j<4; j++){
        total+=checks[j];
    }
    //If with extra chars, password < 6, add the difference to chars needed.
    if(6-(n+total)>0){
        return (total+(6-n-total))    
    }
    //else return chars needed.
    else{
        return (total)
    }
}
