'''
Created on Sept 24, 2017

@author: Austin Lee
'''


def process(name):
    # name is a file, returns a list of strings
    #    from the file
    f = open(name)
    answer = []
    for line in f:
        #answer.append(line.strip())
        answer.append(line.strip().split(":"))

    #answer = str(answer)
    #x = answer.split(":")
    return answer

def averageHeight(answer):
    total_height = 0
    x = 0
    for myList in answer:
        height = myList[4]
        height = int(height)
        total_height += height
        x+=1
        averageheight = total_height/x
    print("")
    print("The average height is:")
    print(averageheight)
    print("")
    print("")

def maxHeight(answer):
    max_height = 0
    for myList in answer:
        maxu_height = myList[4]
        maxu_height = int(maxu_height)
        if maxu_height > max_height:
            max_height = maxu_height
    print("")
    print("The maximum height is:")
    print(max_height)
    print("")
    print("")

def height_range(answer, height1, height2):
    height1 = 50
    hegith2 = 80
    for myList in answer:
        heightstart = myList[4]
        heightstart = int(heightstart)
        if heightstart <= height1:
            heightstart = height1
        else:
            heightstart = height2








filename = "athletes.txt"
data = process(filename)
print("THE DATA IS:")
for item in data:
    print(item)
averageHeight(data)
maxHeight(data)
height_range(data)
