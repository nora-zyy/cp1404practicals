# 1.
OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, "w")
name = str(input("Enter Name: "))
print(name, file=out_file)
out_file.close()


# 2.
FILE_NAME = "name.txt"
in_file = open(FILE_NAME)
text = in_file.read().strip()
in_file.close()
print(f"Your name is {text}")


# 3.
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)


# 4.
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)