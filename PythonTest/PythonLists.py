def reverseString():
    stringToReverse = input("Please enter a string to reverse: ")
    print("String to Reverse: " + stringToReverse)
    print("Reversed String: " + stringToReverse[::-1])
    return

def lengthOfList(listLength=[]):
    if(len(listLength) == 0):
        listLength = input("Enter list items separated by comma (,) to find length of: ").split(',')
    print("Length: %s" % (len(listLength)))
    return

def sumList(listSum=[]):
    if(len(listSum) == 0):
        listSum = input("Enter list items separated by comma (,) to find sum of: ").split(',')
    sum = 0
    for i in listSum:
        sum = sum + int(i)
    print("Sum: %s" % sum)
    return

def avgList(listAvg=[]):
    if(len(listAvg) == 0):
        listAvg = input("Enter list items separated by comma (,) to find average of: ").split(',')
    avg = 0
    for i in listAvg:
        avg = avg + int(i)
    print("Average: %s" % (avg / len(listAvg)))
    return

def allList():
    listAll = input("Enter list items separated by comma (,) to get information of: ").split(',')
    print(listAll)
    lengthOfList(listAll)
    sumList(listAll)
    avgList(listAll)
    return

print("Welcome to the list test for Python!")

commandsList = ["Reverse String", "Length of List", "Sum List", "Average List", "All List"]
while(1):
    command = input("Please enter a command (" + ', '.join(commandsList) + "): ")
    switch = {
        "Reverse String": reverseString,
        "Length of List": lengthOfList,
        "Sum List": sumList,
        "Average List": avgList,
        "All List": allList
        }
    switch.get(command, "Sorry, that command is not in the list yet")()
