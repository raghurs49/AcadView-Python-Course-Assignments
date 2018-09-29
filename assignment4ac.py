Q.1- Reverse the whole list using list methods. 


1.
>>> lst=[10,20,30,'python','java','perl']
>>> z=list(reversed(lst))
>>> print(z)
    ['perl', 'java', 'python', 30, 20, 10]
>>> lst[::-1]
    ['perl', 'java', 'python', 30, 20, 10]
>>> lst.reverse()
>>> print(lst)
    ['perl', 'java', 'python', 30, 20, 10]

 Q.2- Print all the uppercase letters from a string. 

2.
  >>> str="Hello welcome to The classes of Python Programming"
>>> for i in str:
	if i==i.upper():
		print(i,end="",sep="")
	print()

	
H




 







 


 
T


 







 


 
P





 
P


Q.3- Split the user input on comma's and store the values in a list as integers.

3.

   >>> string=(input("enter some elements of a list seperated by commas").split(","))
        enter some elements of a list seperated by commas python,perl,machine learning,10,20,30,7.8
   >>> w=list(string)
   >>> print(w)
       [' python', 'perl', 'machine learning', '10', '20', '30', '7.8']

 Q.4- Check whether a string is palindromic or not.


4.
   x=input("Enter the element to check whether it is palindromic or not:")
if x[::-1]==x:
    print(x,"is palindromic element")
else:
    print(x,"is not palindromic element")
    
   python palindromic.py
   Enter the element to check whether it is palindromic or not:apple
   apple is not palindromic element

   python palindromic.py
   Enter the element to check whether it is palindromic or not:pop
   pop is palindromic element


Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.

5.
   
>>> z=['python','java',10,30,40]
>>> id(z)
140490885376200
>>> p=z
>>> id(p)
140490885376200
>>> s=z.copy()
>>> id(s)
140490885304840
>>> del z[-1]
>>> print(z)
['python', 'java', 10, 30]
>>> print(p)
['python', 'java', 10, 30]
>>> print(s)
['python', 'java', 10, 30, 40]
>>> 
 Here,the z and p is the shallow copy because of the same id whereas the s is the deep copy beacuse of the different id.  

