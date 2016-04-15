class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        pass

    def printself(self):
        print 'age:', self._age, 'name:', self._name

    def setname(self, name):
        self._name = name


bart = Student('steve Yan', 22)

bart.printself()

bart.setname('hello')

bart.printself()


class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def run(self):
        print 'Dog is running'


class Cat(Animal):
    def run(self):
        print 'Cat is running'


animal = Animal()
animal.run()
dog = Dog()
dog.run()
cat = Cat()
cat.run()

print isinstance(dog, Animal)
print isinstance(cat, Animal)
print isinstance(animal, Dog)


def multi(a):
    a.run()


multi(animal)
multi(dog)
multi(cat)


class Teacher(object):
    def __index__(self):
        pass

    # only these attr
    _slots_ = ('name', 'age')


teahcer = Teacher()
teahcer.name = 'steve teahcer'
print teahcer.name


