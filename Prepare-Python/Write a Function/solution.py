def is_leap(year):
    """
    Determines if a year is a leap year based on Gregorian calendar rules.
    Utilizes boolean short-circuiting for optimal evaluation performance.
    """
    # Leap year logic: divisible by 4, but not by 100 unless also divisible by 400
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    
    # leap = False
    # if year % 4 == 0:
    #     leap = True
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             leap = True
    #         else:
    #             leap = False
    # return leap

year = int(input())