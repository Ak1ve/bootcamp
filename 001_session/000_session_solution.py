"""
The previous session asked for the following code to work:

```
dog = Dog("Fiedo", "Brown")
dog.bark()
print(dog.fur_color)

cat = Cat("Lily", "Calico")
cat.meow()
print(cat.name)

same_dog = Dog("Fiedo", "Brown")
different_dog = Dog("Max", "Orange")

print(same_dog == dog)
print(dog == different_dog)
```
with the output:
```
Bark!
Brown
Meow!
Lily
True
False
"""


# you may have created the following classes:
class Dog:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

    def bark(self):
        print("Bark!")


class Cat:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

    def meow(self):
        print("Meow!")


dog = Dog("Fiedo", "Brown")
dog.bark()
print(dog.fur_color)

cat = Cat("Lily", "Calico")
cat.meow()
print(cat.name)

same_dog = Dog("Fiedo", "Brown")
different_dog = Dog("Max", "Orange")

print(same_dog == dog)
print(dog == different_dog)
"""
However, this code has a few problems.  Firstly, if you run the code, you don't get the expected output.
Specifically, ``same_dog == dog`` prints out as False.  But they have the same name and fur_color!
This is because they don't have the ``__eq__(self, other)`` method declared.  More on that later.

Additionally, the code has a cat and a dog with the same attributes: name and fur_color.
You should extract the similar characteristics into a base class ``Animal``

Here's how inheritance functions in python
"""


class Animal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color

    def print_animal(self):
        print(self.name, "is an Animal")

    def __eq__(self, other):  # "equals"
        return self.fur_color == other.fur_color and self.name == other.name


class Cat(Animal):
    def meow(self):
        print("Meow!")

    def print_animal(self):
        print(self.name, "is a Cat")


class Dog(Animal):
    def bark(self):
        print("Bark!")

    def print_animal(self):
        print(self.name, "is a Dog")


class Jaguar(Animal):
    def __init__(self, name, fur_color, speed):
        super().__init__(name, fur_color)
        self.speed = speed

    def rawr(self):
        print("Rawr! xD")  # yikes

    def print_animal(self):
        print(self.name, "is a Jaguar")


print(same_dog == dog)  # now this Works!
print(dog == different_dog)
"""
A couple notes:
    - To derive from a parent class, you declare a class and wrap the parent in parens ().
    - You don't need to access variables from "super". So instead of accessing a parent attribute like this in java:
            ``print(super.name, "is a Jaguar")``
            you would just do
            ``print(self.name, "is a Jaguar")``
    - Python uses ``super()`` instead of `super`.  To access a parent function, you call ``super()`` then you give the function name
        ``super().__init__(name, fur_color)``
        - Please note you don't pass in `self` as a parameter.
    - We have declared another dunder/magic method:  ``__eq__``.
        - Magic or dunder methods are special functions that python calls when using special syntax.  In this example,
        python converts ``print(same_dog == dog)`` into ``print(same_dog.__eq__(dog))``.  Try it yourself!  You'll
        see that it produces the same thing.  The ``__eq__`` method can be declared to denote instances in which
        you want objects to be considered equal to each other.  Sometimes it is every single property in the class,
        other times it is not.
        - We'll talk more about dunder methods later in this session
"""