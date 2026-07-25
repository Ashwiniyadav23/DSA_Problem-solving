# Problem: Reverse only the names while keeping the IDs in the same order.

# Input

students = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Output

# [
#   { id: 1, name: "Charlie" },
#   { id: 2, name: "Bob" },
#   { id: 3, name: "Alice" }
# ]
left = 0
right = len(students) - 1

while left < right:
    students[left]["name"], students[right]["name"] = (
        students[right]["name"],
        students[left]["name"]
    )

    left += 1
    right -= 1

print(students)