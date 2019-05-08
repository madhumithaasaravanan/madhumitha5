import re
s=input()
if(re.findall('[a-zA-Z]',s))and(re.findall('[0-9]',s)):
    print("yes")
else:
    print("no")
