int diagonalDifference(vector<vector<int>> arr) {
    int ltr = 0;
    int rtl = 0;
    int a = arr.size();
    for(int i=0; i<a;  i++){
        ltr+= arr[i][a-i-1];
        rtl+= arr[a-i-1][a-i-1];
    }
    int absoluteDiff = abs(ltr-rtl);
    return absoluteDiff;
}