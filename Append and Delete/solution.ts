/* https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true
 * Complete the 'appendAndDelete' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. STRING t
 *  3. INTEGER k
 */

function appendAndDelete(s: string, t: string, k: number): string {
  // What a good solution. Credit to YASH PAL @ programs.programingoneonone.com
  for (var i = 0; i < s.length; i++) {
    if (!(s[i] == t[i])) {
      break;
    }
  }
  let deletesRequired: number = s.length - i;
  let addsRequired: number = t.length - i;
  let minRequired: number = deletesRequired + addsRequired;
  let max: number = s.length + t.length;
  // if we have less moves than min required or if (K is odd & minRequired is even (or vice versa)) AND we have less moves than the length of both arrays
  if (k < minRequired || ((k % 2 != minRequired % 2) && k < max)) {
    return ("No");
  } else {
    return ("Yes");
  }
}
