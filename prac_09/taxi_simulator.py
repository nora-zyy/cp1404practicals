from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").upper()
    while choice != 'Q':
        if choice == 'C':
            print("Taxis available: ")
            for index in range(len(taxis)):
                print(f"{index} - {taxis[index]}")
            choose_taxi = int(input("Choose taxi: "))
            if choose_taxi < 0 or choose_taxi > len(taxis) - 1:
                print("Invalid taxi choice")
            current_taxi = taxis[index]

        elif choice == 'D':
            if current_taxi == None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far?"))
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                total_cost += current_taxi.get_fare()

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>>").upper()

    print(f"Total trip cost: ${total_cost}")
    print("Taxis are now:")
    for taxi in taxis:
        print(taxi)


main()