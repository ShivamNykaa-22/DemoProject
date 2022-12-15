class Car:
    attr1="Vehicle"
    attr2="sports_vehicle"

    def car_type(self):
        print("I'm a",self.attr1)
        print("I'm a",self.attr2)

Audi = Car()

print(Audi.attr1)
Audi.car_type()