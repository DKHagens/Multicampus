# 다형성(polymorhism)

class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method') #추상 메소드? 틀만 만들어둠

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'woof woof!'

animals = [Cat('missy'), Cat('Mr.mistoffelees'), Dog('zion')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())

