# importing python regex library
import re
k = str(raw_input('enter the raw data containing mail addresses:'))
#finds all patterns that match alphanumeric_with_symbols@alphanumeric.com|net|any 3 letter extension
m = re.findall(r"[a-zA-Z0-9._$%+-]+.[@].[a-zA-Z0-9]+\..[a-zA-Z]{0,1}.",k)
print('extracted mail addresses are:')
#printing all the mail addresses matching the pattern
for i in range(0,len(m)):
    print(m[i])
