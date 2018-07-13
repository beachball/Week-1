import math

def start():
    print("")
    print("")
    print("Available options include:")
    print("Addition (1)")
    print("Subtraction (2)")
    print("Multiplication (3)")
    print("Division (4)")
    print("Exponents (5)")
    print("Minimum (6)")
    print("Maximum (7)")
    print("Radix (8)")
    print("Binary to Octal (9)")
    print("Binary to Hex (10)")
    function = input("What operation would you like to do? ")

    #Addition function.
    if  function == "1":
        addfunc()

    #Subtraction function.
    if function == "2":
        subfunc()

    #Multiplication fuction.
    if function == "3":
        multfunc()

    #Division function.
    if function == "4":
        divfunc()

    #Power (Squaring) function.
    if function == "5":
        powerfunc()

    #Minimum function
    if function == "6":
        minfunc()

    #Maximum function
    if function == "7":
        maxfunc()

    #Radix-R Number System
    if function == "8":
        radixfunc()

    #Binary to Octal convertor
    if function == "9":
        octalfunc()

    #Binary to Hex convertor
    if function == "10":
        hexfunc()

def addfunc():
    number = input("Input the first number. ")
    number = float(number)
    additive = input("Input the number you would like to add. ")
    additive = float(additive)
    additionend = number+additive #Adding the number
    print(additionend)
    print("")
    print("All done!")
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def subfunc():
    number = input("Input the first number. ")
    number = float(number)
    subtractive = input("Input the number you would like to subtract. ")
    subtractive = float(subtractive)
    subtractionend = number-subtractive
    print(subtractionend)
    print("")
    print("All done!")
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def multfunc():
    number = input("Input the first number. ")
    number = float(number)
    multiplicative = input("Input the number you want to multiply by. ")
    multiplicative = float(multiplicative)
    multiplicative = number*multiplicative
    print(multiplicative)
    print("")
    print("All done!")
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def divfunc():
    number = input("Input the first number. ")
    number = float(number)
    dividend = input("Input the number you would like to divide by. ")
    dividend = float(dividend)
    quotient = number/dividend
    print(quotient)
    print("")
    print("All done!")
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def powerfunc():
    number = input("Input the first number. ")
    number = float(number)
    power = input("Input the power in which to put your number to. ")
    power = float(power)
    print(pow(number, power))
    print("")
    print("All done!")
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def squarefunc():
    number = input("Input the first number. ")
    number = float(number)
    sqrroot = number**(1/2.0)
    print("")
    print("All done!")
    print("")
    print("The square root of your number is:")
    print(sqrroot)
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def minfunc():
    amountofinput = input("How many numbers will you input? ")
    amountofinput = int(amountofinput)
    minseries = []
    currentmin = 1000000000000
    while amountofinput > 0:
        amountofinput = amountofinput - 1
        inputno = input("What number would you like to input? ")
        inputno = float(inputno)
        if inputno < currentmin:
            currentmin = inputno
    print("")
    print("All done!")
    print("")
    print("The minimum of that range is:")
    print(currentmin)
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def maxfunc():
    amountofinputmax = input("How many numbers will you input? ")
    amountofinputmax = int(amountofinputmax)
    maxseries = []
    currentmax = 0
    while amountofinputmax > 0:
        amountofinputmax = amountofinputmax - 1
        inputnomax = input("What number would you like to input? ")
        inputnomax = float(inputnomax)
        if inputnomax > currentmax:
            currentmax = inputnomax
    print("")
    print("All done!")
    print("")
    print("The maximum of that range is:")
    print(currentmax)
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def avgfunc():
    amountofinputavg = input("How many numbers would you like to input? ")
    amountofinputavg = int(amountofinputavg)
    totalsum = 0
    knucle = amountofinputavg
    while amountofinputavg > 0:
        numbers = input("What number would you like to input? ")
        numbers = float(numbers)
        totalsum += numbers
        amountofinputavg = amountofinputavg - 1
    avg = totalsum/knucle
    print("")
    print("All done!")
    print("")
    print("The average of that range is:")
    print(avg)
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def radixfunc():
    radnum = input("What number would you like to input? ")
    decimal = int(radnum, 2)
    decimal = str(decimal)
    print("")
    print("All done!")
    print("")
    print("The answer is: " + decimal)
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def octalfunc():
    octnum = input("Input any number in binary format. ")
    a , b = octnum.split(".")

    if len(a) % 3 == 1:
        a = "00" + a
    elif len(a) % 3 == 2:
        a = "0" + a

    if len(b) % 3 == 1:
        b = b + "00"
    elif len(b) % 3 == 2:
        b = b + "0"

    side_a = len(a)
    output = ""
    for index in range(0, len(a), 3):
        agroup = a[index:index+3]
        if agroup == "000":
            output = output + "0"
        if agroup == "001":
            output = output + "1"
        if agroup == "010":
            output = output + "2"
        if agroup == "011":
            output = output + "3"
        if agroup == "100":
            output = output + "4"
        if agroup == "101":
            output = output + "5"
        if agroup == "110":
            output = output + "6"
        if agroup == "111":
            output = output + "7"

    side_b = len(b)
    outputb = "."
    for index in range(0, len(b), 3):
        bgroup = b[index:index+3]
        if bgroup == "000":
            outputb = outputb + "0"
        if bgroup == "001":
            outputb = outputb + "1"
        if bgroup == "010":
            outputb = outputb + "2"
        if bgroup == "011":
            outputb = outputb + "3"
        if bgroup == "100":
            outputb = outputb + "4"
        if bgroup == "101":
            outputb = outputb + "5"
        if bgroup == "110":
            outputb = outputb + "6"
        if bgroup == "111":
            outputb = outputb + "7"

    print("")
    print("All done!")
    print("")
    print(output + outputb)
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

