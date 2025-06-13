class person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__ (self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
    

    def add_passengers (self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} se subio al bus.")
        else:
            print("El bus esta lleno. No se pueden subir mas personas.")
    

    def remove_passenger(self, person): 
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} se bajo del bus")
        else:
            print(f"{person.name} no esta en el bus")


Bus = Bus(5)

p1 = person("Josias")
p2 = person("Lucas")
p3 = person("Nicole")
p4 = person("Amanda")
p5 = person("Sheryl")
p6 = person("Josue")

Bus.add_passengers(p1)
Bus.add_passengers(p2)
Bus.add_passengers(p3)
Bus.add_passengers(p4)
Bus.add_passengers(p5)
Bus.add_passengers(p6)

Bus.remove_passenger(p2)
Bus.remove_passenger(p5)