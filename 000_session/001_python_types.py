"""
In java there are many types:
boolean, String, double, float, int, long, ArrayList, etc.

these are the corresponding python types:
bool, str, float, float, int, int, list

As you can see, an integer number is an int, regardless of size, and a decimal number is represented via float,
regardless of size.
"""

is_true = True  # bool
integer = 23_453_335_234 + 4444444444444444  # you can use _ for easy reading
floating_point = 3.3 * 3.683457239572308956723698476908245672945867
some_list = [2, 3, 4, 5, 6, 7]
some_text = "Some text"

# operations
num = 2
print(num + 1)
print(num - 1)
print(num * 2)

print(num / 3)  # 0.6666... NOT 0
print(num // 3)  # this is 0... floor division
print(num ** 3)  # 8, exponentiation
print((num + 2) % 3)  # 1, remainder


# now this is where this gets interesting...
print("a" * 3)  # aaa
print([2] * 4)  # [2, 2, 2, 2]


# conversions
string_number = "3.323"
print(float(string_number))

string_number = "3"
print(int(string_number))

num = 3
print(str(num) * 5)  # 33333


# if statements and boolean operators:
num = int(input("Enter a number"))
if num == 3:
    print("Equals 3")
elif num == 4:  # else if
    print("Equals 4")
else:
    print("Idk what it equals man")

if num > 0 and num % 2 == 0:
    print("The number is positive and even!")
elif -10 < num < 5:  # well isnt this nice?
    print("Num is between -10 and 5")
elif num == 0 or num == 99999999:
    print("Bruh")


"""
Exercise: Print through 1-100
    if the number is divisible by 3, print "Fizz"
    Otherwise, if the number is divisible by 5, print "Buzz"
    UNLESS if the number is divisible by both, print "FizzBuzz"
    If the number is not divisible by either, print the number 
Here's the first 16 outputs:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
Fun Fact:
This is a very well-known interview question for screening programming knowledge.
But why? Seems simple right?  Why don't we start with something you may have had:
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    if i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    if i % 5 != 0 and i % 3 != 0:
        print(i)


"""
While this works, if a potential employer saw this code, you would not hear back from them.
Not only is the code long, it is hard to read and contains redundant if conditionals.

In the first if statement, you see how we check if i % 3 == 0?  Then the next, we check if i % 3 != 0?
This is incredibly redundant.  Instead, use elif statements!
"""

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""
You see how much more concise that code is?  It's very readable, and doesnt contain redundant checks.
You can also see how `i % 3 == 0 and i % 5 == 0` was replaced with `i % 15 == 0`.  Just another way to write it, plus it 
clears up space.

But there's ONE MORE step that is important, which is why this code is used as a good beginner example
of coding interview questions.  What if your boss told you that you wanted "Fizz" to be printed when the number is 
divisible by 2 instead of 3.  "Easy" you think to yourself, so you rewrite it:
"""
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 2 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""
Uh oh!  Flaw.

You see, you forgot the original logic of the problem.  It must print FizzBuzz if both numbers are divisible.
But the first FizzBuzz to print out is at the number fifteen, not 5 * 2 = 10.  You computed logic in your own
for the sake of clarity that you code is now broken.

This is an albeit simple example.  But it's important to realize the importance of it.  If your code relies on 
something else, you should only have to change it once.
So the "best" code to write is this:
"""
FIZZ = 2
BUZZ = 5
for i in range(1, 101):
    if i % (FIZZ * BUZZ):
        print("FizzBuzz")
    elif i % FIZZ:
        print("Fizz")
    elif i % BUZZ:
        print("Buzz")
    else:
        print(i)

"""
By declaring these constants, you make your life easier.  You only have to change one number in the 
code and the logic is still the same.  
Plus, if you have to change the logic, you only have to change the one number and the entire program
changes!

This is the essence of good programming.  Keeping things in one place.
"""
