# Problem:   You are given a list of student records. Each record contains an id and a name. Find the name of the student with the given ID.

# Input: 102
# Output: Bob

students = [
    {"id": 101, "name": "Alice"},
    {"id": 102, "name": "Bob"},
    {"id": 103, "name": "Charlie"}
]


def students_details(student_id):
    for i in range(len(students)):
        if(students[i]["id"] == student_id):
            print(f"Result: {students[i]["name"]}")
       
Input = int(input("Enter your Input: "))
students_details(Input)