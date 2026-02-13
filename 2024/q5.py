#Q5.py

def calculate_grade(marks):
    if 90<= marks <=100:
        return "A"
    elif 80<= marks <=89:
        return "B"
    elif  70<= marks <=79:
        return "C"
    elif  60<=marks <=69:
        return "D"
    else:
        return "F"
    
num_students=int(input("Enter number of students: "))

students = {}

for i in range(num_students):
    name=input("Enter student name: ")
    marks = int(input("Enter marks: "))
    grade=calculate_grade(marks)
    students[name] =grade

print("\nStudents Grade Report:")
for name, grade in students.items():
    print(f"Name: {name}, Grade: {grade}")