def soe(n,prime):
    p = 2
    while p*p<=n:
        if prime[p] ==True:
            i=p*2
            while i<=n:
                prime[i] = False
                i = i+p
        p+=1
    return prime


def mp(n):
    prime = [True for i in range(0,n+1)]
    prime = soe(n,prime)
    k = 2
    while ((1<<k)-1<=n and (1<<k)+1<=n):
        num = (1<<k)-1
        if (prime[num]):
            print(num)
        num = (1<<k)+1
        if (prime[num]):
            print(num)
        k = k+1

print('enter the number')
n = int(input())
print('primes that are exactly at absolute difference of 1 with powers of 2 are:')
mp(n)
