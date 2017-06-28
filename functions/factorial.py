def facta(n):
    #if n==1 and n==0 returns 1 and the stopping condtion for recursion
    if n==1 or n==0:
        return 1
    else:
        #using recursion and calling the factorial of n-1
        return n*facta(n-1)
msg = 'enter the number to find its factorial'
print(msg)
k = int(input())
print('factorial is %d'%facta(k))
