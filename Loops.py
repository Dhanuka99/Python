
list = [1,2,3,4,5,6,7,8,9,10]
#for loop
for counter in list:
    print("counter is : ",counter)


print("----------")

total = 0
for counter in range(0,101,2):
    print(counter)
    total+=counter
print(total)

a=0
for i in range(2,4):
    print(i)
    a=a+i
print(a)

#while
for counter in range(5):
    for co in range(10):
        print('$' ,end=' ')
    print(" ")


print(range(4))
for i in range(4):
    print(i)

print("---------")
numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    if number==1:
        break
else:
    count=-1
print(count)

for i in range(0,100,2):
    print(i)

num1 = 2
while (num1 !=0):
    num2 = 3
    while (num2 !=0) :
        print ("Hello World!")
        num2 = num2 - 1
    num1 = num1 - 1