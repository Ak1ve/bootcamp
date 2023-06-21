"""
For Monday's assignment, I asked for you to read up about dictionaries.

a dictionary, or dict for short, is a way of storing similar data.

Let's say I declare some variables:
"""
# the (number, number, number) is called a tuple.  It's basically a list, but more suitable for colors.
# We'll cover another time
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
"""
I could then use these variables like this:
``draw_circle(PURPLE)``

Great!  Super easy to read and I dont have to worry about mental load.
But what is the problem for this?  Well let's say I have a character named "Violet"
and her character information is stored like this: 
"""
VIOLET = Character("Violet")
"""
Then if I do this:
``draw_circle(VIOLET)``
The code looks like im drawing a VIOLET color, but in fact I am not.
This is where dictionaries shine.

If you have a group of colors, declare them like this:
"""
COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "PURPLE": (255, 0, 255),
    "VIOLET": (255, 10, 255)
}
"""
*Please note that {} is used to declare a dictionary, not a code block.  {} is
ONLY used for dictionary (and sets but we'll talk about that later)*

Now what we can do is have the ``VIOLET = Character("Violet")`` in our code but
still allow for ourselves to use colors!  You can access the colors like this:
"""
draw_circle(COLORS["RED"])
COLORS["WHITE"] = (255, 255, 255)  # Adding a new value
"""
Nice!.  We still represent the same data, but now we only have one, concise variable
as opposed to 5.

Let's talk about another important use-case.

Consider this code:
"""
string = "1234567890"
for char in string:
    if char == "1":
        print("ONE")
    elif char == "2":
        print("TWO")
    elif char == "3":
        print("THREE")
    elif char == "4":
        print("FOUR")
    elif char == "5":
        print("FIVE")
    elif char == "6":
        print("SIX")
    elif char == "7":
        print("SEVEN")
    elif char == "8":
        print("EIGHT")
    elif char == "9":
        print("NINE")
    elif char == "0":
        print("ZERO")

"""
Simple enough right?  But my god is it noisy.  AND SLOW.  If char == "0",
then that means that it has to do 9 other if-statements before it reaches
the right pathway.
Let's use a dictionary
"""
NUMBERS = {
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE",
    "0": "ZERO",
}

for char in string:
    print(NUMBERS[char])

"""
Much much easier to understand.  And more readable.
To give a little insight into how this works:
* the in-depth version is kind of difficult to explain, so this
* explanation is a rough-version
dictionaries are like alphabetical tables.
it takes what are the "keys" ("RED", "GREEN", "BLUE", etc. in our COLORS example) and maps
them to a "value" ( (255, 0, 0), etc.).
like a real dictionary, you don't need to go through every single word, or "key", to find
what you're looking for.  Instead, you just need to know what letter it starts with
and then know the alphabetical order of the word list.
So if you're on the page "Plum" you know you need to skip several pages before you
come across "Red".  This is much faster than checking every single entry, like the if-statement
example we did.

Dictionaries are also called "maps" because it "maps" one value to another.
"""

"""
Exercise:
Create a dict, ``people`` that maps these first names to people's last names (i.e: John Doe's
entry would be "John": "Doe"):
    John Doe,
    Alex Smith,
    Jane Alex
    Robert Smith,
    John Limejuice

Here's the solution:
"""
people = {
    "John": "Doe",
    "Alex": "Smith",
    "Jane": "Alex",
    "Robert": "Smith",
    "John": "Smith"
}

# Now let's test the first Name.  John Doe.
print(people["John"])  # outputs Smith
"""
???
As you can see, the name "John" maps to TWO different last names: "Smith" and "Doe".
A dictionary cannot map to two values at once, therefore "Doe" is deleted!
A "value" can have multiple "keys", however.
i.e. "Alex" -> "Smith" and "Robert" -> "Smith" is no problem.
"""