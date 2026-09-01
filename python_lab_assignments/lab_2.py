print("Enter the speed of the object in miles per hour (mph):")
speed_mph = float(input())
speed_mps = speed_mph * 0.447
print(f"{speed_mph:.2f} mph = {speed_mps:.2f} m/s") 

time = 10  # time in seconds
distance_meters = speed_mps * time
print(f"In {time} seconds, the object travels {distance_meters:.2f} meters.")

print("Enter the weight of an object in pounds:")
weight_pounds = float(input())
weight_kilograms = weight_pounds * 0.4536
print(f"{weight_pounds:.2f} pounds = {weight_kilograms:.2f} kg")

print(f"{weight_kilograms*1000:.2f} grams")  # Converting kilograms to grams

first_name = input("Enter your first name: ")
favorite_food = input("Enter your favorite food: ")
home_town = input("Enter your hometown: ")
print(first_name + " from " + home_town + " likes " + favorite_food + ".")

with open('gradebook.txt', 'r') as f:
# <your code here: part c>
    total = 0
    count = 0
    for line in f:
        name, id, grade = line.strip().split(',')
        grade = int(grade)
        print(f"Name: {name}, ID: {id}, Grade: {grade}")
        total+= grade 
        count+=1
    avg = total / count
    print(f"Average Grade: {avg:.2f}")

sentence = "Assign the string variable sentence as this sentence."
print(sentence)
print(sentence.upper())
word = sentence.split(" ")
print(word)

capital_word = sentence.upper().split(" ")
print(capital_word)


word_on_s = sentence.split("s")
print(word_on_s)

position_1 = sentence.find("ten")
print(position_1)

position_2 = sentence.find("ten", position_1 + 1)
print(position_2)

tabby = '\t'
sentence_with_tab =  sentence.replace(" ", tabby)
print(sentence_with_tab)