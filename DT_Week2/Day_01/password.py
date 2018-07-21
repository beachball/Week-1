import time

def start():
    first = input("Please input the first number of the password. ")
    first = int(first)
    firstnum()

def firstnum():
    if first == 8:
        correct = 0
        correct = correct + 1
    else:
        time.sleep(3)
        print("")
        print("")
        print("Input incorrect. Program will terminate.")
        print("")
        print("")
        time.sleep(3)
        exit()

def secondnum():
    if second == 3:
        correct = 1
        correct = correct + 1
    else:
        time.sleep(3)
        print("")
        print("")
        print("Input incorrect. Program will terminate.")
        print("")
        print("")
        time.sleep(3)
        exit()

def thirdnum():
    if third == 1:
        correct = 2
        correct = correct + 1
    else:
        time.sleep(3)
        print("")
        print("")
        print("Input incorrect. Program will terminate.")
        print("")
        print("")
        time.sleep(3)
        exit()

def fourthnum():
    if fourth == 0:
        correct = 3
        correct = correct + 1
    else:
        time.sleep(3)
        print("")
        print("")
        print("Input incorrect. Program will terminate.")
        print("")
        print("")
        time.sleep(3)
        exit()

def fifthnum():
    if fifth == 3:
        correct = 4
        correct = correct + 1
        if correct == 5:
            time.sleep(3)
            print("")
            print("Terminal unlocked. Access granted.")
            print("")
            time.sleep(2)
            exit()
    else:
        time.sleep(3)
        print("")
        print("")
        print("Input incorrect. Program will terminate.")
        print("")
        print("")
        time.sleep(3)
        exit()


print("")
print("")
print("")
time.sleep(3)
print("This terminal is locked. You must enter a password to continue.")
time.sleep(3)
first = input("Please input the first number of the password. ")
first = int(first)
firstnum()
second = input("Please input the second number of the password. ")
second = int(second)
secondnum()
third = input("Please input the third number of the password. ")
third = int(third)
thirdnum()
fourth = input("Please input the fourth number of the password. ")
fourth = int(fourth)
fourthnum()
fifth = input("Please input the fifth number of the password. ")
fifth = int(fifth)
fifthnum()
