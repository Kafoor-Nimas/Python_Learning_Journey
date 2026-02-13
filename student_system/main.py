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


#Class Statistics
def class_statistics():
    students=read_students()

    if not students:
        print("No data available.")
        return
    
    marks_list=[]
    for student in students:
        marks_list.append(student["marks"])

    total=calculate_total_recursive(marks_list)
    average=total/len(marks_list)

    highest = find_highest(marks_list)
    lowest = find_lowest(marks_list)

    print("\n--- Class Statistics ---")
    print("Average Marks:",round(average,2))
    print("Highest Marks:",highest)
    print("Lowest Marks:",lowest)

#Main Menu
def main():
    while True:
        print("\n==== Student Information system ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. search students")
        print("4. Class Statistics")
        print("5. Exit")

        choice=input("Enter Your chice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

#"Only run the main() function if this file is executed directly."

#Program Entry Point
if __name__ =="__main__":
    main()