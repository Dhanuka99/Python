time = 10
if time<12:
    print("Good morning")
if time>12:
    print("Good afternoon")
print("have a great day")

x = int(input('Enter x: '))
if x > 100:
    k = x * 2
    if x >= 200:
        k = k * 3
    elif k < 300:
        k = k * 4
    else:
        k = k * 5
else:
    k = x * 3
print (k)

x = int(input('Enter x: '))
if (x > 100):
       k = x * 2
       if (x >= 200):
              k = k * 3
       elif (k < 300):
              k = k * 4
       else:
              k = k * 5
else:
       k = x * 3
print(k)

m = int(input('Enter an integer: '))

if (m < 1000):
    p = 2000 / m
else:
    p = m/1000
print(p)

mark = 55
if mark <= 39: grade = 'D'
elif mark < 55 : grade = 'C'
elif mark < 70 : grade = 'B'
else: grade = 'A'
print (grade)
