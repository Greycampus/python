# program to store a sequence in a list or array
# taking length of list to be inputted
k = int(input('enter the number of elements:'))
#empty list
ll = []
print('Enter the elements:')
for i in range(0,k):
    #using append function of lists and appending the data into empty list
    ll.append(int(input()))
print('Elements of list are:')
print(ll)
