1.
  >>> x=list()
  >>> x
  []

2. 

  >>> x=x+["google","apple","facebook","microsoft","tesla"]
  >>> x
     ['google', 'apple', 'facebook', 'microsoft', 'tesla']
3.
  >>> x.count("google")
      1
  >>> x.count("apple") 
      1 
  >>> x.count("facebook")
      1
  >>> x.count("microsoft")
      1
  >>> x.count("tesla")
      1

4.
   >>> y=[12,23,43,51,2,3,94,1,455,42,568,998,900]
   >>> y
       [12, 23, 43, 51, 2, 3, 94, 1, 455, 42, 568, 998, 900]
   >>> y.sort()
   >>> y
       [1, 2, 3, 12, 23, 42, 43, 51, 94, 455, 568, 900, 998]

5.
   >>> a=[12,23,43,51,2,3,94,1,455,42,568,998,900]
   >>> b=[133,14,53,6,2,7,8,9,0,5,3,2,666]
   >>> c=a+b
   >>> c.sort()
   >>> c
       [0, 1, 2, 2, 2, 3, 3, 5, 6, 7, 8, 9, 12, 14, 23, 42, 43, 51, 53, 94, 133, 455, 568, 666, 900, 998]

6.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_odd=0
count_even=0
for x in numbers:
    if x%2==0:
        count_even+=1
    else:
        count_odd+=1

print("no of odd number",count_odd)
print("no of even numbers",count_even)


no of odd number 5
no of even numbers 4
[Finished in 0.12s]


7.
  >>> t=("python","java","perl","numpy","pandas","anaconda")
  >>> t
      ('python', 'java', 'perl', 'numpy', 'pandas', 'anaconda')
  >>> type(t)
      <class 'tuple'>
  >>> t[::-1]
      ('anaconda', 'pandas', 'numpy', 'perl', 'java', 'python')
  >>> t
      ('python', 'java', 'perl', 'numpy', 'pandas', 'anaconda
      
8.
  >>> v=(100,33,425,5251,33,4,2,0,-1)
  >>> max(v)
      5251
  >>> min(v)
      -1

9.
   >>> "python".upper()
       'PYTHON'

10.
    >>> a="0900"
    >>> a.isdigit()
        True

11.

    >>>  s="Hello World"
    >>>  s
	'Hello World!'
    >>>  s.replace("World","raghu")
        'Hello raghu'



