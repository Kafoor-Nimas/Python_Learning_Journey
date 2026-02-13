#main.py
#Student Information & Grade Processing System

import utils 
from utils import *

def add_student():
    try:
        student_id=input("Enter Student ID (Format: S001): ")
        assert student_id.startswith("S"), "student ID must start with 'S'"

        name=input("Enter Student name: ")
        marks=int(input("Enter Marks (0-100): "))

        if marks <0 or marks >100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
        students=read_students()

        #Prevent Duplicate IDs
        for student in students:
            if student["id"] == student_id:
                print("Student ID already exists!")
                return
        
        add_student_to_file(student_id,name,marks)
        print("Student added successfully")

    except AssertionError as e:
        print("Error:",e)
    except InvalidMarksError as e:
        print("Error:",e)
    except ValueError:
        print("Marks must be a valid number.")

#View All Students
def view_students():
    students=read_students()

    if not students:
        print("No student record found.")
        return
    
    print("\n-- student Records --")
    for student in students:
        grade = calculate_grade(student["marks"])
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Grade: {grade}")
        print("-------------")

#Search student by ID

def search_student():
    search_id = input("Enter Student ID to search: ")
    students = read_students()

    for student in students:
        if student["id"] == search_id:
            grade =calculate_grade(student['marks'])
            print("\nStudent Found!")
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Grade: {grade}")
            return
    print("Student not found.")
