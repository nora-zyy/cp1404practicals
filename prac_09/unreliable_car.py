from car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        choice_number = random.randint(0, 100)
        if choice_number < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0
