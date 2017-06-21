equa = raw_input('enter the coefficients of quadratic equation:')
quo = list(map(float,equa.split()))
mm = []
#derivative loop
#power of x = length - 1 - i  for i = 0 => power = 2
for i in range(0,len(quo)):
    #checks if the power of x is 0
    if(len(quo)-i-1!=0):
        #appending the derivative equation ,power of x*quotient of x
        mm.append((len(quo)-i-1)*quo[i])
print('After differentiation the equation:'+str(mm[0])+'x%+f'%(mm[1]))
#getting solution : constant in derived equation/quotient of x
mai = float(-1*mm[1])/mm[0]
if(quo[0]>=0):
    print('the minima of given equation is at x=%f'%mai)
else:
    print('the maxima of given equation is at x=%f'%mai)
