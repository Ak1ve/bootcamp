"""
This is meant as an Introduction to python coming from a Java background
"""

# In java, you would write a "Hello world" program like this:
"""
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!")
    }
}
"""

# In python, its simply:
print("Hello world!")

"""
A couple things to note:
    - Instead of `System.out.println` you only need to use `print`
    - You don't need to end statements with a ;
    - You don't need a class to run instructions
    - You don't need a method/function to run instructions

Python is not object-orientated.  It is considered a multi-paradigm langauge, but
we'll talk more about that in later lessons.  All that is important to note
is that it makes writing dcode easier.  

This is a general trend you will see in python as compared to many other
familiar languages: things generally are easier to write

As a trade off, however, the running speed of python is generally much slower
than other languages like Java.  100x slower give or take in some scenarios

But a big benefit is it becomes much easier to write in python!

Lets go over some other java conversions to python
"""


# to create a class:
class ClassName:
    ...


# to create a function:
def foo(bar):
    print(bar)


# This for loop in Java:

"""
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
"""
# Converts to this in python:
for i in range(10):
    print(i)

"""
A couple notes:
    - in python, {} arent used, instead a mix of tabs and : are used
    - python uses something called a `range` object in for-loops.  We'll 
    talk more about them later
    - the keyword `def` is used to *def-ine* a function.  The `foo`
    function is NOT a method, because it is not in a class.
   
Now lets take a simple Truck class in java and convert it to python  
"""
# Java:
"""
public class Truck {
    int numWheels;
    boolean isDriving;
    public Truck(int numWheels, boolean isDriving) {
        this.numWheels = numWheels;
        this.isDriving = isDriving;
    }
    
    public void drive() {
        this.isDriving = True;
    }
}
// in some class:
Truck abc = new Truck(4, true);
"""


# Python:
class Truck:
    def __init__(self, num_wheels, is_driving):
        self.num_wheels = num_wheels
        self.is_driving = is_driving

    def drive(self):
        self.is_driving = True


abc = Truck(4, True)


"""
Please note:
    - the `def __init__` line is used to declare a constructor.  It 
    *init-ializes* the object.
        - the reasoning for the "__" is used to define special-kinds of methods.
        These methods are called "dunder" methods (short for double underscore)
        but they are also known as magic methods because they are special function
        names that are used in special scenarios that are specific to python.  We'll
        talk more about them later. 
    - Python doesn't need to use types.  You dont need to declare a variable
    with specific types because python deduces the types at runtime, instead of
    "compile time."  Java does this at compile time.  This is the main reasoning
    behind the slowness of python.  It takes a lot more time to calculate types
    - Python uses the `self` parameter instead of `this`.  Each class method must have
    "self" as the first parameter
    - to create an instance of a class, you don't need to use the `new` keyword.
    - in python, the `public/private` keywords do not exist
    - boolean states are denoted with `True/False` instead of `true/false`
"""

"""
Now as you may notice, python has a couple other 000_session differences that are important
to note.
Comments:
    Line comments use `#` instead of `//`
    Multi-line comments use 3 " marks instead of `/* */`

Naming conventions:
    Python follows a different convention that java.  To name a variable
    that holds the number of wheels, you'd say: `num_wheels` and not `numWheels` 
    While you're allowed to use `numWheels` in python, it is not best practice
    and every library in python will use the underscores (known as snakecase)
    as opposed to varied capitals (known as camel case) 
"""

# Practice: convert the java program to python
"""

class Dog {
    boolean isBarking;
    int numEyes;
    public Dog(boolean isBarking, int numEyes) {
        this.isBarking = isBarking;
        this.numEyes = numEyes;
    }
    
    public void printEyes() {
        System.out.println(this.numEyes);
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog(false, 4);
        dog.printEyes();
    }
}
"""


# solution:

class Dog:
    def __init__(self, is_barking, num_eyes):
        self.is_barking = is_barking
        self.num_eyes = num_eyes

    def print_eyes(self):
        print(self.num_eyes)


dog = Dog(False, 4)
dog.print_eyes()
