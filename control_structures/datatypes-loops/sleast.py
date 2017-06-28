#get number of students
msg = 'Enter number of students:'
print(msg)
#getting input, stripping spaces and converting to int
n  = int(raw_input().strip())
names = []
marks = []
msg = 'enter student details'
print(msg)
for i in range(0,n):
    #getting student name and marks
    names.append(str(raw_input()))
    marks.append(float(raw_input().strip()))
#using zip and making tuple of marks and names
dd = zip(names,marks)
#getting the sorted list using the lambda function
#more about lambda function can be found on python docs
dd = sorted(dd,key= lambda x: (x[1], x[0]))
marks = sorted(marks)
#getting sorted list of unique marks for getting count of second least
sm = sorted(list(set(marks)))
sms = marks.count(sm[1])
sml = marks.count(sm[0])
#getting only names in tuple list using list comprehension
oo = [x[0] for x in dd]
#looping in range of least marks count to least+second least marks count
for i in range(sml,sms+sml):
    print(oo[i])
