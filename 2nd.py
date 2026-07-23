# Problem: A database contains employee IDs. Count how many times each employee ID appears.

# Input

# ids = [101, 102, 101, 103, 102, 101]

# Output
# {
#     101: 3,
#     102: 2,
#     103: 1
# }

ids = [1,2,3,2,2,3,1]

count = 0
obj = {}

for i in range(len(ids)):
    for j in range(len(ids)):
        if ids[j] == ids[i]:
            count = count + 1
    obj[ids[i]] = count
    count = 0
print(obj)