def hexfunc():
    hexnum = input("Input any number in binary format. ")
    c , d = hexnum.split(".")

    if len(c) % 4 == 1:
        c = "00" + c
    elif len(c) % 4 == 2:
        c = "0" + c

    if len(d) % 4 == 1:
        d = d + "00"
    elif len(d) % 4 == 2:
        d = d + "0"

    side_c = len(c)
    outputc = ""
    for index in range(0, len(c), 4):
        cgroup = c[index:index+4]
        if cgroup == "000":
            outputc = outputc + "0"
        if cgroup == "001":
            outputc = outputc + "1"
        if cgroup == "010":
            outputc = outputc + "2"
        if cgroup == "011":
            outputc = outputc + "3"
        if cgroup == "100":
            outputc = outputc + "4"
        if cgroup == "101":
            outputc = outputc + "5"
        if cgroup == "110":
            outputc = outputc + "6"
        if cgroup == "111":
            outputc = outputc + "7"
        if cgroup == "1000":
            outputc = outputc + "8"
        if cgroup == "1001":
            outputc = outputc + "9"
        if cgroup == "1010":
            outputc = outputc + "A"
        if cgroup == "1011":
            outputc = outputc + "B"
        if cgroup == "1100":
            outputc = outputc + "C"
        if cgroup == "1101":
            outputc = outputc + "D"
        if cgroup == "1110":
            outputc = outputc + "E"
        if cgroup == "1111":
            outputc = outputc + "F"

    side_d = len(d)
    outputd = "."
    for index in range(0, len(d), 4):
        dgroup = d[index:index+4]
        if dgroup == "000":
            outputd = outputd + "0"
        if dgroup == "001":
            outputd = outputd + "1"
        if dgroup == "010":
            outputd = outputd + "2"
        if dgroup == "011":
            outputd = outputd + "3"
        if dgroup == "100":
            outputd = outputd + "4"
        if dgroup == "101":
            outputd = outputd + "5"
        if dgroup == "110":
            outputd = outputd + "6"
        if dgroup == "111":
            outputd = outputd + "7"
        if dgroup == "1000":
            outputd = outputd + "8"
        if dgroup == "1001":
            outputd = outputd + "9"
        if dgroup == "1010":
            outputd = outputd + "A"
        if dgroup == "1011":
            outputd = outputd + "B"
        if dgroup == "1100":
            outputd = outputd + "C"
        if dgroup == "1101":
            outputd = outputd + "D"
        if dgroup == "1110":
            outputd = outputd + "E"
        if dgroup == "1111":
            outputd = outputd + "F"

    print("")
    print("All done!")
    print("")
    print(outputc + outputd)
    print("")
    again = input("Calculate again? (y/n) ")
    if again == "y":
        start()
    if again == "n":
        exit()

#Start of the program
print("")
print("Welcome to the calculator!")
print("")
print("Available options include:")
print("Addition (1)")
print("Subtraction (2)")
print("Multiplication (3)")
print("Division (4)")
print("Exponents (5)")
print("Square Roots (5a)")
print("Minimum (6)")
print("Maximum (7)")
print("Average (7a)")
print("Radix (8)")
print("Binary to Octal (9)")
print("Binary to Hex (10)")
function = input("What operation would you like to do? ")

#Addition function.
if  function == "1":
    addfunc()

#Subtraction function.
if function == "2":
    subfunc()

#Multiplication fuction.
if function == "3":
    multfunc()

#Division function.
if function == "4":
    divfunc()

#Power (Squaring) function.
if function == "5":
    powerfunc()

#Square Rooting functionself
if function == "5a":
    squarefunc()

#Minimum function
if function == "6":
    minfunc()

#Maximum function
if function == "7":
    maxfunc()

#Average
if function == "7a":
    avgfunc()

#Radix-R Number System
if function == "8":
    radixfunc()

#Binary to Octal convertor
if function == "9":
    octalfunc()

#Binary to Hex convertor
if function == "10":
    hexfunc()
