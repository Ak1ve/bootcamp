"""
Create An `Animal` class that has a name field and a fur_color field

In addition, create two classes `Dog` and `Cat` such that the following code works:
"""

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
The Output should be:
```
Bark!
Brown
Meow!
Lily
True
False
```

Then read up on the following:
https://www.techbeamers.com/python-list/
https://realpython.com/python-dicts/
"""