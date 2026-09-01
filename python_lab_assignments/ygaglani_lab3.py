# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani

def question2():
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

def question3():
    num = int(input("Please enter an integer from 1 to 7: "))
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

def question4():
    myString = str(input("Please enter a string containing letters, digits, and other characters: "))
    for char in myString:
        if char.isdigit():
            print(char)

def question5():
    myNumber = int(input("Please enter a positive integer: "))
    length = len(str(abs(myNumber)))
    for _ in range(length):
        print(myNumber % 10, end="")
        myNumber = myNumber// 10

def main():
    # question2()
    # question3()
    # question4()
    question5()


if __name__ == "__main__":
    main()