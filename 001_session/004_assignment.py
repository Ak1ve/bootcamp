"""
Refactor the following code:
"""


class Wheel:
    def __init__(self, position):
        self.Position = position

    def move_forwrd(self, unis):
        self.Position += unis

    def __repr__(self):
        return f"Wheel({self.Position})"


class Truck:
    def __init__(self, wheels):
        self.wheels = wheels

    def totalSize(self):
        total = 0
        for i in range(len(self.wheels)):
            total += self.wheels[i].size
        return total

    def mv_forward(self):
        for i in range(len(self.wheels)):
            self.wheels[i].Position += 4

    def __repr__(self):
        return f"Truck({self.wheels})"


class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def move_forward(self, wheels):
        self.wheels = wheels

    def __repr__(self):
        return f"Vehicle({self.wheels})"

wheels = []
for i in range(2, 50, 4):
    wheels.append(Wheel(i * 2))
truck = Truck(wheels)
print(truck)
vehicle = Vehicle(wheels)
truck.mv_forward()
vehicle.move_forward(wheels)
print(vehicle)
# tip: look into __repr__(self)
"""
Any of the code can change, but it must be sensible and the output must still be:
```
Truck([Wheel(4), Wheel(12), Wheel(20), Wheel(28), Wheel(36), Wheel(44), Wheel(52), Wheel(60), Wheel(68), Wheel(76), Wheel(84), Wheel(92)])
Vehicle([Wheel(8), Wheel(16), Wheel(24), Wheel(32), Wheel(40), Wheel(48), Wheel(56), Wheel(64), Wheel(72), Wheel(80), Wheel(88), Wheel(96)])
```
"""


# BONUS:  Convert this code:
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


val = []
for x in range(1000):
    if is_prime(x):
        val.append(x)