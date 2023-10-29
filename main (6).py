#challenge 3.2
class student:

   def__init__(self,name,roll_number,cgpa):
    self.name=Name
    self.roll_number=roll_number
    self.cgpa=cgpa


def sort_students(student_list):
  #sort the list of students in descending order of cgpa
   sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=true)
  #syntax-lambda arg:exp
   return sorted_students


#example usage:
students=[
    students("hari","A123",7.8),,
    students("srikanth","A124",8.9),
    students("saumya","A125",9.1),
    students("mahidhar","A126",9.9),
]

sorted_students=sort_students(students)

#print the sorted list of students
for students in sorted_students:
  print("name:{},Roll_number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
  
  