import random


class Car:
    def __init__(self, register, max_speed):
        self.register = register
        self.max_speed = max_speed
        self.speed = 0
        self.dist_travelled = 0

    def print_info(self):
        print(f"Auton {self.register} "
              f"huippunopeus on {self.max_speed} km/h, "
              f"matkamittari: {self.dist_travelled} km, "
              f"Tämänhetkinen nopeus: {self.speed} km/h.")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change <= self.max_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        if self.speed + speed_change > self.max_speed:
            self.speed = self.max_speed
        return self.speed

    def drive(self, time):
        for hour in range(time):
            self.dist_travelled += self.speed * time


car1 = Car("ABC-123", 142)
car2 = Car("ABC-2", 150)
car1.accelerate(60)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)
car1.print_info()

car1.drive(12)

cars = []
for i in range(10):
    cars.append(Car(f"ABC-" + str(i+1), random.randint(100, 200)))

racing = True
while racing:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.dist_travelled >= 10000:
            racing = False
            break

for car in cars:
    print("--------------------------------------------------------------------------------------------\n")
    car.print_info()
    print("")

print("--------------------------------------------------------------------------------------------")

