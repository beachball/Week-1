import time
def is_leap1 (year):
    year = input("Input year. ")
    year = int(year)
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year %   4 == 0:
        return True
    return False


a = "computational thinking"
b = "duke university"
c = "python code"

print("")
print(b[0]+a[1]+a[0]+b[2]+a[19:22])
print("Cost = 5")
print("")
print(a[14:18] + a[13] + a[18:22])
print("Cost = 3")
print("")
print(a[0:6] + b[9:11] + a[13] + c[7:11])
print("Cost = 4")
print("")
print(b[10] + a[6:8]*4)
print("Cost = 2")
print("")
print(b[0:4] +a[13] + b[7] + b[11] + a[13] + c[7:9] + a[9] + a[12])
print("Cost = 8")
print("")
print(b[0] + b[7:15] + a[13] + c[5] + a[11] + a[7:11])
print("Cost = 6")
print("")
print(a[2] + a[1] + a[10] + b[3] + b[14] + a[13] + c[3] + a[1] + a[10] + b[3] + b[14])
print("Cost = 12")
print("")



val = input("Enter a word. ")
i=0
time.sleep(3)
print("")
print("Here's your acronym!")
print("")
time.sleep(1)
while i < len(val):
    print(val[i])
    i += 1
print("")
