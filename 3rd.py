# Find the Highest Salary 
# Problem: You are given a list of employee salaries. Find the highest salary.
# Input: salaries = [25000, 40000, 35000, 50000, 45000]
# Output: 50000


salaries = [25000, 40000, 35000, 50000, 45000]
largest = 0
for i in range(len(salaries) -1):
        if salaries[i] > largest:
            largest = salaries[i]
print(largest)