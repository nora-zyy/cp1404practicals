"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "".upper():
    while True:
        try:
            state = input("Enter short state:").upper()
            if state.lower() == 'quit':
                break
            capital = CODE_TO_NAME[state.upper()]
            print(f"{state.upper()} is {capital}")
        except KeyError:
            print("Enter short state: ")

    for state, capital in CODE_TO_NAME.items():
        print(f"{state} is {capital}")





