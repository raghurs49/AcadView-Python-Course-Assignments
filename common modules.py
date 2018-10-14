# Q.1- Print the current day using Datetime module.

from datetime import date
import calendar
my_date=date.today()
print(calendar.day_name[my_date.weekday()])

========================== RESTART: /root/assgn.py ==========================
Sunday

# Q.2- Open your browser and play a video using webbrowser module in python.

import webbrowser
import time

total_breaks=3
break_count=0
while(break_count<total_breaks):
    print("this is program on:"+time.ctime())
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=SCOKysMnH50")
    break_count+=1

========================== RESTART: /root/assgn.py ==========================
this is program on:Sun Oct 14 10:32:55 2018
this is program on:Sun Oct 14 10:33:05 2018
this is program on:Sun Oct 14 10:33:15 2018

# Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.

import os
path='/root/Documents'
files=os.listdir(path)
i=1

for file in files:
    os.rename(os.path.join(path,file),os.path.join(path,str(i)+'.jpg'))

    i+=1
========================== RESTART: /root/assgn.py ==========================
>>>

x-special/nautilus-clipboard
copy
file:///root/Documents/1.jpg
file:///root/Documents/2.jpg
file:///root/Documents/3.jpg
file:///root/Documents/4.jpg
file:///root/Documents/5.jpg
file:///root/Documents/6.jpg
file:///root/Documents/7.jpg
file:///root/Documents/8.jpg
file:///root/Documents/9.jpg
file:///root/Documents/10.jpg
file:///root/Documents/11.jpg
file:///root/Documents/12.jpg
