#take in user input with multiple types in string format
msg = 'Enter the number of students'
print(msg)
#taking input from user stripping extra spaces and converting into integer
n = int(raw_input().strip())
marks = []
print('Enter the details of students:')
for _ in range(n):
    #making list of raw data
    marks.append(list(raw_input().split(' ')))
#get name for percentage finding
msg = 'enter name of student'
print(msg)
c = str(raw_input())
for x in marks:
    if (x[0] == c):
        #summing the marks
        total = int(x[1])+int(x[2])+int(x[3])
        #finding average for getting marks
        total = total/3
        print('percentage is %.2f'%total)
