def printme(str,age):
    print(str,age)

printme("Dhanuka",32)

printme("kamal",43);

#printme("Dhanuka") #type error

def greet(*names):
    for name in names:
             print("Hello", name)


greet("Dhanuka","kamal","sidath","namal")

def add(a, b):
    return a+5, b+5
print(add(3, 2))
