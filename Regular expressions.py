#1.Write a python code to find a valid email address from a text. 

import re
str1='hi my name is raghu and for any help contact me on my mail id raghusharma0404@gmail.com'
addresses=re.findall(r'[\w\.-]+@[\w\.-]+',str1)
print(addresses)

========================== RESTART: /root/assgn.py ==========================
['raghusharma0404@gmail.com']


# Q.2- Write a python program to find a valid Indian phone number from a text.(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )

import re
pattern=r"[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$"
str1=('hi my name is raghu and for any help contact me on my mail id raghusharma0404@gmail.com and my phone no is 7889806911')
valid_no=re.findall(pattern,str1)
print(valid_no)

========================== RESTART: /root/assgn.py ==========================
['7889806911']
