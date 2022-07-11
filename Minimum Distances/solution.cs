/*
* Complete the 'minimumDistances' function below.
*
* The function is expected to return an INTEGER.
* The function accepts INTEGER_ARRAY a as parameter.
*/

public static int minimumDistances(List<int> a)
{
    // Simple and clean.
    int min = int.MaxValue;
    for(int i=0; i<a.Count; i++){
        for(int j=i+1; j<a.Count; j++){
            if(a[i]==a[j]){
                min = Math.Min(Math.Abs(i-j), min);
            }
        }
    }
    return (min == int.MaxValue ? -1 : min);
}