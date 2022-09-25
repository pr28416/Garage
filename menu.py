# get menu data
inFile = open('menu.txt', 'r')
menu = {}
print("Here's what is on the menu:")
for line in inFile:
    itemList = line.split()
    menu[itemList[0]] = float(itemList[1])
    print(itemList[0] + "\t" + itemList[1])
inFile.close()

# gather order
order = {}
while True:
    item = input("What would you like to order? (Say 'done' if finished) ")
    if item == 'done':
        break
    elif item not in menu:
        print("That's not on the menu!")
    else:
        amount = int(input("How many " + item + " do you want? "))