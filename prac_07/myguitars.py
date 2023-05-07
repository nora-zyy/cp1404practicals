import csv
from prac_07.guitar import Guitar

def main():
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    guitar_data = csv.reader(in_file)

    while True:
        name = input("Name:")
        if name == "":
            break
        year = int(input("Year:"))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{name}({year}): ${cost:,.2f}\n")
    for name, year, cost in guitar_data:
        guitars.append(Guitar(name, int(year), float(cost)))

    in_file.close()
    guitars.sort()
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)



main()