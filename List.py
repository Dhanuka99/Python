# creating list
list1 = [1,2,3,4,5]
list2 = ['A','B','C','D']
list3 = ["apple","banana",23,69.5]

print(type(list1))
print(list1)
print(list2)
print(list3)
#access the element
print(list1[2])
print(list3[1])
print(list1[1:3])
print(list1[::2])
print(list1[2::])
print(list1[2:])
#add 60 to the end of the list1
list1.append(60)

print(list1)
del list1[0]
print(list1)

list = ['ph','ch',1997,2000,2000,2009]
list[2] = 2001
list.remove(2000)
list.append(2015)
print(list[2:])
print(len(list))
print("---------------------------------")
numlist = [2,4,6,8,3,4,2,1]
# iteration
for num in numlist:
    # check
    if num % 2 == 0:
        print(num)

