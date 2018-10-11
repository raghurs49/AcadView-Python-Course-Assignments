#Q.1- Name and handle the exception occured in the following program: a=3 if a<4: a=a/(a-3) print(a) 
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError as ob:
    print("Zero Division error found")

==================== RESTART: /root/.atom/assignment6.py ====================
Zero Division error found
    
#Q.2- Name and handle the exception occurred in the following program:
try:
    l=[1,2,3]
    print(l[3])
except IndexError as ob:
    print("Index Value Error Found")
==================== RESTART: /root/.atom/assignment6.py ====================
Zero Division error found

#Q.3- What will be the output of the following code:


    # Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    
==================== RESTART: /root/.atom/assignment6.py ====================
An exception

#Q.4- What will be the output of the following code:
     # Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    
    # Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

==================== RESTART: /root/.atom/assignment6.py ====================
-5.0
a/b result in 0

#Q.5- Write a program to show and handle following exceptions:
#1. Import Error
#2. Value Error
#3. Index Error

try:
    from xyz import abc
except ImportError as e:
    print("Import Error found")

try:
    a="hi"
    print(int(a))
except ValueError as v:
    print("Value error found")

try:
    l=[1,2,3]
    print(l[3])
except IndexError as i:
    print("Index Error Found")

==================== RESTART: /root/.atom/assignment6.py ====================
Import Error found
Value error found
Index Error Found

    
