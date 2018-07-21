#Factorial function
import time
start = time.time()
def factorialfunc():
    num = input("What number would you like to factorial? ")
    num = int(num)
    factorial = 1
    if num < 0:
        print("Number must be greater than 0.")
        exit()
    elif num == 0:
        print("The factorial of 0 is: 1")
        exit()
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    factorial = str(factorial)
    num = str(num)
    print("")
    print("The factorial of " + num + " is: " + factorial)
    print("")
factorialfunc()
end = time.time()
cool = (end - start)
cool = str(cool)
print("")
print("This operation took: " + cool + " seconds!")
print("")
