class Elevator:
    def __init__(self, highest_floor, lowest_floor):
        self.highest_floor = highest_floor
        self.lowest_floor = lowest_floor
        self.floor = self.lowest_floor

    def move_to_floor(self, target_floor):
        while self.floor != target_floor:
            if target_floor > self.floor:
                self.floor_up()
            else:
                self.floor_down()
        #print(self.floor)

    def elevator_info(self):
        print(f"Elevator's highest floor: {self.highest_floor}")
        print(f"Elevator's lowest floor: {self.lowest_floor}")
        print(f"Elevator's current floor: {self.floor}\n")

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        self.floor -= 1


class House:
    def __init__(self, highest, lowest, amount):
        self.elevators = []
        self.highest = highest
        self.lowest = lowest
        self.amount = amount

        for i in range(amount):
            e = Elevator(highest, lowest)
            self.elevators.append(e)

    def fire_alarm(self):
        for i in self.elevators:
            i.move_to_floor(i.lowest_floor)

    def print_info(self):
        print(f"Korkein kerros: {self.highest} Alin kerros: {self.lowest} Hissien määrä: {self.amount}")

    def ride_elevator(self, selected_elevator, target_floor):
        elevator = self.elevators[selected_elevator - 1]
        elevator.move_to_floor(target_floor)
        for i in self.elevators:
            i.elevator_info()


h = House(6, 1, 3)
h.print_info()
h.ride_elevator(2, 5)
h.fire_alarm()

