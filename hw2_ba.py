import names as nm
import numpy as np
import time
import pandas as pd

# Random English Name Generator using names Module
def generate_random_name():
    return nm.get_full_name()

# Grade Calculation
def calculate_grade(grades):
    # Component 1 (50%)
    project = (
        grades['Proposal Presentation'] * 0.1 + 
        grades['Progress Presentation'] * 0.1 + 
        grades['Final Presentation'] * 0.1 + 
        grades['Final Report'] * 0.2
    )
    # Component 2 (20%)
    assignments = (
        grades['Homeworks'] * 0.1 + 
        grades['3D Games'] * 0.1
    )
    # Component 3 (30%)
    final_exam = grades['Final Exam'] * 0.3
    return project + assignments + final_exam

# Execution Time
def execution_time(func):
    start_time = time.time()
    result = func()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds\n")
    return result

# Distribution (Mean & STD)
def distribution():
    return {
        'Proposal Presentation': (88, 5), 
        'Progress Presentation': (90, 10), 
        'Final Presentation': (87, 7), 
        'Final Report': (90, 5),
        'Homeworks': (80, 15), 
        '3D Games': (78, 10), 
        'Final Exam': (80, 7)
    }

# Result
def show_results(student):
    print(f"\nStudent           : {student['Name']}")
    print(f"Grade Received    : {student['Total Grade']:.2f}")
    print("with Details")
    for component, grade in student['Grades'].items():
        print(f"     {component}: {grade:.2f}")

# Full Execution Mode
def full_execution_mode(num_students):
    print(f"Running full execution mode for {num_students} students...")

    grade_distribution = distribution()
    total_class_grade = 0
    students = []

    # Grade Calculation
    for _ in range(num_students):
        grades = {key: np.clip(np.random.normal(*grade_distribution[key]), 0, 100) for key in grade_distribution}
        student = {
            'Name': generate_random_name(),
            'Grades': grades,
            'Total Grade': calculate_grade(grades)
        }
        students.append(student)
        total_class_grade += student['Total Grade']
        show_results(student)

    # Summary
    class_average = total_class_grade / num_students
    print ('\n---------')
    print('\nSummary')
    print(f"Class Participation: {num_students} Students")
    print(f"Class Average Grade: {class_average:.2f}")

# Debugging Mode 
def debug_mode(filename):
    print(f"Running debug mode with data from {filename}...")

    # txt loader
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    data_lines = lines[1:]  # Skip header
    total_class_grade = 0
    students = []

    for line in data_lines:
        row = line.strip().split(',')
        grades = {
            'Proposal Presentation': float(row[1]),
            'Progress Presentation': float(row[2]),
            'Final Presentation': float(row[3]),
            'Final Report': float(row[4]),
            'Homeworks': float(row[5]),
            '3D Games': float(row[6]),
            'Final Exam': float(row[7])
        }
        student = {
            'Name': row[0],
            'Grades': grades,
            'Total Grade': calculate_grade(grades)
        }
        students.append(student)
        total_class_grade += student['Total Grade']
        show_results(student)

    # Summary
    class_average = total_class_grade / len(data_lines)
    print ('\n---------')
    print('\nSummary')
    print("Class Participation :{num_students} Students")
    print(f"Class Average Grade: {class_average:.2f}")

# Mode Selection
def main():
    mode = input("Enter mode (debug/full): ").strip().lower()

    if mode == 'full':
        num_students = int(input("Enter the number of students: "))
        execution_time(lambda: full_execution_mode(num_students))

    elif mode == 'debug':
        filename = 'random_students.txt'
        execution_time(lambda: debug_mode(filename))

    else:
        print("Invalid mode selected. Please choose 'full' or 'debug'")

# RUN!
if __name__ == "__main__":
    main()