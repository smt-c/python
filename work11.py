# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Dog({self.name!r})"  # for developers

#     def __str__(self):
#         return f"My dog’s name is {self.name}"  # for users

# dog = Dog("Buddy")
# print(dog)        # calls __str__
# print(repr(dog))  # calls __repr__


class Example:
    def greet(self):
        print("Hello!")

obj = Example()
method = obj.greet

# print(method.__self__)  # the instance `obj`
# print(method.__func__)  # the original function object
print(method())  # the original function object
