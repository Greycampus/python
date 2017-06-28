msg = 'enter total number of mediums: '
print(msg)
k = int(raw_input().strip())
msg = 'enter length of medium: '
print(msg)
l = int(raw_input().strip())
msg = 'enter height from which ball is thrown: '
print(msg)
h = int(raw_input().strip())
msg = 'enter distance travelled in each step:'
print(msg)
d = int(raw_input().strip())
print('now enter qoutients of loss for %d mediums:'%k)
kq =[]
for i in range(0,k):
    #appending into list, the converted float from input
    kq.append(float(input('%d medium :'%(i+1))))#input can print messages given as parameters
h1 = h
d1 = 0
while h1!=0:
    fl = k*l
    for i in range(0,k): #for medium check
        if (h1!=0): #height not equal to zero
            tt = d1%fl #medium repeatition check
            d1=d1+d #distance increament per step
            h1 = int(h1*(1-kq[int(tt/l)]))
            print(h1)
print('distance traveled by ball is %d'%d1)
