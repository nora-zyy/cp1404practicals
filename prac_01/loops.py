for i in range(1, 21, 2):
    print(i, end=' ')
print()


# a
for i in range(0, 100+1, 10):
    print(i, end=' ')
print()


# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()


# c
numbers = int(input("Number of stars:"))
while numbers < 0:
    print("Invalid Input")
    numbers = int(input("Number of stars:"))
else:
    for i in range(numbers):
        print("*", end="")
    print()


# d
numbers = int(input("Number of stars:"))
while numbers < 0:
    print("Invalid Input")
    numbers = int(input("Number of stars:"))
for i in range(numbers):
    i += 1
    print('*' * i)