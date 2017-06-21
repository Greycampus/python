# Python program to check if the input year is a leap year or not

year = int(input('Enter year:'))
#first divisible by 4 and not by 100 or second divisible by 400
if (year % 4 == 0 and year % 100!=0) or year%400==0:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
