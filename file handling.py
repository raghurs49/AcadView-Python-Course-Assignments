#Q.1- Write a Python program to read n lines of a file

with open(r"/root/Documents/file.txt","rt") as ob:
    n=int(input("Enter the number of lines you want to read:"))
    lines=ob.readlines()[0:n]
    for i in lines:
        print(i)
print("Done!!!")

==================== RESTART: /root/.atom/assignment7.py ====================
Enter the number of lines you want to read:4
there are 15 students present in class

we are using file handling

fo=open(r"/root/Documents/students.txt","r")

str1=fo.read(10)

Done!!!

#Q.2- Write a Python program to count the frequency of words in a file.

from collections import Counter

with open("/root/Documents/file.txt") as f:
    freq_count=Counter(f.read().split())
    print(freq_count)

==================== RESTART: /root/.atom/assignment7.py ====================
Counter({'print("Read': 3, 'string:",str1)': 3, "print('-'*5)": 3, 'are': 2, 'str1=fo.read(15)': 2, 'there': 1, '15': 1, 'students': 1, 'present': 1, 'in': 1, 'class': 1, 'we': 1, 'using': 1, 'file': 1, 'handling': 1, 'fo=open(r"/root/Documents/students.txt","r")': 1, 'str1=fo.read(10)': 1})

#Q.3- Write a Python program to copy the contents of a file to another file

with open("/root/Documents/file.txt") as f:
    with open("/root/Documents/test.txt", "wt") as t:
        for line in f:
            t.write(line)
with open("/root/Documents/test.txt","rt") as t:
    for line in t:
        print(line)
        
==================== RESTART: /root/.atom/assignment7.py ====================
there are 15 students present in class

we are using file handling

fo=open(r"/root/Documents/students.txt","r")

str1=fo.read(10)

print("Read string:",str1)

print('-'*5)

str1=fo.read(15)

print("Read string:",str1)

print('-'*5)

str1=fo.read(15)

print("Read string:",str1)

print('-'*5)

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.

with open('/root/Documents/file.txt') as f, open('/root/Documents/test.txt') as t:
    for l2,l5  in zip(f, t):
        
        print(l2+l5)
        
==================== RESTART: /root/.atom/assignment7.py ====================
there are 15 students present in class
there are 15 students present in class

we are using file handling
we are using file handling

fo=open(r"/root/Documents/students.txt","r")
fo=open(r"/root/Documents/students.txt","r")

str1=fo.read(10)
str1=fo.read(10)

print("Read string:",str1)
print("Read string:",str1)

print('-'*5)
print('-'*5)

str1=fo.read(15)
str1=fo.read(15)

print("Read string:",str1)
print("Read string:",str1)

print('-'*5)
print('-'*5)

str1=fo.read(15)
str1=fo.read(15)

print("Read string:",str1)
print("Read string:",str1)

print('-'*5)
print('-'*5)


#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file
import random

with open("/root/Documents/file.txt","wt") as f:
    for i in range(10):
        f.write(str(random.randint(0,9)))
        f.write("\n")

with open("/root/Documents/file.txt","rt") as f,open("/root/Documents/test.txt","wt") as t:
    l = []
    for line in f:
        l.append(int(line.strip("\n")))
    l = sorted(l)
    for i in l:
        t.write(str(i)+"\n")

with open("/root/Documents/test.txt") as t:
    for i in t:
        print(i.strip("\n"))
==================== RESTART: /root/.atom/assignment7.py ====================
0
1
3
4
5
5
6
7
8
9

