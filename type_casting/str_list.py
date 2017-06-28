#program for converting string to list
msg = 'Enter the string'
print(msg)
k = raw_input()
print('Entered string :'+k)
#using split and type casting we convert string to list
li = list(k.split(' '))
print('List generated is:')
print(li)
