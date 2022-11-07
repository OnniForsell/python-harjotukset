import random


class Car:
    def __init__(self, register, top_speed):
        self.register = register
        self.top_speed = top_speed
        self.speed = 0
        self.dist_travelled = 0

    def print_info(self):
        print(f"Auton {self.register} matkamittari näyttää että se kulki {self.dist_travelled} km")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change <= self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        if self.speed + speed_change > self.top_speed:
            self.speed = self.top_speed
        return self.speed

    def drive(self, time):
        for hour in range(time):
            self.dist_travelled += self.speed * time


class ElectricCar(Car):
    def __init__(self, register, top_speed, battery):
        self.battery = battery
        super().__init__(register, top_speed)


class GasCar(Car):
    def __init__(self, register, top_speed, gas):
        self.gas = gas
        super().__init__(register, top_speed)


car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = GasCar("ACD-123", 165, 32.3)

car1.accelerate(10)
car1.drive(3)
car1.print_info()

car2.accelerate(20)
car2.drive(3)
car2.print_info()
