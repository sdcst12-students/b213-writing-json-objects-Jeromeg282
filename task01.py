#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""

import json

assignments = []
assignment_scores = {}


def create_assignment(name, value):
    assignment_id = len(assignments)
    assignments.append({"id": assignment_id, "name": name, "value": value})
    assignment_scores[assignment_id] = {}
    return assignment_id

def enter_scores(assignment_id, student_scores):
    assignment_scores[assignment_id] = {i + 1: score for i, score in enumerate(student_scores)}

def get_assignment_by_id(assignment_id):
    return next((assignment for assignment in assignments if assignment["id"] == assignment_id), None)

def assignment_ui():
    name = input("Enter assignment name: ")
    value = float(input("Enter assignment value: "))
    assignment_id = create_assignment(name, value)
    print(f"Your assignment has been assigned ID {assignment_id}")

def scores_ui():
    assignment_id = int(input("Enter the assignment ID: "))
    assignment = get_assignment_by_id(assignment_id)
    if assignment:
        print(f"Enter the scores for 10 students for {assignment['name']}:")
        student_scores = [float(input(f"{i + 1}: ")) for i in range(10)]
        enter_scores(assignment_id, student_scores)
        print("Complete.")
    else:
        print("Assignment not found.")

def write_to_file():
    data = {"assignments": assignments, "assignment_scores": assignment_scores}
    with open("assignment_data.json", "w") as file:
        json.dump(data, file)

while True:
    print("1. Create an assignment\n2. Enter assignment scores\n3. Write your data to file")
    choice = input("Enter in your choice: ").strip()

    if choice == "1":
        assignment_ui()
    elif choice == "2":
        scores_ui()
    elif choice == "3":
        write_to_file()
        break
    else:
        print("Invalid choice.")






