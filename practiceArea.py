# Learned from https://www.youtube.com/watch?v=I2wURDqiXdM&list=PLcMUlx_U6bJo4dJK6VxaB8JDw_nvU2jj6&index=3

# comment for one line code
""" My comment """
x = 2 + 1
print(x)

a = "Wazzap!!!"
print(a)
print("-----------------------------------------------")

# an example of list ---------------------------------------------------
b = ["Wazzap!!!", "Apa khabar!!!"] 
#print(b[0]) #output Wazzap!!!
#print(b) #output the list of b

b = b + [1,2,3,4]
print(b)
print("-----------------------------------------------")

# an example of dictionaries -------------------------------------------
# Every dictionaries have a name that we call a key

c = {"favcolor":"purple and blue"} 
print(c["favcolor"]) #associative array
print("-----------------------------------------------")

# an example of set ----------------------------------------------------
# set doesnt have order and repitition

d = {1,2,3,4,5,5,5,6,6,6}
print(d)
# can be add logic
x=2
y=2
if x==2:
    print("of course!")
if y==2:
    print("Obviously not!")
print("-----------------------------------------------")

# Boolean Data type ---------------------------------------------------
print(True)
print(False)
# Also have boolean operator
print(True or False)
print(True and False)
print("-----------------------------------------------")

# Loops ---------------------------------------------------------------
# For Loops
groceries = ["rice", "sauce", "chicken", "soda"]
for item in groceries:
    print(item)

# loops also can use number
for i in range(0,10):
    print(i)
print("===============")

# While Loops (Selagi bla bla, bla bla)
x=10
while x>0:
    print(x)
    x-=1
print("-----------------------------------------------")

# Exception -----------------------------------------------------------
tools=["pen","eraser","pencil","ruler"]
#print(tools[4]) # this will produce an IndexError
try:
    print(tools[4]) 
except IndexError: # this will write proper index error depends on what we want to type
    print("Tools is not in list")
print("-----------------------------------------------")

# Function -------------------------------------------------------------
def wazap():
    print("Wazzap!!!")
wazap()

# if we write it twice, the outcome will be twice
wazap();wazap()
print("-----------------------------------------------")

# Object (include OOP) ---------------------------------------------------
class Person: # an example of object
    def __init__(self): # this is what we called constructor (so this constructor is a function that runs when we create our object)
        print("New Person")

p = Person()
print(p)
print("-----------------------------------------------")

# Inheritance (include OOP//relate to object) -----------------------------------------------
class Bruno(Person):
    def __init__(self):
        super().__init__()
        print("My name is Bruno Mars")

bruno = Bruno()
print(bruno)
print("-----------------------------------------------")

# Modules --------------------------------------------------
# We dont want to type everything over and over again
import math # this is a library on python
print(math.pi)