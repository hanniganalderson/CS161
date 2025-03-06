#CS161 Week 9
class Students:
    def __init__(self, name, age, grade): #initalize with self and 3 attributes
        self.name = name #name attribute
        self.age = age #age attribute
        self.grade = grade #grade attribute
    def __str__ (self): #__str__ for formatting the printing of Students object
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}" #\n for neat lines

student_1 = Students("Raj", 16, "11th") # giving parameters to student_1
student_2 = Students("Joe", 17, "11th") # giving parameters to student_2
#print results
print(student_1)
print(student_2)

class Staff: #parent class Staff
    def __init__(self, name, department, role, salary):
        self.name = name #name attribute
        self.department = department #department attribute
        self.role = role #role attribute
        self.salary = salary #salary attribute

class Teacher(Staff): #child class Teacher
    def __init__(self, name, department, role, salary, age):
        Staff.__init__(self, name, department, role, salary) #calling Staff constructor to get attributes
        self.age = age #adding age attribute for Teacher
    def __str__(self): #formatting the printing
        return f"Name: {self.name}\nAge: {self.age}\nRole: {self.role}\nSalary: {self.salary}\nDepartment: {self.department}"
#\n for neat lines

#giving parameters to teacher_1 & teacher_2
teacher_1 = Teacher("Raj", "Science", "Teacher", 20000, 20)
teacher_2 = Teacher("Joe", "Science", "Teacher", 30000, 58)
#print results
print(teacher_1)
print(teacher_2)

class Square: #class Square
    def __init__(self, side_length):
        self.side_length = side_length #initalize side length
    def area(self):
        return self.side_length**2 #calculating area
    def perimeter(self):
        return 4 * self.side_length #calculating perimeter
square_1 = Square(10) #giving side length parameter to square_1
square_2 = Square(20) #giving side length parameter to square_2
#printing results of area and perimeter of square 1 & 2
print(f"The area of square 1 is: {square_1.area()}")
print(f"The perimeter of square 1 is: {square_1.perimeter()}")
print(f"The area of square 2 is: {square_2.area()}")
print(f"The perimeter of square 2 is: {square_2.perimeter()}")
