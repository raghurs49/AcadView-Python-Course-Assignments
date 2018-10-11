# Q.1- Create a function to calculate the area of a sphere by taking radius from user.
def area_sphere(rad):
    return(4*(3.14*rad**2))
r=float(input("Enter the radius of sphere:"))    
print(area_sphere(r))

==================== RESTART: /root/.atom/assignment8.py ====================
Enter the radius of sphere:50
31400.0

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perf_num(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return True
for i in range(1,1001):
    if perf_num(i):
        print(i,"is perfect number")

==================== RESTART: /root/.atom/assignment8.py ====================
6 is perfect number
28 is perfect number
496 is perfect number

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.

def multi_table(n):
    for i in range(1,21):
        print(n,'*',i,"=",n*i)
n=int(input("Enter the number for which u want to generate the table:"))
multi_table(n)

==================== RESTART: /root/.atom/assignment8.py ====================
Enter the number for which u want to generate the table:101
101 * 1 = 101
101 * 2 = 202
101 * 3 = 303
101 * 4 = 404
101 * 5 = 505
101 * 6 = 606
101 * 7 = 707
101 * 8 = 808
101 * 9 = 909
101 * 10 = 1010
101 * 11 = 1111
101 * 12 = 1212
101 * 13 = 1313
101 * 14 = 1414
101 * 15 = 1515
101 * 16 = 1616
101 * 17 = 1717
101 * 18 = 1818
101 * 19 = 1919
101 * 20 = 2020

#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def pow_num(base,expo):
    if(expo==1):
        return base
    if(expo!=1):
        return (base*pow_num(base,expo-1))
base=int(input("Enter the base:"))
expo=int(input("Enter the exponent:"))
print(pow_num(base,expo))

==================== RESTART: /root/.atom/assignment8.py ====================
Enter the base:2
Enter the exponent:3
8






