#main.py
#Student Information & Grade Processing System

import utils
# from utils import *

def add_student():
    try:
        student_id=input("Enter Student ID (Format: S001): ")
        assert student_id.startswith("S"), "student ID must start with 'S'"

        

