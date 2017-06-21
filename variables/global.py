#defining a global inside the fuction
def glob():
    #global variable
    global gb
    gb = 3.146
glob()
r = input('enter radius of the circle:')
# initialized the function and using global value of pi
print ('Area of circle with radius '+str(r)+'is'+str(gb*r*r))
