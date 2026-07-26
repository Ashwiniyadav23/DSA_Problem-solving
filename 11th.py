# A factor is a number that divides another number without leaving any remainder. Both positive and negative numbers can have factors.

# N = int(input("Enter value of N: "))
# i = 1
# for i in range(1, N + 1):
#     if N % i == 0:
#         print(i)



N = int(input("Enter a number: "))

if N > 0:
    for i in range(1, N + 1):
        if N % i == 0:
            print(i)

elif N < 0:
    for i in range(-1, N - 1, -1):
        if N % i == 0:
            print(i)

else:
    print("0 has no factors.")