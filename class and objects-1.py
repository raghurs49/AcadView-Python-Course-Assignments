#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.

dict={}
for i in range (int(input("Enter the key-value pairs you want to input:"))):
    dict[i]=i
n=int(input("Enter the value for which the key you want to search:"))
for key in dict.keys():
    if dict[key]==n:
        print(key)
    else:
        print("key not found!!! Error")
print("total elements present are:",dict[i])

==================== RESTART: /root/.atom/assignment8.py ====================
Enter the key-value pairs you want to input:10
Enter the value for which the key you want to search:4
key not found!!! Error
key not found!!! Error
key not found!!! Error
key not found!!! Error
4
key not found!!! Error
key not found!!! Error
key not found!!! Error
key not found!!! Error
key not found!!! Error
total elements present are: 9


#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject

students={
          "Doraemon":{"discrete maths":76,"python":56,"aptitude":80,"perl":40},
          "Nobita":{"discrete maths":86,"python":96,"aptitude":90}
          }
stu_name=input("Enter the name of student you want to search:").title()
if stu_name in students:
    print(stu_name)
    for key,value in students[stu_name].items():
        print(key,value)
else:
    print("No such student in the list as you mentioned")

==================== RESTART: /root/.atom/assignment8.py ====================
Enter the name of student you want to search:doraemon
Doraemon
discrete maths 76
python 56
aptitude 80
perl 40
