# Problem: Find the first student whose submitted status is True.

# Input

students = [
    {"id": 1, "name": "Alice", "submitted": False},
    {"id": 2, "name": "Bob", "submitted": False},
    {"id": 3, "name": "Charlie", "submitted": True},
    {"id": 4, "name": "David", "submitted": True}
]

# Output

# {"id": 3, "name": "Charlie", "submitted": True}


for i in range(len(students)):
    if students[i]["submitted"]:
        print(students[i])
        break