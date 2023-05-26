class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a cat. My name is {self.name}. I am {self.age} years old')

    def make_sound(self):
        print('meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a dog. My name is {self.name}. I am {self.age} years old')

    def make_sound(self):
        print("bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Rocky", 6)

for animal in (cat1, dog1):  # in first iteration animal = cat1, it prints cat1.info() and cat1.make_sound(). In second
    animal.info()            # iteration, animal = dog1, and do the same.
    animal.make_sound()
