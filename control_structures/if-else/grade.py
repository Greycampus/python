#finding grades
#message variable
msg = 'enter the percentage of student:'
#printing message for user input
print(msg)
a = raw_input()
#stripping zeroes and converting it into interger
a = int(a.strip())
if(a>85):#if percent > 85 --A
    print('Grade - \'A\'')
elif(a<=85 and a>80):#80<percent80=85  --A-
    print('Grade - \'A-\'')
elif(a>70 and a<=80):#70<percent<=80 --B
    print('Grade - \'B\'')
elif(a>60 and a<=70):#60<percent<=70  --C
    print('Grade - \'C\'')
elif(a>40 and a<=60):#40<percent<=60  --D
    print('Grade - \'D\'')
elif(a<=40):#percent<=40  --E
    if(a<=35):#failed condition
        print('Grade - \'E\' Candidate failed')
    else:
        print('Grade - \'E\'')
