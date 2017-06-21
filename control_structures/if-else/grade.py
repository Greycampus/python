#finding grades
k = input('enter the percentage of student:')
if(k>85):#if percent > 85 --A
    print('Grade - \'A\'')
elif(k<=85 and k>80):#80<percent80=85  --A-
    print('Grade - \'A-\'')
elif(k>70 and k<=80):#70<percent<=80 --B
    print('Grade - \'B\'')
elif(k>60 and k<=70):#60<percent<=70  --C
    print('Grade - \'C\'')
elif(k>40 and k<=60):#40<percent<=60  --D
    print('Grade - \'D\'')
elif(k<=40):#percent<=40  --E
    if(k<=35):#failed condition
        print('Grade - \'E\' Candidate failed')
    else:
        print('Grade - \'E\'')
