mylist = [2, -1, 3, 0, 100, 5]
range(1000000, 1, -1)
newlist = []

while mylist:
    minimum = mylist[0]
    for x in mylist:
        if x < minimum:
            minimum = x
    newlist.append(minimum)
    mylist.remove(minimum)

print(newlist)


# inserting a card into the deck makes room for the next card by shifting them to a
