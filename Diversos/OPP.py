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

print("-="*40)
print("MAGIC METHODS & OPERATOR OVERLOAD")
print("-="*40)

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

# More magic methods for common operators:

# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |

# The expression x + y is translated into x.__add__(y).
# However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
# There are equivalent r methods for all magic methods just mentioned.


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

# Python also provides magic methods for comparisons.
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=

# There are several magic methods for making classes act like containers.
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in

# There are many other magic methods that we won't cover here, such as __call__ for calling objects as 
# functions, and __int__, __str__, and the like, for converting objects to built-in types.

# Object Lifecycle

# The lifecycle of an object is made up of its creation, manipulation, and destruction.

# The first stage of the life-cycle of an object is the definition of the class to which it belongs.
# The next stage is the instantiation of an instance, when __init__ is called. 
# Memory is allocated to store the instance. Just before this occurs, the __new__ method of the class is called.
# This is usually overridden only in special cases.
# After this has happened, the object is ready to be used.

# When an object is destroyed, the memory allocated to it is freed up, and can be used for other purposes.
# Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object.
# If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted.

# In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well.
# The del statement reduces the reference count of an object by one, and this often leads to its deletion.
# The magic method for the del statement is __del__.
# The process of deleting objects when they are no longer needed is called garbage collection.
# In summary, an object's reference count increases when it is assigned a new name or placed in a container 
# (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, 
# its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches 
# zero, Python automatically deletes it.

a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>

# Data Hiding


# Weakly private methods and attributes have a single underscore at the beginning.
# This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention, and does not stop external code from accessing them.
# Its only actual effect is that from module_name import * won't import variables that start with a single underscore.

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

# Strongly private methods and attributes have a double underscore at the beginning of their names. 
# This causes their names to be mangled, which means that they can't be accessed from outside the class.
# The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses 
# that have methods or attributes with the same names.
# Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod 
# of class Spam could be accessed externally with _Spam__privatemethod.

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)

