import getpass
#getpass is used to get input hidden
msg = 'enter secret number for game:'
sec = getpass.getpass(prompt=msg,stream=None)
msg = 'player have three guesses for a 4digit number.(number range 1-6)'
print(msg)
for i in range(0,3):#three guesses
    g = str(raw_input())
    scr = str()
    if(g==sec):#if guess = actual
        print('++++ you won')
        break
    else:
        for j in range(0,len(sec)):
            if(sec.find(g[j])==g.find(g[j])):
                #if position of a digit in guess = position of digit in actual number
                scr = scr+'+'
            elif(sec.count(g[j])==g.count(g[j]) and sec.find(sec[j]) != sec.find(g[j]) ):
                #if position of digit is not same but if digit exists in numbers
                scr = scr+'-'
            else:
                #if no match in position or occurence
                scr = scr+' '
        print(scr+' have another try')
print('well played')
