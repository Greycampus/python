def gcdd(n,m):
    #stopping condition for recursion that is bigger number is divisible by smaller number in gcd parameters
    #max(1,2) returns 2 and min(1,2) returns 1
    #if we pass two numbers as parameters it first checks the division condition of maximum and minimum
    #returns minimum if condition is successful
    if(max(n,m)%min(n,m)==0):
        return min(n,m)
    else:
        #returns gcd of remainder and divisor
        return gcdd(min(n,m),max(n,m)%min(n,m))
#reading the input from user
#first number
print('enter two numbers whose GCD is to be found')
k = int(input())
#second number
k1 = int(input())
print('The GCD is :%d'%gcdd(k,k1))
