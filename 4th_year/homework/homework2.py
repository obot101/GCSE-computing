#import the time library
import time

#main function to ask user which program they would like to use
def main():
    #dictionary of all the programs
    programDict = {"Digit Extractor":digitExtractor, "Palindrome Checker":palindromeChecker,
                   "Sum Of Digits":sumOfDigits, "Time Converter":timeConvert,
                   "String Malipulation":stringMalip,
                    "Multiplication Table":multiTable}

    while True:
        #ask user for program of choice
        programChooser = input("Which program would you like to use, Digit Extractor, Palindrome Checker, Sum Of Digits, Time Converter, String Malipulation or Multiplication Table:\n").title()
        time.sleep(1)
        print(f"Opening {programChooser}")
        for i in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
        print("")
        #try to open program
        try:
            while True:
                programDict[programChooser]()
                digitC = input(f"Would you like to continue with {programChooser}? y or n\n")
                if digitC == "y":
                    continue
                else:
                    break
            userSecond = input("Would you like to open another program? y or n\n")
            if userSecond == "y":
                continue
            else:
                break
        #if key error is found repromt user for program
        except  KeyError:
            time.sleep(0.6)
            print("Errorrr")
            print("Please only choose a program from the list below.")
            time.sleep(1)
#digit extractor
def digitExtractor():
    threeDigit = int(input("Please enter a 3 digit nunber: "))
    print(f"{threeDigit // 100} hundreds")
    lastTwo = (threeDigit % 100)
    time.sleep(0.5)
    print(f"{lastTwo // 10} tens")
    time.sleep(0.5)
    print(f"{threeDigit % 10} ones")
#palindrome Checker
def palindromeChecker():
    word = input("Please enter a word: ")
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
#sum of deigits
def sumOfDigits():
    multiNumber = str(input("Please enter a number with multiple dijits: "))
    total = 0
    for i in multiNumber:
        total += int(i)
    print(f"The total is {total}")
#Time converter
def timeConvert():
    seconds = int(input("How many seconds?\n"))
    if seconds // 3200 == 1:
        print("1 hour")
    elif seconds // 3200 > 1:
        print(f"{seconds // 3200} hours")
    else:
        pass
    rem = seconds % 3200
    if rem // 60 == 1:
        print("1 minute")
    elif rem // 60 > 1:
        print(f"{rem // 60} mintues")
    else:
        pass
    if rem % 60 == 1:
        print("1 second")
    elif rem % 60 > 1:
        print(f"{rem % 60} seonds")
    else:
        pass
#string malipulation
def stringMalip():
    string = input("Please enter a string: ")
    print(f"First 3: {string[:3]}")
    time.sleep(0.5)
    print(f"Last 2: {string[-2:]}")
    time.sleep(0.5)
    print(f"String reversed: {string[::-1]}")
#multiplication table
def multiTable():
    number = int(input("Please enter a nunber: "))
    for i in range(10):
        print(f"{number} x {i + 1} = {(i + 1)*number}")
        time.sleep(0.5)
main()