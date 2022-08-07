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

print(int(3.0))

print("Dhanuka"*5)

c = "moratuwa university"
word = c[-4]+c[-2]
word += c[1:3]+c[0]
print (word)

c = "pythontutor"
word = c[1] + c[-2] + c[-4]
word += c[-3:-1] + c[0]
print (word)

x = "Computer Science and Engineering"
print (x[:3]+x[6]+x[9:12]+x[-11:-8])

for i in range(3,2,-1):
   print('!'*i)


