#comment for one line code
""" My comment """
x = 2 + 1
print(x)

a = "Wazzap!!!"
print(a)

# an example of list ---------------------------------------------------
b = ["Wazzap!!!", "Apa khabar!!!"] 
#print(b[0]) #output Wazzap!!!
#print(b) #output the list of b

b = b + [1,2,3,4]
print(b)

# an example of dictionaries -------------------------------------------
# Every dictionaries have a name that we call a key

c = {"favcolor":"purple and blue"} 
print(c["favcolor"]) #associative array

#an example of set ----------------------------------------------------
# set doesnt have order and repitition

d = {1,2,3,4,5,5,5,6,6,6}
print(d)
#can be add logic
x=2
if x==1:
    print("of course!")
if x==2:
    print("Obviously not!")