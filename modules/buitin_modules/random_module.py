import random

print(dir(random))
# random.seed(0)  # sets a seed value. I destroys randomness
print(random.random())  # prints random number between 0 and 1
print(random.randint(1, 10))  # prints random number in the range. right side included.
print(random.randrange(1, 10, 2))  # arguments are range and step size. right range excluded.

my_list = [5, 10, 15, 20, 25, 30, 35]
print(random.choice(my_list))
print(random.sample(my_list, 3))
