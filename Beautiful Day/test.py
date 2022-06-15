def beautifulDays(i, j, k):
    # Write your code here
    dayArray = [num for num in range(i,j+1)]
    print(dayArray)
    beautifulDayCount = 0
    for day in dayArray:
        chars = [char for char in str(day)]
        chars.reverse()
        dayFlip = ''.join(str(x) for x in chars)
        if abs(day - int(dayFlip))%k==0:
            beautifulDayCount+=1
    return beautifulDayCount