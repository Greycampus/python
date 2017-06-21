# enter equation that is in form of  x3+4x2+2x-1 as 1 4 2 -1
equa = input('enter the quotients:')
#spliting string into int list using map and split
quo = list(map(int,equa.split()))
mm = []
#integration loop for getting integration of equation
for i in range(0,len(quo)):
    if(len(quo)-i-1!=0):
        mm.append((len(quo)-i-1)*quo[i])
str1 = 'after differentiation,the equation is:'
#using loops and generating user understandable equation
for i in range(0,len(mm)):
    #if power of x not equal to zero condition
    if(len(mm)-i-1 != 0):
        #for i = o
        #str1=str1+'quotient of x^n i.e mm[0]'+X+'power of x(n(length - 0 - 1))'
        str1=str1+''.join(str('%+d'%mm[i])+'x^'+str(len(mm)-i-1))
    else:
        str1=str1+''.join(str('%+d'%mm[i]))
    #condition for last term with power = 0
    if i != (len(mm)-1):
        str1=str1+' '
print(str1)
str2 = 'after integration the equation is:'
dd = [len(quo)-i for i in range(0,len(quo))]
for i in range(0,len(quo)):
    #for i = o
    #str2=str2+'quotient of x^n i.e mm[0]'+X+'power of x(n(length - 0))'
    str2=str2+''.join(str('%+f'%(float(quo[i])/dd[i]))+'x^'+str(len(quo)-i))
    str2=str2+' '
#adding constant
str2 = str2+'+C'
print(str2)
