#utils.py
#Helper function for student Information & Grade Processing System

#Custom Exception for Invalid marks

class InvalidMarksError(Exception):
    pass

#Grade calculation function

def calculate_grade(marks):
    if marks >=75:
        return "A"
    elif marks >=65:
        return "B"
    elif marks >=55:
        return "C"
    elif marks >=45:
        return "S"
    else:
        return "F"
        

#Recursive function to Calculate Total

def calculate_total_recursive(marks_list):
    if len(marks_list) == 0:
        return 0
    return marks_list[0] + calculate_total_recursive(marks_list[1:])

