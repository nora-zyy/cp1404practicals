MENU = """
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

LOWEST_SCORES = 0
HIGHEST_SCORES = 100
EXCELLENT_SCORES = 90
PASS_SCORES = 50

def main():
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = get_examination_level(score)
            print(f"score: {score} \nExamination level: {result}")
        elif choice == 'S':
            print('*' * int(score))

        print(MENU)
        choice = input(">>>").upper()

    print("Thank you!")


def get_valid_score():
    score = float(input("Entry score: "))
    while score < LOWEST_SCORES or score > HIGHEST_SCORES:
        print("Invalid score!")
        score = float(input("Entry score: "))
    return score


def get_examination_level(score):
    result = ""
    if score < LOWEST_SCORES or score > HIGHEST_SCORES:
        result = "Invalid score"
    else:
        if score > PASS_SCORES:
            result = "Passable"
        if score > EXCELLENT_SCORES:
            result = "Excellent"
    if score < PASS_SCORES:
        result = "Bad"

    return result


main()

