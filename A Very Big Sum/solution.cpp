long aVeryBigSum(vector<long> ar){
    long sum = 0;
    int count = ar.size();
    for(int i=0; i<count; i++){
        sum+=ar[i];
    }
    return sum;
}