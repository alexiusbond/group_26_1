class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Car(Transport):
    number_of_wheels = 4  # class attribute

    def __init__(self, the_model, the_year, the_color, penalties=0):  # constructor
        # attributes / fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties

    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    number_of_wheels = 10
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, type, weight):
        if weight > self.load_capacity:
            print(f'Can not load cargo more than {self.load_capacity}')
        else:
            print(f'Cargo of {type} {weight} kg was successfully loaded on truck')


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)


bmw_car = Car('BMW X7', 2020, 'White')
print(bmw_car)
print(f'Model: {bmw_car.model} year: {bmw_car.year} color: {bmw_car.color} '
      f'penalties: {bmw_car.penalties}')

honda_car = Car(the_year=2019, the_model='Honda Civic', the_color='Red', penalties=900)
print(f'Model: {honda_car.model} year: {honda_car.year} color: {honda_car.color} '
      f'penalties: {honda_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Tokmok')
# honda_car.color = 'Green'
honda_car.change_color('Green')
print(f'Model: {honda_car.model} year: {honda_car.year} color: {honda_car.color} '
      f'penalties: {honda_car.penalties}')

print(f'We need {Car.number_of_wheels * 10 * 5000} soms for winter lastics')

Car.number_of_wheels = 5
print(f'We need {Car.number_of_wheels * 10 * 5000} soms for winter lastics')

boeing_plane = Plane('Boeing 737', 2022, 'Blue')
print(f'Model: {boeing_plane.model} year: {boeing_plane.year} color: {boeing_plane.color}')

man_truck = Truck('Man 60', 2009, 'Black', 1000, 25000)
print(f'Model: {man_truck.model} year: {man_truck.year} color: {man_truck.color} '
      f'penalties: {man_truck.penalties} load capacity: {man_truck.load_capacity}')
man_truck.load_cargo('Apples', 30000)
man_truck.load_cargo('Potatoes', 20000)
man_truck.drive('LA')

print(f'{Truck.number_of_wheels}')