# Name: Yashvi Himanshu Gaglani

# solution 1
def isVowel(myChar) -> bool:
    if not isinstance(myChar, str):
        return False
    if len(myChar) != 1:
        return False
    if(myChar.upper() == "A" or myChar.upper() == "E" or myChar.upper() == "I" or myChar.upper() == "O" or myChar.upper() == "U"):
        return True
    else:
        return False

def testIsVowel():
    print(isVowel('A'))
    print(isVowel('G'))
    print(isVowel('a'))
    print(isVowel('aeiou'))

# solution 2
def countVowels(s):
    count = 0
    for char in s:
        if isVowel(char):
            count += 1
    return count

# solution 3
def getVowels(s):
    vowelList = [char for char in s if isVowel(char)]
    return vowelList

# solution 4
def toUppercase(words):
    return list(map(lambda w : w.upper(), words))

# solution 5
def transformNumbers(nums):
    return list(map(lambda x : 2*x + 1, nums))

# 6. The file simpleFunctions contains specifications for several functions. Consider the functions euclid(a,
# b) and isbn(digits).

def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    c = str(input("Please enter a character: "))
    myCharLength = len(c)
    isUpperCase = isVowel(c)
    print(isUpperCase)

    testIsVowel()

    s = str(input("Please enter a string: "))
    isVowelCount = countVowels(s)
    print(isVowelCount)

    #copied from the lab examples
    print(countVowels('abc123')) # should display 1
    print(countVowels('Now is the time')) # should display 5

    getVowel = str(input("Please enter a string: "))
    print(getVowels(getVowel))

    print(toUppercase(['dog', 'CAt', 'mOuSe']))

    print(transformNumbers([1, 2, 3, 4]))
