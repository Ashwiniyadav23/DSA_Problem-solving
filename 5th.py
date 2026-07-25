# Problem

# Count how many students are enrolled in each course.

# Input

students = [
  { "name": "A", "course": "MERN" },
  { "name": "B", "course": "Python" },
  { "name": "C", "course": "MERN" }
]

# Output

# {
#   MERN: 2,
#   Python: 1
# }

c = 0
obj = {}
for i in range(len(students)):
    for j in range(len(students)):
        if(students[j]["course"] == students[i]["course"]):
            c += 1
    obj[students[i]["course"]] = c
    c = 0
print(obj)