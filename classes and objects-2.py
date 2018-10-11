 #Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle():
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return self.radius**2*3.14
    
    def getCircumference(self):
        return 2*self.radius*3.14

NewCircle = Circle(10)
print(NewCircle.getArea())
print(NewCircle.getCircumference())
======================== RESTART: /root/assignment.py ========================
314.0
62.800000000000004

#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
#2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.

class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print (self.name)
    print (self.roll)
  def setAge(self,age):
    self.age=age
    print (self.age)
  def setMarks(self,marks):
    self.marks = marks
    print (self.marks)
Stu_Info=Student('Kiteretsu',1)
Stu_Info.display()
Stu_Info.setAge(20)
Stu_Info.setMarks(100)
======================== RESTART: /root/assignment.py ========================
Kiteretsu
1
20
100

#Q.3- Create a Temprature class and create two methods:
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temperature():
    def getCelsius(self,fahrenheit):
        return (fahrenheit-32)*(5/9)
    def getFahrenheit(self,celsius):
        return (celsius*(9/5))+32

New_Temp=Temperature()
print(New_Temp.getCelsius(98))
print(New_Temp.getFahrenheit(37))
======================== RESTART: /root/assignment.py ========================
36.66666666666667
98.60000000000001

#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
#Make methods to
#1. Display-Display the details.
#2. Add- Add the movie details.

class Movie:
  def __init__(self,an,yor,r):
     self.artistname=an
     self.year_of_release=yor
     self.ratings=r
  def display(self):
     print("Movie Discription : \nArtist Name: %s\nYear of release: %d\nRatings: %d"%(self.artistname,self.year_of_release,self.ratings))
  def update(self,an,yor,r):
     self.artistname=an
     self.year_of_release=yor
     self.ratings=r 

m= Movie("xyz",2004,8)
m.display()
print("Updated details :------")
m.update("xyz1",2018,9)
m.display()
======================== RESTART: /root/assignment.py ========================
Movie Discription : 
Artist Name: xyz
Year of release: 2004
Ratings: 8
Updated details :------
Movie Discription : 
Artist Name: xyz1
Year of release: 2018
Ratings: 9

#Q5.Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
   def animal_attribute(self,name,atribute):
       print(name," has attribute to ",atribute)

class Tiger(Animal):
   def show_attribute(self,name,atribute):
       self.animal_attribute(name,atribute)

T = Tiger()
T.show_attribute("Tiger","roar")
======================== RESTART: /root/assignment.py ========================
Tiger  has attribute to  roar

#Q.6- What will be the output of following code.


class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
======================== RESTART: /root/assignment.py ========================
A B
A B


#Q7. Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.

class Shape:
   length=float()
   breadth=float()
   def area(self,l,b):
       self.length=l
       self.breadth=b
       return self.length*self.breadth

class Rectangle(Shape):
   def display_area(self):
      l=float(input("Enter length of rectangle: "))
      b=float(input("Enter breadth of rectangle: "))
      print("Area of Rectangle: ",self.area(l,b))

r= Rectangle()
r.display_area()

class Square(Shape):
   def display_area(self):
      a=float(input("Enter side length of square: "))
      print("Area of Rectangle: ",self.area(a,a))

s= Square()
s.display_area()
======================== RESTART: /root/assignment.py ========================
Enter length of rectangle: 2.0
Enter breadth of rectangle: 4
Area of Rectangle:  8.0
Enter side length of square: 5
Area of Rectangle:  25.0

