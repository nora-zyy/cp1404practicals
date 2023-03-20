"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

LOW_LIMIT = 0
HIGH_LIMIT = 100
score = float(input("Enter score: "))
if score < LOW_LIMIT or score > HIGH_LIMIT:
    print("Invalid score")
else:
    if score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    elif score < 50:
        print("Bad")


