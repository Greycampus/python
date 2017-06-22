# importing python regex library
import re
k = str(raw_input('enter the raw data containing mail addresses:'))
#finds all patterns that match alphanumeric
m = re.findall(r"[a-zA-Z0-9._$%+-]+.[@].[a-zA-Z0-9]+\..[a-zA-Z]{0,1}.",k)
print('extracted mail addresses are:')
for i in range(0,len(m)):
    print(m[i])
