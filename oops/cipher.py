import re
#cipher parent
#stores text
class cipher:
    """docstring for ."""
    def __init__(self, tst,sh):
        self.tst = tst


class icipher(cipher):
    #inheriting cipher
    #constructor
    def __init__(self,tst,sh):
        cipher.__init__(self,tst,sh)
        self.sh = sh
        #bre function for getting texts from cipher
    def encrypt(self):
        print('entered plain text:'+str(self.tst))
        csr =self.tst.lower()
        cc = str()
        for i in range(0,len(self.tst)):
            if(ord(csr[i])>122-(self.sh%26)):
                #after checking if the ord value may exceed the ascii alphabet range
                #eg: shift = 5 ,for z =>122-26+5%26 => gives 101 i.e., e
                cc =cc+''.join(chr(ord(csr[i])-26+self.sh%26))
            #finding whether the text has numbers
            elif(re.search('(\d)',csr[i])):# can also be done by (ord(csr[i])>=48 and ord(csr[i])<=57)
                #checking for ord value exceeding the numbers limit
                if(ord(csr[i])>57-(self.sh%10)):
                    #eg: for 9 , shift = 3 => 57 -10+3%10 = >50 i.e., 2
                    cc =cc+''.join(chr(ord(csr[i])-10+self.sh%10))
                else:
                    #simply adding the shift as it will not exceed the limits
                    cc= cc+''.join(chr(ord(csr[i])+int(self.sh%10)))
            else:
                #simply adding the shift as it wll not exceed the limits
                cc= cc+''.join(chr(ord(csr[i])+int(self.sh%26)))
        print('cipher text is:'+str(cc))
txt = raw_input('enter the text to encrypted:')
sht = int(input('enter shift for cisear cipher:'))
k = icipher(txt,sht)
k.encrypt()
