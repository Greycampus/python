#getting user input
#get initial term in series
a = int(input('enter initial term:'))
#get ratio in series only integers
r = int(input('enter ratio in series(only integers):'))
k = int(input('enter number you want to check:'))
if(k%a==0 and k==a):
    print('you just entered the initial term again,yes its in series')
elif(k%a==0 and k%r==0 and k>a):
    #for G.P : a ar ar2 ar3 ......
    tmp = k/a #dividing by a(initial term)
    #now series consideration becomes
    # 1 r r2 r3 r4 .......
    while tmp!=1 and tmp >=r:#check for ratio exponential as in a.r^n
        tmp=tmp/r
    if(tmp==1):
        print('%d is in series'%k)
    else:
        print('%d is not in series'%k)
else:
    print('%d is not in series'%k)
