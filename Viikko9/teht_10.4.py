import random


class Race:
    def __init__(self, race_name, race_distance, racers):
        self.race_name = race_name
        self.race_distance = race_distance
        self.racers = racers

    def hour_passes(self):
        for car in self.racers:
            car.accelerate(random.randint(-10, 15))
            car.travel_distance(1)

    def print_status(self):
        print("-----------------------------------------------------------------------------------------------")
        for car in self.racers:
            car.print_info()
            print("-----------------------------------------------------------------------------------------------")

    def race_over(self):
        for car in self.racers:
            if car.distance >= self.race_distance:
                return True
        return False


class Car:
    def __init__(self, register, max_speed):
        self.register = register
        self.max_speed = max_speed
        self.distance = 0
        self.speed = 0
        self.hours = 0

    def print_info(self):
        print(f"Auton {self.register} "
              f"huippunopeus on {self.max_speed} km/h, "
              f"matkamittari: {self.distance} km, "
              f"Tämänhetkinen nopeus: {self.speed} km/h.")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        else:
            self.speed = self.max_speed

    def print_currentspeed(self):
        print(f"The speed of the car is {self.speed} km/h.")

    def travel_distance(self, hours):
        self.distance = self.distance + (self.speed * hours)
        self.hours = self.hours + hours


def create_car():
    cars = []
    for x in range(10):
        cars.append(Car("ABC-" + str(x + 1), random.randint(100, 200)))
    return cars

hour = 0
cars = create_car()
race = Race("Suuri Romuralli", 8000, cars)
race.print_status()
while not race.race_over():
    race.hour_passes()
    hour += 1
    if hour % 10 == 0:
        print(f"{hour} hours have passed.")
        race.print_status()

print("\n")
print(f"After {hour} hours the race is over! Here are the results:")
race.print_status()
for car in race.racers:
    if car.distance >= race.race_distance:
        print(f"{car.register} wins the race!")