import re
msg = 'enter the alphanumeric string'
print(msg)
k= str(raw_input())
#getting all the patterns having instance of single digit and mapping it as integer for storing inlist
k = list(map(int,re.findall(r"[0-9]",k)))
#find sum using sum finction of python can be used on integer,float and long type lists
summ = sum(k)
print('the sum is %d'%summ)
