function repeatedString (s: string, n: number): number {
  // Write your code here

  // Get length of substring s
  let sLength: number = s.length;
  // Get number of a's in the string
  let stringACount: number = s.split('a').length - 1;
  // Get the number of times the complete string s will be in the final string
  let sCount: number = Math.floor(n / sLength);
  // Multiply the number of a's in s with the number of s's in the final string
  let actualACount: number = stringACount * sCount;
  // obtain remaining a's by checking if there is a partially complete s
  actualACount += (s.slice(0, n % sLength).split('a').length - 1);

  return actualACount;

  // let stringVar: string = s;
  // let sLength: number = s.length;

  // for(let i=sLength; i<n; i+=sLength){
  //   if(i+sLength<=n){
  //     stringVar = stringVar.concat(s);
  //   }
  //   else{
  //     stringVar = stringVar.concat(s.substring(0,sLength-(i+sLength-n)));
  //   }
  // }
  // let counter:number = 0;
  // for(let j=0; j<stringVar.length; j++){
  //   if(stringVar[j] == 'a'){
  //     counter++;
  //   }
  // }
  // return counter;
}