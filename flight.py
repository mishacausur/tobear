class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats() == 0:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
people = ['Jenny', 'Pussifer']

for person in people:
    if flight.add_passenger(person):
        print(f'added {person} to flight')
    else:
        print(f'No available for {person}')

