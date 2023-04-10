import random

MINIMUM = 1
MAXIMUM = 45
QUICKPICK_QUANTITY = 6

def main():
    quickpicks_number = int(input("How many quick picks? "))
    quickpicks = []
    for i in range(quickpicks_number):
        quickpick = generate_quickpick()
        quickpicks.append(quickpick)

    for quickpick in quickpicks:
        for number in quickpick:
            print(f"{number:2d}", end=" ")
        print()

def generate_quickpick():
    numbers = []
    while len(numbers) < QUICKPICK_QUANTITY:
        number = random.randint(MINIMUM, MAXIMUM + 1)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)


main()

