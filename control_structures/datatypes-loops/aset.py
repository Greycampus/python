#message variable
msg = 'enter list of your choice with repetitions:'
#printing message for user input
print(msg)
#taking data from user in console
a = raw_input()
#stripping the excess zeroes in input
a = a.strip()
#splitting the raw input into individual elements and storing in list
b = list(a.split())
#set is a datatype in python only stores unique items in list
#conversion list->set
c = set(b)
#printing the unique item list
print(c)
