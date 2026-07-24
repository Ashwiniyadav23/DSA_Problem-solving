# Sort Students by Marks 
# Problem: Sort students in ascending order of marks.
# Input
# const students = [
#   { name: "A", marks: 90 },
#   { name: "B", marks: 70 },
#   { name: "C", marks: 85 }
# ];
# Output
# [
#   { name: "B", marks: 70 },
#   { name: "C", marks: 85 },
#   { name: "A", marks: 90 }
# ]
students = [
    {"name": "A", "marks": 90},
    {"name": "B", "marks": 70},
    {"name": "C", "marks": 85}
]

for i in range(len(students) - 1):
    for j in range(len(students) - 1 - i):
        if students[j]["marks"] > students[j + 1]["marks"]:
            students[j], students[j + 1] = students[j + 1], students[j]

print(students)