programon = 1
print("This terminal is locked with a 5 digit password. Please enter the password to continue.")
#Password is 8/31/03
#First digit of the 5 digit password
firstdigit = input("Please enter the first digit of the password. ")
firstdigit = int(firstdigit)
if firstdigit == 8:
    check = 1
else:
    programon = 2
#Second digit of the 5 digit password
secondigit = input("Please enter the second digit of the password. ")
secondigit = int(secondigit)
if secondigit == 3:
    check = 2
else:
    programon = 3
#Third digit of the 5 digit password
thirdigit = input("Please enter the third digit of the password. ")
thirdigit = int(thirdigit)
if thirdigit == 1:
    check = 3
else:
    programon = 4
#Fourth digit of the 5 digit password
fourthdigit = input("Please enter the fourth digit of the password. ")
fourthdigit = int(fourthdigit)
if fourthdigit == 0:
    check = 4
else:
    programon = 5
#Fifth digit of the 5 digit password
fifthdigit = input("Please enter the fifth digit of the password. ")
fithdigit = int(fifthdigit)
if fifthdigit == 3:
    check = 5
else:
    programon = 6

if programon == 6:
    print("Password rejected. Application will terminate.")
if check == 5:
    print("Password accepted. Application will terminate.")
