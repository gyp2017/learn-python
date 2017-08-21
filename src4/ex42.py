# -*- coding: utf-8 -*-
# 42 is-a, has-a 객체, 클래스

## Animal은 object의 일종이다. (is-a) 추가 점수 부분을 살펴보세요.
class Animal(object):
    pass

## Dog은 Animal의 일종이다. (is-a)
class Dog(Animal):

    def __init__(self, name):
        ## Dog은 어떤 종류의 name을 갖고 있다. (has-a)
        self.name = name

## Cat은 Animal의 일종이다. (is-a)
class Cat(Animal):

    def __init__(self, name):
        ## Cat은 어떤 종류의 name을 갖고 있다. (has-a)
        self.name = name

## Person은 object의 일종이다. (is-a)
class Person(object):

    def __init__(self, name):
        ## Person은 어떤 종류의 name을 갖고 있다. (has-a)
        self.name = name

        ## Person은 어떤 종류의 pet을 갖고 있다. (has-a)
        self.pet = None

## Employee는 Person의 일종이다. (is-a)
class Employee(Person):

    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
        ## Employee는 어떤 종류의 salary를 갖고 있다.
        self.salary = salary

## Fish는 object의 일종이다. (is-a)
class Fish(object):
    pass

## Salmon는 Fish의 일종이다. (is-a)
class Salmon(Fish):
    pass

## Halibut는 Fish의 일종이다. (is-a)
class Halibut(Fish):
    pass

## rover는 Dog의 일종이다. (is-a)
rover = Dog("Rover")

## satan은 Cat의 일종이다. (is-a)
satan = Cat("Satan")

## mary는 Person의 일종이다. (is-a)
mary = Person("Mary")

## mary는 satan 종류의 pet을 갖고 있다. (has-a)
mary.pet = satan

## frank는 Employee의 일종이다. (is-a)
frank = Employee("Frank", 120000)

## frank는 rover 종류의 pet을 갖고 있다.(has-a)
frank.pet = rover

## flipper는 Fish의 일종이다. (is-a)
flipper = Fish()

## crouse는 Salmon의 일종이다. (is-a)
crouse = Salmon()

## harry는 Halibut의 일종이다. (is-a)
harry = Halibut()
