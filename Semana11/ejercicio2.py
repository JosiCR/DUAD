
class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__ (self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
    

    def add_passengers (self, Person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(Person)
            print(f"{Person.name} se subio al bus.")
        else:
            print("El bus esta lleno. No se pueden subir mas personas.")
    

    def remove_passenger(self, Person): 
        if Person in self.passengers:
            self.passengers.remove(Person)
            print(f"{Person.name} se bajo del bus")
        else:
            print(f"{Person.name} no esta en el bus")


Bus = Bus(5)

p1 = Person("Josias")
p2 = Person("Lucas")
p3 = Person("Nicole")
p4 = Person("Amanda")
p5 = Person("Sheryl")
p6 = Person("Josue")

Bus.add_passengers(p1)
Bus.add_passengers(p2)
Bus.add_passengers(p3)
Bus.add_passengers(p4)
Bus.add_passengers(p5)
Bus.add_passengers(p6)

Bus.remove_passenger(p2)
Bus.remove_passenger(p5)