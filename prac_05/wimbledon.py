"""
estimate: 40 mins
actual: 60 mins
"""

def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champions = get_champions(data)
    countries = get_countries(data)
    print_champions(champions)
    print()
    print_countries(countries)

def read_csv_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # start reading from the second line
        data = in_file.readlines()[1:]
        # split each line by commas and store in a list
        data = [line.strip().split(",") for line in data]
        return data

def get_champions(data):
    champions = {}
    for line in data:
        winner = line[2]
        if winner in champions:
            champions[winner] += 1
        else:
            champions[winner] = 1
    return champions

def get_countries(data):
    countries = set()
    for line in data:
        country = line[1]
        countries.add(country)
    return sorted(countries)

def print_champions(champions):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

def print_countries(countries):
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
