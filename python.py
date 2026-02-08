
# Classes & Objects (Basics)
# 🔹 What is a Class?
# A class is a blueprint (design).

# 🔹 What is an Object?
# An object is a real thing created from a class.
"""
class Person:
    name = "RK"
    age = 24

    

 p1 = Person()  #  creating a object here 
print(p1.name)
print(p1.age)

"""
#  _init_ Method(Constructor)

# What is _init_
# Automatically runs when object is created

# Used to initialize values
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person( "Rk" , 24)
p2 = Person("vignesh" , 35)

print(p1.name, p1.age)
print(p2.name, p2.age)
"""

#  Methods in Class
# 🔹 What is a Method?
# A function inside a class
"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p = Person("RK")
p.greet()
"""

# Inheritance (Parent -> child)
# Child class inherits properties and methods from parent class.
"""
class Parent:
    def Familyname(self):
        print("Perants familyname is katravath")
class Child(Parent):
    def job(self):
        print("get own job ")

d = Child()
d.Familyname()
d.job()
"""

# Encapsulation (Data Protection)
# Protect sensitive data (passwords, balance)

"""
class Bank:
    def __init__(self):
        self.name = "RK"       # public
        self._branch = "SBI"   # protected
        self.__balance = 5000  # private

    def show_balance(self):
        print(self.__balance)

b = Bank()
print(b.name)
print(b._branch)
b.show_balance()
"""

# Exception Handling
# 🔹 What is an Exception?
# An error that stops program execution
"""
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Program finished")

"""

# raise (Custom Error)
"""
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18+")
print("Eligible")

"""
