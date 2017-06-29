#defining a global inside the fuction
def glob():
    #global variable
    global pi
    gb = 3.14159
glob()
#message variable
msg = 'Enter radius of the circle:'
#printing message for getting user input
print(msg)
#getting input from console
r = raw_input()
#stripping excess spaces and converting into float
r = float(r.strip())
#calculating radius
area = pi*r*r
# initialized the function and using global value of pi
print ('Area of circle with radius '+str(r)+' is '+str(area))
