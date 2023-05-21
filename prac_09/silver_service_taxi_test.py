from silver_service_taxi import SilverServiceTaxi

def main():
    my_silver_taxi = SilverServiceTaxi("Humer", 200, 2)
    print(my_silver_taxi)

    my_silver_taxi.drive(18)
    print(my_silver_taxi)
    print(my_silver_taxi.get_fare())

main()