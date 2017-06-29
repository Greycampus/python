#import threading
import threading
#function for printing the ouputs
def printt(s):
    print(s)
#defining the gcd function
def gcdd(m,n):
    if(max(m,n)%min(m,n)==0):
        return min(m,n)
    else:
        return gcdd(min(m,n),max(m,n)%min(m,n))
#defining the factorial function
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
#taking input from user
#written in python 2.7 change raw_input to input for python 3
ll = list(map(int,raw_input('enter the numbers:').split(' ')))
#making thread for gcd and factorial
t = threading.Thread(name='gcd',target=printt,args=(gcdd(ll[0],ll[1]),))
d = threading.Thread(name='fact',target=printt,args=(fact(min(ll)),))
#starting threads
t.start()
d.start()
