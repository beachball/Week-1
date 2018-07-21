import time
start = time.time()
xd = list(range(1000, 0, -1))
newlist = []

while xd:
    minimum = xd[0]
    for x in xd:
        if x < minimum:
            minimum = x
    newlist.append(minimum)
    xd.remove(minimum)

print(newlist)
end = time.time()
cool = (end - start)
cool = str(cool)
print("")
print("This operation took:" + cool + "seconds!")
print("")
