# Problem: Print all student names starting from the last student.

# Input

students = [
  { id: 1, "name": "Alice" },
  { id: 2, "name": "Bob" },
  { id: 3, "name": "Charlie" }
]

# Output

# Charlie
# Bob
# Alice

for i in range(len(students)):
    print(students[len(students) - 1 - i]["name"])