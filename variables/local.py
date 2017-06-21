#program to find nearest power of three for a number
#import math library for log functions
from math import log,floor,ceil
#taking input and casting it into integer
k = int(input('enter the number:'))
#log(x[,base]) gives the natural algorithm of log(x)/log(base)
#helpful in getting the nearest power to 3 as follows
#3^n = x+c where c is minimum for nearest power
#3^n = x+c => log(3^n) = log(x+c) => n*log(3) = log(x+c)
#let x+c = X
#=> n = log(X)/log(3) where n is the nearest nth power of 3
# similar in our case  3^n < x < 3^n+1 we calculate the minimum by
#n<log(x)/log(3)<n+1 and find the nearest power
minn = floor(log(k,3))
maxx = ceil(log(k,3))
if abs(k - 3**minn) <= abs(3**maxx - k):
    print(3**minn)
else:
    print(3**maxx)
