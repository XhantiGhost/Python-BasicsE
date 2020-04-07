class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.w = 50
point2.z = 40
print(point2.w)


# Constructors

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
print(point1.x)


# Exercise
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hey dude iam {self.name}')


john = Person('John Smith')
bob = Person('Bob Smith')
print(bob.name)
print(john.name)
john.talk()


#Inheritence in classes
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('whofwhof')


class Cat(Mammal):
    def be_annonying(self):
        print('annoying')


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annonying()


import converters
from converters import lbs_to_kg
print(lbs_to_kg(70) )
print(converters.kg_to_lbs(70))