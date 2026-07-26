# Problem: You are given an array of user objects. Move all users whose isActive is false to the end of the array. Keep the active users at the beginning.

# Input

users = [
    {"id": 1, "name": "Alice", "isActive": True},
    {"id": 2, "name": "Bob", "isActive": False},
    {"id": 3, "name": "Charlie", "isActive": True},
    {"id": 4, "name": "David", "isActive": False}
]

# Output

# [
#     {"id": 1, "name": "Alice", "isActive": True},
#     {"id": 3, "name": "Charlie", "isActive": True},
#     {"id": 2, "name": "Bob", "isActive": False},
#     {"id": 4, "name": "David", "isActive": False}
# ]


write = 0

for read in range(len(users)):
    if users[read]["isActive"]:
        users[read], users[write] = users[write], users[read]
        write += 1

print(users)

