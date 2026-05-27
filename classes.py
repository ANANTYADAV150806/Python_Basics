class Dog:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name}says Woof!"
dog1 = Dog("Buddy","Golden Retriever")
dog2 = Dog("Luna","French Bulldog")
print(dog1.name)
print(dog2.breed)
print(dog1.bark())
print(dog2.bark())