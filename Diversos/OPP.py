# Objects are created using classes, which are actually the focal point of OOP.
# The class describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object's blueprint, description, or definition.
# You can use the same class as a blueprint for creating multiple different objects.

# Classes are created using the keyword class and an indented block, which contains class methods (which are functions).

class Felino:
  def __init__(self,name,color):
    self.legs = 4
    self.tails = 1
    self.name = name
    self.color = color
  
  def noise(self):
    print("miu")

class Cat(Felino):
  def noise(self):
    print("Miauuuu")

class Leao(Felino):
  def noise(self):
    print("Hurrrrr")

class Domestico(Cat):
    def noise(self):
      print("miumiu")
      super().noise()

felix = Cat("Felix","ginger")
rover = Domestico("Rover","dog-colored")
stumpy = Leao("Stumpy","brown")

print(felix.name)
print(rover.color)
print(stumpy.legs)
print(felix.tails)
felix.noise()
rover.noise()
stumpy.noise()

# This code defines a class named Cat, which has two attributes: color and legs.
# Then the class is used to create 3 separate objects of that class.
# Tap Continue to learn more!

# All methods must have self as their first parameter, although it isn't explicitly passed, 
# Python adds the self argument to the list for you; you do not need to include it when you call the methods. 
# Within a method definition, self refers to the instance calling the method.

# Instances of a class have attributes, which are pieces of data associated with them.
# In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, 
# and the attribute name after an instance.
# In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.

# Classes can also have class attributes, created by assigning variables within the body of the class. 
# These can be accessed either from instances of the class, or the class itself.

# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on. 
# Although they may differ in some ways (only Dog might have the method bark), 
# they are likely to be similar in others (all having the attributes color and name).
# This similarity can be expressed by making them all inherit from a superclass Animal, 
# which contains the shared functionality.
# To inherit a class from another class, put the superclass name in parentheses after the class name.

# If a class inherits from another with the same attributes or methods, it overrides them.

# Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class.

# The function super is a useful inheritance-related function that refers to the parent class. 
# It can be used to find the method with a certain name in an object's superclass.

# Magic methods are special methods which have double underscores at the beginning and end of their names.
# They are also known as dunders.
# So far, the only one we have encountered is __init__, but there are several others.
# They are used to create functionality that can't be represented as a normal method.

# One common use of them is operator overloading.
# This means defining operators for custom classes that allow operators such as + and * to be used on them.
# An example magic method is __add__ for +.

print("-="*60)
print("MAGIC METHODS & OPERATOR OVERLOAD")
print("-="*60)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)