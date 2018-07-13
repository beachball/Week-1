print("")
print("Welcome to line printer!")
print("Options:")
print("Decreasing (1)")
print("Increasing (2)")
print("Repeating Pyramids (3)")
option = input("Please select your option. [1/2/3/4] ")
option = int(option)

# Decreasing in size
if option == 1:
    lineno = input("How many lines of stars would you like? ")
    lineno = int(lineno)
    star = "*"
    while lineno > 0:
        print(star * lineno * 2)
        lineno = lineno - 1

# Increasing in size
if option == 2:
    lineno = input("How many lines of stars would you like? ")
    lineno = int(lineno)
    count = 0
    star = "*"
    while count < lineno:
        count = count + 1
        print(count * star)

# Repeating Pyramids
if option == 3:
    lineno = input("How many lines of stars would you like? ")
    lineno = int(lineno)
    count = 0
    star = "*"
    while count < 5:
        count = count + 1
        print(count * star)
        lineno = lineno - 1
    while count > lineno:
        count = count - 1
        print(count * star)
        lineno = lineno + 1

# Expanding Pyramids (5 spaces)
if option == 4:
    lineno = input("How many lines of stars would you like? ")
    lineno = int(lineno)
    count = 0
    line1 = 0
    cash = "$"
    space = "     "
    space2 = "    "
    while count < lineno:
        count = count + 1
        print(space, count * cash)
        line1 = line1 + 1
        if

# Pascal's Triangle
