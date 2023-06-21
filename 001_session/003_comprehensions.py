"""
Comprehensions are almost never taught in introductory python courses.
They are generally saved for much longer in time, but I think it is important
to understand them as it is the basis for much more complex topics,
such as generators and functional programming.

So let's start with something easy:
"""

some_list = list(range(10))
print(some_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# this is much easier than writing:
some_list = []
for i in range(10):
    some_list.append(i)  # hopefully you've read about this

"""
While list(range(10)) is nice, it is very restrictive.
What if we want a list of even numbers?

This is where comprehensions really shine.

List comprehensions are a way of "spelling" out how the list is created 
"""

some_list = list(i for i in range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# it's saying that for every element i in range of 0->10, the next element is equal to i

# now let's try another one:
other_list = list(i * 2 for i in range(10))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# For every element i within 0->10, the next element is equal to i * 2.

# so if we were to say we want a list of the first 10 even numbers (including zero), we write:
evens = list(i * 2 for i in range(10))
# instead of:
evens = []
for i in range(10):
    evens.append(i * 2)
"""
This is much easier!

let's make it more complicated.  Let's say we want a list of numbers:"""
numbers = [1, 2, 3]
"""
and we want to double each element in the list
we could do this:
"""
for i in range(len(numbers)):
    numbers[i] *= 2
# or we could do this:
numbers = [number * 2 for number in numbers]
"""
Note: We used [] instead of list().  This is the same thing.

Here is the final component of comprehensions
"""

list_of_evens = []
for i in range(100):
    if i % 2 == 0:
        list_of_evens.append(list_of_evens)

# this is the same as:
list_of_evens = [i for i in range(100) if i % 2 == 0]

"""
Don't be overwhelmed.  This is hard to get used to, but this is vital in understanding higher concepts

Convert the following for-loop into a list comprehension:
"""
odd_squares = []
for i in range(100):
    if i % 2 == 1:
        odd_squares.append(i ** 2)
total = 0
for number in odd_squares:
    total += number
"""
This would turn into:
"""

odd_squares = [i ** 2 for i in range(100) if i % 2 == 1]
total = sum(odd_squares)
