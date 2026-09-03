import math

# Question 2
print("Please enter the temperature in degrees Fahrenheit: ")
temperature = float(input())
print("Is it raining? ")
raining = input().lower()
if temperature < 32 and raining == "yes":
    print("Stay inside")
elif temperature < 50:
    print("Bring a coat")
elif temperature < 60:
    print("Wear a sweater")
else:
    print("Nice weather")

# Question 3
# num = int(input("Please enter an integer from 1 to 7: "))
num = 1
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Error")

# Question 4
myString = str(input("Please enter a string containing letters, digits, and other characters: "))
for char in myString:
    if char.isdigit():
        print(char, end="")

# Question 5
myNumber = int(input("Please enter a positive integer: "))
length = len(str(abs(myNumber)))
for _ in range(length):
    reverse = myNumber % 10
    print(reverse, end="")
    myNumber = myNumber // 10

# Question 6
# part '6a' runs the following commands in the interpreter
# import math and dir(math)

# part '6b'
print("Please enter an angle in degrees: ")
angleInDegrees = int(input())
theta = math.radians(angleInDegrees)
print(theta)

# part '6c'
sum_of_squares = math.sin(theta)**2 + math.cos(theta)**2
print(sum_of_squares)
if(sum_of_squares == 1):
    print("Equal")
else:
    print("Not equal")

# part '6d'

# i)
left = math.tan(theta)
right = math.sin(theta) / math.cos(theta)
print(left, right)
print(left == right)
print('%.16f' % (left))
print('%.16f' % (right))
difference = abs(left - right)
for tolerance in (0.001, 0.00001, 0.000000001):
    if(difference < tolerance):
        print("Equal")
    else:
        print("Not equal")

# ii)
left = math.cos(theta)
right = math.sin(math.pi / 2 - theta)
print(left, right)
print(left == right)
print('%.16f' % (left))
print('%.16f' % (right))
difference = abs(left - right)
for tolerance in (0.001, 0.00001, 0.000000001):
    if(difference < tolerance):
        print("Equal")
    else:
        print("Not equal")

# iii)
left = math.cos(2 * theta)
right = math.cos(theta) ** 2 - math.sin(theta) ** 2
print(left, right)
print(left == right)
print('%.16f' % (left))
print('%.16f' % (right))
difference = abs(left - right)
for tolerance in (0.001, 0.00001, 0.000000001):
    if(difference < tolerance):
        print("Equal")
    else:
        print("Not equal")

# iv)
left = math.sin(theta / 2)
right = math.sqrt((1 - math.cos(theta)) / 2)
print(left, right)
print(left == right)
print('%.16f' % (left))
print('%.16f' % (right))
difference = abs(left - right)
for tolerance in (0.001, 0.00001, 0.000000001):
    if(difference < tolerance):
        print("Equal")
    else:
        print("Not equal")
