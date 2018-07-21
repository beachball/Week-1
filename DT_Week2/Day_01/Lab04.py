import time

word = input("Enter an uppercase word! ")
new = word.lower()
time.sleep(3)
print("")
print("Here is your new lowercase word!")
print(new)
print("")

maxi = max("science")
print(maxi)

value = input("Enter a string. ")
valuenew = value.endswith(value[-3:])
time.sleep(3)
print(valuenew)
time.sleep(2)
print("")
print("The method: 'str.endswith(str[-3:])' returns True because the word ends with a space, and the character -3 values behind the starting letter is a space.")
print("")


#print("The value of: 'reversed(sorted([5,4,1,2,8]))' is: 8,5,4,2,1 because python first sorts the list, then reverses the order of the list. )
