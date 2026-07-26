# A prime number is a positive number that has exactly two factors: 1 and itself.
num = int(input("Enter a Number: "))
Count = 0
for i in range(1, num  + 1):
    if num % i == 0 :
        Count+= 1
if Count == 2:
    print("Prime Number")
else:
    print("Not a prime Number")
