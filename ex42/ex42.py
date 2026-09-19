## Animal наследует object
class Animal(object):
    pass

## Dog inherits Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has the "name" property
        self.name = name

## Cat inherits Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has the "name" property
        self.name = name

## Person inherits object
class Person(object):

    def __init__(self, name):
        ## Person has two properties: "name" and "pet", so Person is a composition of them
        self.name = name

        ## Person – композиция животного некоторого вида
        self.pet = None

## Employee inherits Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has the "name" property from Person, что за чудеса?
        super(Employee, self).__init__(name)
        ## Employee has the "salary" property
        self.salary = salary

## Fish inherits object
class Fish(object):
    pass

## Salmon inherits Fish
class Salmon(Fish):
    pass

## Halibut inherit Fish
class Halibut(Fish):
    pass


## barbos наследует Dog
barbos = Dog("Барбос")

## barsik is an instance of Cat
barsik = Cat("Барсик")

## mary is an instance of Person
mary = Person("Машка")

## now mary is a composition with pet = instance of Cat
mary.pet = barsik

## filka is an instance of Employee
filka = Employee("Филька", 120000)

## now filka is a composition with pet = instance of Dog
filka.pet = barbos

## flipper is an instance of Fish
flipper = Fish()

## crouse is an instance of Salmon
crouse = Salmon()

## harry is an instance of Halibut
harry = Halibut()