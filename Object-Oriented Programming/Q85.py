class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year) 
        self.battery_size = battery_size

    def car_info(self):
        base_info = super().car_info() 
        return f"{base_info}, Battery Size: {self.battery_size} kWh"
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = int(input("Enter the year of the car: "))
battery_size = int(input("Enter the battery size (in kWh) for the electric car: "))
car = Car(make, model, year)
electric_car = ElectricCar(make, model, year, battery_size)
print("\nCar Information:")
print(car.car_info())
print("\nElectric Car Information:")
print(electric_car.car_info()) 