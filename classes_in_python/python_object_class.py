class Animal(object):
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal : Parent, Base
# Mammal : Child, sub


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
