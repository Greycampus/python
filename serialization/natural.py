#importing pickle module
import pickle
msg = 'enter the nth term:'
print(msg)
#storing in pickle dumps
#                                       list comprehension for getting natural number range after stripping spaces from input
x = pickle.dumps(range(1,int(raw_input().strip())+1))
print('serialized numbers')
#printing the serialized data using pickle loads
print(pickle.loads(x))
